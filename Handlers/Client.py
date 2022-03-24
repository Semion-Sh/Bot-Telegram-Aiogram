from aiogram import types
from create_bot import dp, bot
from aiogram.dispatcher import Dispatcher
from Keyboards import kb_Client
from DateBase import SqlLiteDb


async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Choose from offers', reply_markup=kb_Client)
    except:
        await message.reply('Чтобы я смог с тобой общаться, напиши мне: https://web.telegram.org/z/#5258746451')

async def Boys(message: types.Message):
    await SqlLiteDb.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(Boys, commands=['Boys'])