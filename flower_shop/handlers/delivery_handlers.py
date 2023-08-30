import time
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from filters.is_admin import IsAdmin, IsPlaced
from lexicon import LEXICON
from database import (get_delivery_man_ids, get_palced_orders,
                      get_placed_order_ids, set_order_status)
from keyboards import create_order_inline_kb


router = Router()
router.message.filter(IsAdmin(get_delivery_man_ids()))


@router.message(F.text == LEXICON['show_orders'])
async def process_show_orders(message: Message):
    await message.answer(text=LEXICON['instruction'],
                         reply_markup=ReplyKeyboardRemove())
    placed_order_ids = get_palced_orders()
    for order in placed_order_ids:
        await message.answer(text=LEXICON['show_accepted_orders'].format(
                                    order_id=order.id,
                                    recipient_name=order.recipient_name,
                                    delivery_date=order.delivery_date,
                                    delivery_time=order.delivery_time,
                                    delivery_address=order.delivery_address),
                             reply_markup=create_order_inline_kb(order))
        time.sleep(1)


@router.callback_query(IsPlaced(get_placed_order_ids()))
async def process_change_order_status(callback: CallbackQuery):
    placed_order_id = int(callback.data)
    await set_order_status(order_id=placed_order_id,
                           status=LEXICON['status_delivered'])
    await callback.message.answer(text=LEXICON['thanks'].format(
                                        order_id=placed_order_id))
    await callback.answer(text=LEXICON['order_delivered_button'])


@router.message()
async def process_no_placed_orders(message: Message):
    await message.answer(text=LEXICON['no_orders_available'])
