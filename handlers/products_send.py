from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db import main_db
from aiogram.types import InputMediaPhoto


async def start_send_products(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_all_products = types.InlineKeyboardButton('Вывести все товары',
                                                     callback_data='send_products')

    keyboard.add(button_all_products)


async def send_all_products(call: types.CallbackQuery):
    products = main_db.sql_get_all_products()

    if products:
        for product in products:
            caption = (f'Название - {product["name"]}\n'
                       f'Размер - {product["size"]}\n'
                       f'Категория - {product["category"]}\n'
                       f'Артикул - {product["product_id"]}\n'
                       f'Информация о товаре - {product["info_product"]}\n'
                       f'Цена - {product["price"]}\n')

            await call.message.answer_photo(photo=product['photo'], caption=caption)
    else:
        await call.message.answer('Товаров нет')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=['products'])
    dp.register_callback_query_handler(send_all_products, Text(equals='send_products'))