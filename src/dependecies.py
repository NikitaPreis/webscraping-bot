from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db_session
from src.repository import WebResourceRepository
from src.service import WebScrapingService


async def get_web_resource_repository() -> WebResourceRepository:
    db_session: AsyncSession = await get_db_session()
    return WebResourceRepository(db_session=db_session)


async def get_web_scraping_service() -> WebScrapingService:
    web_resource_repository = await get_web_resource_repository()
    return WebScrapingService(web_resource_repository=web_resource_repository)
