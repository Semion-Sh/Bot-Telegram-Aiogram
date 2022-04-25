from aiogram import types
from create_bot import bot
from aiogram.dispatcher import Dispatcher, FSMContext
from Keyboards import main_kb
from DateBase import SqlLiteDb
from aiogram.types import BotCommand
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter

async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name}', reply_markup=main_kb)
    except:
        await message.reply('Чтобы я смог с тобой общаться, напиши мне: https://web.telegram.org/z/#5258746451')


async def commands_help(message: types.Message):
    await bot.send_message(message.from_user.id, '''
    Список команд:
/admin - профиль создателя Бота

                                                    ''')
# /bible - чтение Библии

async def boys(message: types.Message):
    await SqlLiteDb.sql_read(message)


async def creator(message: types.Message):
    await bot.send_message(message.from_user.id, '@sem4ek')


# async def mailing(message: types.Message):
#     await bot.send_message(message.from_user.id,
# '''Каждый день я буду отправлять опрос о твоём чтении Библии. У тебя будет мотивация читать слово Божье каждый день.
#
# Пришли \"Да\" - чтобы подписаться на рассылку или \"Нет\"''')
#     await Mailing.Text.set()
#
#
# async def bible(message: types.Message, state: FSMContext):
#     if message.text.lower() in ('да', 'yes', 'da'):
#         await bot.send_message('''Теперь каждый день я буду тебе отправлять опрос, отвечай честно, ведь это надо только тебе.
# В любой момент ты можешь отписаться от рассылки, написав мне "Cтоп"''')




# async def empty(message: types.message):
#     if message.text not in ('/admin'):
#         await bot.send_message(message.from_user.id, '''
#         Список команд:
# /admin - профиль создателя Бота
# /bible - чтение Библии
#                                                             ''')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(commands_help, commands=['help'])
    dp.register_message_handler(boys, commands=['boys'])
    # dp.register_message_handler(mailing, commands=['bible'])
    # dp.register_message_handler(bible, state=Mailing.Text)
    dp.register_message_handler(creator, ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['Admin'])
    # dp.register_message_handler(empty, ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
