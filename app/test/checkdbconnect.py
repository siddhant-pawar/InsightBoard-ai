import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy import text  # ✅ Import text()

# ✅ Async DB URL
DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/insight"

async def check_async_db_connection(url):
    print(f"🔍 Checking async DB connection for: {url}")
    try:
        engine = create_async_engine(url, echo=False)

        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))  # ✅ Wrap SQL in text()
            print("✅ Async DB connection successful.")
            print("Result:", result.scalar())

        await engine.dispose()

    except OperationalError as e:
        print("❌ Database connection failed.")
        print(f"Error: {e}")
    except Exception as e:
        print("❌ Unexpected error.")
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(check_async_db_connection(DATABASE_URL))
