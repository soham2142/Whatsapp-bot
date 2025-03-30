import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart  # ✅ Correct import for handling /start command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Router

# Directly set your bot token
TOKEN = "7581258251:AAETYACJkhnMabB2NKmE6wim1SoOZH0924o"  # Replace with your actual bot token
WEBPAGE_URL = "https://your-hosted-webpage.com"  # Replace with your actual hosted page URL

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Logging setup
logging.basicConfig(level=logging.INFO)

@router.message(CommandStart())  # ✅ Correct way to handle /start command in Aiogram v3
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌍 Open Forex Webpage", url=WEBPAGE_URL)]
    ])
    
    await message.answer("Welcome to the Forex Web Bot! Click below to access live forex rates and ads.", reply_markup=keyboard)

async def main():
    dp.include_router(router)  # Register the router
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
