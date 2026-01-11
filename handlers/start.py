from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.builders import get_language_keyboard
from utils.texts import texts
from utils.storage import user_languages

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # Default to Uz greeting or mixed
    await message.answer(
        texts["uz"]["welcome"],
        reply_markup=get_language_keyboard()
    )

@router.message(F.text == texts["uz"]["btn"])
async def lang_uz(message: Message):
    user_languages[message.from_user.id] = "uz"
    await message.answer(texts["uz"]["lang_selected"])

@router.message(F.text == texts["ru"]["btn"])
async def lang_ru(message: Message):
    user_languages[message.from_user.id] = "ru"
    await message.answer(texts["ru"]["lang_selected"])

@router.message(F.text == texts["en"]["btn"])
async def lang_en(message: Message):
    user_languages[message.from_user.id] = "en"
    await message.answer(texts["en"]["lang_selected"])
