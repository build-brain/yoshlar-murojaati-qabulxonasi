"""
 This is a bot.
"""
 
import logging
 
from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '5242807366:AAF8pFlM3ecs83tdb-o3ExgrOhUzk36k9Uc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu Aleykum")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
