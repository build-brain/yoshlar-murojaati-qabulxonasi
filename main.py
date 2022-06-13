"""
 This is a bot.
"""
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5242807366:AAF8pFlM3ecs83tdb-o3ExgrOhUzk36k9Uc'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
  await bot.send_message(message.from_user.id, 'Assalomu Aleykum' )



if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
