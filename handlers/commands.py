from aiogram import types, Dispatcher
from config import dp, bot
from aiogram.dispatcher.filters import Text

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в наш магазин! Используйте /info для получения информации.")

@dp.message_handler(commands=["info"])
async def cmd_info(message: types.Message):
    await message.answer("Это бот для управления магазином: добавление товаров, оформление заказов.")

def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cmd_info, commands="info")