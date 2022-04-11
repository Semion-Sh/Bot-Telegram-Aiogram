from aiogram import types
import json, string
from aiogram.dispatcher import Dispatcher
import asyncio, aioschedule
from kinds_of_poll import football_poll, sky_time_poll_1, sky_time_poll_2
from filters import IsPrivat
from aiogram.types import BotCommand

d = {
    'а': ['а', 'a', '@'],
    'б': ['б', '6', 'b'],
    'в': ['в', 'b', 'v'],
    'г': ['г', 'r', 'g'],
    'д': ['д', 'd', 'g'],
    'е': ['е', 'e'],
    'ё': ['ё', 'e'],
    'ж': ['ж', 'zh'],
    'з': ['з', 'z'],
    'и': ['и', 'u', 'i'],
    'й': ['й', 'u', 'i'],
    'к': ['к', 'k', 'i{', '|{'],
    'л': ['л', 'l', 'ji'],
    'м': ['м', 'm'],
    'н': ['н', 'h', 'n'],
    'о': ['о', 'o', '0'],
    'п': ['п', 'n', 'p'],
    'р': ['р', 'r', 'p'],
    'с': ['с', 'c', 's'],
    'т': ['т', 'm', 't'],
    'у': ['у', 'y', 'u'],
    'ф': ['ф', 'f'],
    'х': ['х', 'x', 'h', '}{'],
    'ц': ['ц', 'c', 'u,'],
    'ч': ['ч', 'ch'],
    'ш': ['ш', 'sh'],
    'щ': ['щ', 'sch'],
    'ь': ['ь', 'b'],
    'ы': ['ы', 'bi'],
    'ъ': ['ъ'],
    'э': ['э', 'e'],
    'ю': ['ю', 'io'],
    'я': ['я', 'ya']
}


async def mat_block(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()} \
            .intersection(set(json.load(open('cenz.json')))):
        name = message.from_user.first_name
        await message.answer(f'{name}, плохие слова запрещены!')
        await message.delete()


# football poll
async def spam_start():
    aioschedule.every(1).sunday.at('09:00').do(football_poll)
    aioschedule.every(1).wednesday.at('09:00').do(sky_time_poll_1)
    aioschedule.every(1).friday.at('09:00').do(sky_time_poll_2)
    aioschedule.every(1).tuesday.at('09:00').do(sky_time_poll_2)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def empty(message: types.message):
    if message.text:
        await message.answer('This command is not found')


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand('/Admin', ' - профиль создателя Бота'),
        BotCommand('/help', ' - профиль hghghghghg Бота'),
    ])


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mat_block)
    dp.register_message_handler(empty, IsPrivat)
    dp.register_message_handler(set_default_commands)
