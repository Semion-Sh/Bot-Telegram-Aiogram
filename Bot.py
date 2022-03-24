from aiogram.utils import executor
from create_bot import dp
from DateBase import SqlLiteDb


async def start_bot(_):
    print('Bot is starting')
    SqlLiteDb.sql_start()


from Handlers import Client, Other, Admin

Client.register_handlers_client(dp)
Admin.handlers_for_Admin(dp)
Other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
