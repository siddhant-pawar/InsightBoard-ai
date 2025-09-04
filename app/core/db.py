import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# ✅ Load .env file
load_dotenv()

# ✅ Read DATABASE_URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")

# ✅ Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# ✅ Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# ✅ Dependency for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
