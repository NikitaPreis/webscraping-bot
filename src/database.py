from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from src.models import Base
from src.settings import Settings


settings = Settings()


engine = create_async_engine(
    url=settings.db_url,
    future=True,
    echo=True,
)


AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False
)

async_session = async_sessionmaker(engine)


async def get_db_session() -> AsyncSession:
    """Get db session."""
    async with AsyncSessionFactory() as session:
        return session


async def init_models():
    """Create all models."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
