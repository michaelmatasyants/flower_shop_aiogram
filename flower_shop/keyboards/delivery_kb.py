from aiogram.types import (InlineKeyboardButton, KeyboardButton,
                           ReplyKeyboardMarkup, InlineKeyboardMarkup)
from lexicon import LEXICON
from mainapp.models import Order


delivery_start_kb = ReplyKeyboardMarkup(
                        keyboard=[[
                            KeyboardButton(text=LEXICON['show_orders'])]],
                        resize_keyboard=True)


def create_order_inline_kb(order: Order):
    orders_kb_btn = InlineKeyboardButton(
                        text=LEXICON['order_delivered_button'],
                        callback_data=order.id)
    order_inline_kb = InlineKeyboardMarkup(inline_keyboard=[[orders_kb_btn]])
    return order_inline_kb
