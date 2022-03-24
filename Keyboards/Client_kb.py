from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Boys')
b2 = KeyboardButton('/')
b3 = KeyboardButton('/')
b4 = KeyboardButton('где я', request_location=True)

kb_Client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_Client.row(b1, b2, b3).add(b4)
