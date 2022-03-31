from create_bot import dp
from DateBase import SqlLiteDb
from aiogram.utils import executor
from Handlers import Client, Other, Admin


async def start_bot(_):
    print('Bot is starting')
    SqlLiteDb.sql_start()


Admin.handlers_for_admin(dp)
Client.register_handlers_client(dp)
Other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
