from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
class IsPrivat(BoundFilter):
    async def chek(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE
