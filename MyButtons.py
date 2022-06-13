from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Varriables
# menu button
Languige = InlineKeyboardMarkup(row_width=2)
btnUzbek = InlineKeyboardButton(text="Uzbek", callback_data="btnUzbek")
btnRussian = InlineKeyboardButton(text="Russian", callback_data="btnRussian")



Languige.insert(btnUzbek)
Languige.insert(btnRussian)

