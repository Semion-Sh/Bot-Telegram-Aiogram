from aiogram import Dispatcher
from .privat_chat import IsPrivat


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivat)