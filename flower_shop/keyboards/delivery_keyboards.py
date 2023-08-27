from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from lexicon import LEXICON



start_keyboard = ReplyKeyboardMarkup(
                    keyboard=[[KeyboardButton(text=LEXICON['start_button'])]],
                    resize_keyboard=True)
