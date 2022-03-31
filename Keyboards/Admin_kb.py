from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton('➕/upload')
button_delete = KeyboardButton('✖️/delete')
button_end = KeyboardButton('❌️/end')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_load, button_delete).add(button_end)

