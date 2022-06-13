from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Varriables
# menu button
btnMainMenu = KeyboardButton('MainMenu')
# other buttons
btnOther = KeyboardButton('Other')
# button button
btnButton_informations = KeyboardButton('Button_informations')

# Main menu
MainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnButton_informations, btnOther)

# Other menu
OtherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add()

# BuildBrain menu
Button_informations = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMainMenu)
