from aiogram import Router, F, Bot
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery, ContentType

from src.dependecies import get_web_scraping_service
from src.exceptions import AllResourcesInvalidException
from src.settings import Settings
from src.service import WebScrapingService
from src.utils import get_added_resources_text
from src.schemas import WebResourceCreateSchema
from src import keyboards, text


router = Router(
    name='web_scraping',
)


@router.message(Command('start'))
async def cmd_start(message: Message):
    """Start command."""
    await message.answer(text.greet, reply_markup=keyboards.menu)


@router.message(F.text.lower() == 'меню')
@router.message(F.text.lower() == 'menu')
@router.message(Command('menu'))
async def cmd_menu(message: Message):
    """Menu command."""
    await message.answer(text.menu, reply_markup=keyboards.menu)


@router.callback_query(F.data == 'request_user_excel_file')
async def request_user_excel_file(
    callback: CallbackQuery
):
    """Request the user to upload an Excel file."""
    await callback.message.answer(text.request_user_upload_file)


@router.message(F.content_type == ContentType.DOCUMENT)
async def add_websites_for_scraping_from_excel(message: Message, bot: Bot):
    """Download excel file and add web resources for scraping."""

    settings = Settings()
    web_scraping_service: WebScrapingService = (
        await get_web_scraping_service()
    )

    name = message.document.file_id
    download_file_path = f'{settings.BASE_DIR}/files/{name}.xlsx'
    await bot.download(
        message.document,
        destination=download_file_path
    )

    try:
        web_resources_schemas: WebResourceCreateSchema = (
            await web_scraping_service.add_websites_for_scraping(
                excel_filepath=download_file_path
            )
        )
        resources_success = get_added_resources_text(
            web_resources=web_resources_schemas
        )
        await message.answer(resources_success)
    except AllResourcesInvalidException as e:
        await message.answer(text.all_resources_invalid_message)
