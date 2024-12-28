from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

Staff = [7224280710, ]

token = config("TOKEN")
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)