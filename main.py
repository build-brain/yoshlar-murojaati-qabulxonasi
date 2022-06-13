"""
 This is a bot.
"""
import logging
from aiogram import Bot, Dispatcher, executor, types
import MyButtons
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentTypes

API_TOKEN = '5242807366:AAF8pFlM3ecs83tdb-o3ExgrOhUzk36k9Uc'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
  await bot.send_message(message.from_user.id, 'Assalomu Alaykum {0.first_name} men bot man iltimos tilni tanlang!'.format(message.from_user), reply_markup=MyButtons.Languige)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
  await bot.send_message(message.from_user.id, "for start /start\n for help /help\n for stop /stop!")
  
#bot.py
@dp.callback_query_handler(text_contains="leng")
async def LanguigeUzRus(message: types.Message):
  if message.text == btnUzbekleng:
    # @btnUzbek
    async def name1(message: types.Message):
      await bot.send_message(message.from_user.id, "Iltimos ismingizni kiriting")
      name = name1()
      await bot.send_message(message.from_user.id, 'Sizning ismingiz ' + name + 'tugrimi ?')
      async def phone1(message: types.Message):
        await bot.send_message(message.from_user.id, 'Iltimos ' + name + ' nomer raqamingiszni kiriting')
        phone = phone1()
        await bot.send_message(message.from_user.id, 'Sizning nomeringiz ' + phone + 'tugrimi ?')
        async def adress1(message: types.Message):
          await bot.send_message(message.from_user.id, 'Iltimos ' + name + ' adresingizni kiriting')
          adress = adress1()
          await bot.send_message(message.from_user.id, 'Sizning adresingiz ' + adress + 'tugrimi ?')
          async def date1(message: types.Message):
            await bot.send_message(message.from_user.id, 'Iltimos ' + name + ' bugungi sanani kiriting')
            date = date1()
            await bot.send_message(message.from_user.id, 'Bugungi sana ' + date + 'tugrimi ?')
            async def text1(message: types.Message):
              await bot.send_message(message.from_user.id, 'Iltimos ' + name + ' murojatingizni kiriting')
              text = text1()
  elif message.text == btnRussianleng:
    # @btnRussian
    async def name1(message: types.Message):
      await bot.send_message(message.from_user.id, 'Пожалувсто введите свое имя')
      name = name1()
      await bot.send_message(message.from_user.id, 'Sizning ismingiz ' + name + 'tugrimi ?')
      async def phone1(message: types.Message):
        await bot.send_message(message.from_user.id, 'Пожалуйвсто ' + name + ' Введите свой номер телефона')
        phone = phone1()
        await bot.send_message(message.from_user.id, 'Ваш номер телефона ' + phone + 'правильно ?')
        async def adress1(message: types.Message):
          await bot.send_message(message.from_user.id, 'Пожалуйвсто ' + name + ' введите свой адрес')
          adress = adress1()
          await bot.send_message(message.from_user.id, 'Sizning adresingiz ' + adress + 'правильно ?')
          async def date1(message: types.Message):
            await bot.send_message(message.from_user.id, 'Пожалуйвсто ' + name + ' введите сегодняшнюю дату')
            date = date1()
            await bot.send_message(message.from_user.id, 'Bugungi sana ' + date + 'правильно ?')
            async def text1(message: types.Message):
              await bot.send_message(message.from_user.id, 'Пожалуйвсто ' + name + ' введите обрашение')
              text = text1()
 
if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
