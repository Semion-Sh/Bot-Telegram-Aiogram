from aiogram import types
from create_bot import bot
from aiogram.dispatcher import Dispatcher
from Keyboards import main_kb
from DateBase import SqlLiteDb


async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name}', reply_markup=main_kb)
    except:
        await message.reply('Чтобы я смог с тобой общаться, напиши мне: https://web.telegram.org/z/#5258746451')


async def boys(message: types.Message):
    await SqlLiteDb.sql_read(message)


async def creator(message: types.Message):
    await bot.send_message(message.from_user.id, '@sem4ek')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    # dp.register_message_handler(boys, commands=['Boys'])
    dp.register_message_handler(creator, commands=['admin'])


async def empty(message: types.message):
    await message.answer('This command is not found')
