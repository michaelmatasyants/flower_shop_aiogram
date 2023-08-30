from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from lexicon import LEXICON
from keyboards import (occasion_text_btns, create_inline_kb)


router = Router()


@router.message(F.text == LEXICON['next_button'])
async def process_choose_occasion(message: Message):
    await message.answer(text=LEXICON['any_occasion'],
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text=LEXICON['choose_occasion'],
                         reply_markup=create_inline_kb(1, *occasion_text_btns))


@router.callback_query(F.data.in_(occasion_text_btns[-1])) #F.text == occasion_text_btns[-1]
async def get_custom_occasion(callback: CallbackQuery):
    print(callback.json())
    await callback.message.answer(text=LEXICON['input_custom_occasion'])


#@router.callback_query(F.te)
#async def all_messages(message: Message):
#    print(message)


#@router.callback_query(F.text.in_(occasion_text_btns[:-1]))
#async def add_occasion_to_db