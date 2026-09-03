from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = (
    "postgresql+asyncpg://postgres:password@localhost:5432/student_db"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)