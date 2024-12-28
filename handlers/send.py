from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db import main_db
from config import Staff
from aiogram.types import InputMediaPhoto


async def start_send_clients(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_all_products = types.InlineKeyboardButton('Вывести все товары',
                                                     callback_data='send_all_products')

    keyboard.add(button_all_products)


async def send_all_products(call: types.CallbackQuery):
    clients = main_db.sql_get_all_clients()

    if Staff:
        for client in clients:
            caption = (f'Артикул - {client["product_id"]}\n'
                       f'quantity - {client["quantity"]}\n'
                       f'size - {client["size"]}\n'
                       f'number - {client["number"]}\n'
                       )

            await call.message.answer_photo(photo=client['photo'], caption=caption)
    else: # False
        await call.message.answer('Товаров нету')



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_send_clients, commands=['client'])
    dp.register_callback_query_handler(send_all_products, Text(equals='send_all_products'))