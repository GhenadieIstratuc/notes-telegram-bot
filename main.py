from aiogram import Bot, Dispatcher
import asyncio
import os
from notes import user_router

TOKEN = os.environ.get("NOTES_BOT_TOKEN")
ALLOWED_DATA = ["message, edited_message"]

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(user_router)


async def main():
    await dp.start_polling(bot, allowed_updates=ALLOWED_DATA)

asyncio.run(main())
