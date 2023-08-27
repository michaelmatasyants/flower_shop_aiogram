import os
import time
from aiogram import Router, F
from aiogram.types import (Message, ReplyKeyboardRemove, CallbackQuery,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.filters import CommandStart
from filters.is_admin import IsAdmin, IsPlaced
from keyboards import start_keyboard
from lexicon import LEXICON


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_shop.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
import django
from django.conf import settings

if not settings.configured:
    django.setup()

from mainapp.models import Order

router = Router()
router.message.filter(IsAdmin([341559729, 1110823712]))


@router.message(CommandStart())
async def process_admin_start_command(message: Message):
    await message.answer(text=LEXICON['delivery_greeting'].format(
                                full_name=message.chat.full_name),
                        reply_markup=start_keyboard)


@router.message(F.text == LEXICON['start_button'])
async def process_show_orders(message: Message):
    await message.answer(text=LEXICON['instruction'],
                         reply_markup=ReplyKeyboardRemove())
    time.sleep(1)
    placed_orders = Order.objects.filter(status='P')  \
                        .order_by('-delivery_date', '-delivery_time')
    for order in placed_orders:
        orders_keyboard_button = InlineKeyboardButton(
                            text=LEXICON['order_delivered_button'],
                            callback_data=f'{order.id}')
        orders_keyboard = InlineKeyboardMarkup(
                            inline_keyboard=[[orders_keyboard_button]])
        await message.answer(text=LEXICON['show_accepted_orders'].format(
                                    order_id=order.id,
                                    recipient_name=order.recipient_name,
                                    delivery_date=order.delivery_date,
                                    delivery_time=order.delivery_time,
                                    delivery_address=order.delivery_address),
                             reply_markup=orders_keyboard)
        time.sleep(1)


@router.callback_query(IsPlaced([order[0] for order
                                in Order.objects.filter(status='P')  \
                                    .values_list('id')]))
async def process_change_order_status_and_say_thanks(callback: CallbackQuery):
    delivered_order_id = int(callback.data)
    #await callback.message.delete(chat_id=callback.message.chat.id,
    #                              message_id=callback.message.message_id)
    Order.objects.filter(id=delivered_order_id
                         ).update(status=LEXICON['status_delivered'])
    await callback.message.answer(text=LEXICON['thanks'].format(
                                        order_id=delivered_order_id))
    await callback.answer(text=LEXICON['order_delivered_button'])


#@router.message(HasntOrders())
#async def process_no_placed_orders(message: Message):
#    await message.answer(text=LEXICON['no_orders_available'])