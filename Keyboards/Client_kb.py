from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Admin')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/Holy_Bible')
b4 = KeyboardButton('где я', request_location=True)

main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1, b2).add(b3)
