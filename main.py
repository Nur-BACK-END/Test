from aiogram import executor
from config import bot, dp, Staff
import logging
from handlers import commands, fsm

import buttons
from db import main_db


async def on_startup(dp):
    for staff in Staff:
        await bot.send_message(chat_id=staff, text='Бот включен!',
                               reply_markup=buttons.start_markup)
    await main_db.DataBase_create()


commands.register_commands_handlers(dp)
fsm.register_fsm_client_handlers(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)