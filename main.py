"""
 This is a bot.
"""
import logging
from aiogram import Bot, Dispatcher, executor, types
import MyButtons
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from PIL import Image
print(Image.__version__)

API_TOKEN = '5242807366:AAF8pFlM3ecs83tdb-o3ExgrOhUzk36k9Uc'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
  await bot.send_message(message.from_user.id, 'Hello {0.first_name} I\'m InfoBot\nMy commandes:\nfor start /start\n for help /help\n for quit /quit!'.format(message.from_user), reply_markup=MyButtons.MainMenu)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
  await bot.send_message(message.from_user.id, "for start /start\n for help /help\n for quit /quit\n for more informations /informations!")

@dp.message_handler(commands=['informations'])
async def send_welcome(message: types.Message):
  await bot.send_message(message.from_user.id, "")

#PARROT
# @dp.message_handler()
# async def echo(message: types.Message):
#   await message.answer(message.from_user.id, "Sorry we havn\'t got command like that yest! " + message.text)



@dp.message_handler()
async def command_start(message: types.Message):
  # MainMenu
  if message.text == ('MainMenu' or '/MainMenu'):
    await bot.send_message(message.from_user.id, 'MainMenu', reply_markup=MyButtons.MainMenu)

  # Botton_informations
  if message.text == ('Button_informations' or '/Button_informations'):
    await bot.send_message(message.from_user.id, 'Button_info', reply_markup=MyButtons.Button_informations)

  # Other
  if message.text == ('OtherMenu' or '/OtherMenu'):
    await bot.send_message(message.from_user.id, 'Other', reply_markup=MyButtons.OtherMenu)
    
    

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
