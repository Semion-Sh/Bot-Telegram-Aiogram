from aiogram import types
from create_bot import dp
import json, string
from aiogram.dispatcher import Dispatcher



async def mat_block(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()} \
            .intersection(set(json.load(open('cenz.json')))):
        await message.reply('Ты же христианин, плохие слова запрещены!')
        await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mat_block)
