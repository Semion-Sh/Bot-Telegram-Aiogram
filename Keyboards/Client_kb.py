from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/admin')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/bible')
b4 = KeyboardButton('где я', request_location=True)

main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b2)
