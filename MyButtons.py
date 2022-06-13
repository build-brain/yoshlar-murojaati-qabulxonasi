from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Varriables
# menu button
btnMainMenu = KeyboardButton('MainMenu')
# other buttons
btnLanguige = KeyboardButton('Languige')
# # button button
# btnButton_informations = KeyboardButton('Button_informations')

# languige guttones
btnButton_Russian = KeyboardButton(text)()('Russian')
btnButton_Uzbek = KeyboardButton(text)(text)('Uzbek')

# Main menu
MainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnLanguige)

# Other menu
Languige = ReplyKeyboardMarkup(resize_keyboard = True).add(btnButton_Russian, btnButton_Uzbek)

# # BuildBrain menu
# Button_informations = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMainMenu)