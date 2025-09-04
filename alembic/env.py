# alembic/env.py
from __future__ import annotations
import asyncio
import os
import sys
from logging.config import fileConfig
from pathlib import Path

from sqlalchemy import pool, text as sa_text
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine.url import make_url

from alembic import context
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Project root + .env
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
# ensure project root is in path so `app` imports work when alembic runs
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# load .env if present
load_dotenv(PROJECT_ROOT / ".env")

# Alembic config object
config = context.config

# setup Python logging from alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ---------------------------------------------------------------------------
# Database URL resolution — only from alembic.ini
# ---------------------------------------------------------------------------
DATABASE_URL = config.get_main_option("sqlalchemy.url")

# Basic validation / helpful print
try:
    parsed = make_url(DATABASE_URL)
    print(f"[alembic/env.py] Using DATABASE_URL drivername: {parsed.drivername}")
except Exception as e:
    raise RuntimeError(f"Invalid DATABASE_URL: {DATABASE_URL!r} — parse error: {e}") from e

# ensure alembic config is aware of the resolved URL
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ---------------------------------------------------------------------------
# Import the project's MetaData object for 'autogenerate'
# ---------------------------------------------------------------------------
try:
    # Adjust this import based on where your Base is defined
    from app.models.task import Base
except Exception as exc:
    raise RuntimeError(
        "Failed importing app.models.task. Ensure your models import has no side-effects "
        "and that PROJECT_ROOT is on sys.path."
    ) from exc

target_metadata = Base.metadata

# ---------------------------------------------------------------------------
# Migration run helpers
# ---------------------------------------------------------------------------
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode without DB connectivity."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Synchronous migration runner used within run_sync from async connection."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode using an async engine."""
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
