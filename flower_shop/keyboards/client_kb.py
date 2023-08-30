from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon import LEXICON


clients_start_kb = ReplyKeyboardMarkup(
                    keyboard=[[KeyboardButton(text=LEXICON['next_button'])]],
                    resize_keyboard=True)

occasion_text_btns = [occasion_btn.strip() for occasion_btn
                      in LEXICON['occasion_buttons'].split(',')]
