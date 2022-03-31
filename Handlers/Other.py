from aiogram import types
import json, string
from aiogram.dispatcher import Dispatcher
import asyncio
from kinds_of_poll import football_poll, sky_time_poll_1, sky_time_poll_2
import aioschedule

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

name = None

async def mat_block(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()} \
            .intersection(set(json.load(open('cenz.json')))):
        global name
        name = message.from_user.full_name
        if name:
            await message.reply(f'{name}, ты же христианин, плохие слова запрещены!')
        else:
            await message.reply(f'Ты же христианин, плохие слова запрещены!')
        await message.delete()


# football poll
loop = asyncio.get_event_loop()


async def spam_start():
    aioschedule.every(1).sunday.at("12:00").do(football_poll)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

try:
    loop.run_until_complete(spam_start())
except KeyboardInterrupt:
    exit(0)
# sky_time_poll poll_1
loop = asyncio.get_event_loop()
async def spam_start1():
    aioschedule.every(1).thursday.at("12:00").do(sky_time_poll_1)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
try:
    loop.run_until_complete(spam_start1())
except KeyboardInterrupt:
    exit(0)

# sky_time_poll poll_2
loop = asyncio.get_event_loop()
async def spam_start2():
    aioschedule.every(1).friday.at("12:00").do(sky_time_poll_2)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
try:
    loop.run_until_complete(spam_start2())
except KeyboardInterrupt:
    exit(0)

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mat_block)
