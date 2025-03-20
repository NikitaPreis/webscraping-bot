import asyncio

from aiogram import Bot, Dispatcher

from src.database import init_models
from src.handlers import router
from src.settings import Settings


async def main():

    await init_models()

    settings = Settings()

    bot = Bot(
        token=settings.BOT_API_TOKEN,
    )

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
