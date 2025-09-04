import os
import sys
import asyncio
import asyncpg
from logging.config import fileConfig
from alembic import command
from alembic.config import Config
from pathlib import Path
from sqlalchemy.engine.url import make_url

# Load .env file if exists
from dotenv import load_dotenv
load_dotenv()  # This loads environment variables from .env into os.environ

# Ensure the project root is in the path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Load Alembic configuration
alembic_cfg = Config(str(PROJECT_ROOT / "alembic.ini"))

# Optionally override the database URL from environment
db_url = os.getenv("ALEMBIC_DATABASE_URL")
if db_url:
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)
else:
    db_url = alembic_cfg.get_main_option("sqlalchemy.url")

async def ensure_db_exists(database_url: str):
    # Parse the URL with SQLAlchemy
    url = make_url(database_url)

    # Strip '+asyncpg' from drivername for asyncpg compatibility
    clean_scheme = url.drivername.split('+')[0]  # e.g. 'postgresql+asyncpg' -> 'postgresql'
    url = url.set(drivername=clean_scheme)

    db_name = url.database
    # Connect to default 'postgres' database to check/create target database
    default_db_url = url.set(database="postgres").render_as_string(hide_password=False)

    print(f"Connecting to default database to check if '{db_name}' exists...")
    conn = await asyncpg.connect(default_db_url)
    exists = await conn.fetchval("SELECT 1 FROM pg_database WHERE datname=$1", db_name)

    if not exists:
        print(f"Database '{db_name}' does not exist. Creating...")
        await conn.execute(f'CREATE DATABASE "{db_name}"')
        print(f"Database '{db_name}' created.")
    else:
        print(f"Database '{db_name}' already exists.")

    await conn.close()

if __name__ == "__main__":
    print("Ensuring database exists before running migrations...")
    asyncio.run(ensure_db_exists(db_url))

    print("Running database migrations...")
    command.upgrade(alembic_cfg, "head")
    print("Migrations complete!")
