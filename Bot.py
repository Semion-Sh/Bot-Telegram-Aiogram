from create_bot import dp, bot
from DateBase import SqlLiteDb
from aiogram.utils import executor
from Handlers import Client, Other, Admin
import asyncio, filters
from Handlers.Other import spam_start
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import types


async def set_all_default_commands(bot: Bot):
    await set_default_commands(bot)


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[BotCommand('Admin', ' - профиль создателя Бота')]
    )


async def start_bot(_):
    print('Bot is starting')
    SqlLiteDb.sql_start()
    asyncio.create_task(spam_start())
    filters.setup(dp)
    # set_default_commands



Admin.register_handlers_admin(dp)
Client.register_handlers_client(dp)
Other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
