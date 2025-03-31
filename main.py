import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.excel_handler import router
from db.repository import repo


load_dotenv()

API_TOKEN = getenv("API_TOKEN")


dp = Dispatcher()
dp.include_router(router=router)


async def main() -> None:
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await repo.initialize()

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
