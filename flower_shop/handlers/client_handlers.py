from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from lexicon import LEXICON
from keyboards import (start_keyboard, occasion_kb_btns, create_inline_kb)


router = Router()

@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['clients_greeting'].format(
                                full_name=message.chat.full_name),
                         reply_markup=start_keyboard)


@router.message(F.text == LEXICON['next_button'])
async def process_choose_occasion(message: Message):
    await message.answer(text=LEXICON['any_occasion'],
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text=LEXICON['choose_occasion'],
                         reply_markup=create_inline_kb(1, *occasion_kb_btns))
