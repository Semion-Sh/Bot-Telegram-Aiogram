from create_bot import dp, bot
from DateBase import SqlLiteDb
from aiogram.utils import executor
from Handlers import Client, Other, Admin
import asyncio
from Handlers.Other import spam_start
from Handlers.Other import bot_commands


async def start_bot(_):
    print('Bot is starting')
    SqlLiteDb.sql_start()
    asyncio.create_task(spam_start())
    await bot.set_my_commands(bot_commands)


Admin.register_handlers_admin(dp)
Client.register_handlers_client(dp)
Other.register_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
