from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.texts import texts

def get_language_keyboard():
    buttons = [
        [KeyboardButton(text=texts["uz"]["btn"]), KeyboardButton(text=texts["ru"]["btn"])],
        [KeyboardButton(text=texts["en"]["btn"])]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)
