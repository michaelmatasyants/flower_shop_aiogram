import os
import time
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import start_keyboard
from lexicon import LEXICON
from database import get_delivery_man_ids


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    if message.chat.id in get_delivery_man_ids():
        await message.answer(text=LEXICON['delivery_greeting'].format(
                                    full_name=message.chat.full_name),
                             reply_markup=start_keyboard)
    else:
        await message.answer(text=LEXICON['clients_greeting'].format(
                                    full_name=message.chat.full_name),
                             reply_markup=start_keyboard)
