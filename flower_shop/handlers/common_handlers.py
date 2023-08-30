from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import clients_start_kb, delivery_start_kb
from lexicon import LEXICON
from database import get_delivery_man_ids
from filters.is_admin import IsAdmin


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    if IsAdmin(get_delivery_man_ids()):
        await message.answer(text=LEXICON['delivery_greeting'].format(
                                    full_name=message.chat.full_name),
                             reply_markup=delivery_start_kb)
    else:
        await message.answer(text=LEXICON['clients_greeting'].format(
                                    full_name=message.chat.full_name),
                             reply_markup=clients_start_kb)
