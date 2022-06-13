from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Varriables
# menu button
Languige = InlineKeyboardMarkup(row_width=2)
btnUzbekleng = InlineKeyboardButton(text="Uzbekleng", callback_data="btnUzbekleng")
btnRussianleng = InlineKeyboardButton(text="Russianleng", callback_data="btnRussianleng")



Languige.insert(btnUzbekleng)
Languige.insert(btnRussianleng)

