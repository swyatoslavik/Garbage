from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from keyboards.default import kb_menu
from loader import dp


@dp.message_handler(IsPrivate(), Command("menu"), state="*")
async def menu(message: types.Message, state: FSMContext = False):
    if state:
        await state.finish()
    await message.answer("🏠Главное меню:", reply_markup=kb_menu)
