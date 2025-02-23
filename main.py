import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config
from aiogram import Bot, Dispatcher

from handlers.start import start_router

bot = Bot(token=config('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())