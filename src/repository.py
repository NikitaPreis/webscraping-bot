from sqlalchemy.ext.asyncio import AsyncSession

from src.models import WebScrapingResource


class WebResourceRepository:
    """Repository of web resources for web scraping."""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_resources(
        self, resources: list[WebScrapingResource]
    ) -> None:
        async with self.db_session as session:
            session.add_all(resources)
            await session.commit()
