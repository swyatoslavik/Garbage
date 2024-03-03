from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from handlers.users.menu import menu
from loader import dp


@dp.message_handler(IsPrivate(), Command("help"), state="*")
async def command_help(message: types.Message, state: FSMContext = False):
    if state:
        await state.finish()

    await message.answer(
        "Как же пользоваться ботом? 🤔\n"
        "Все очень просто:\n"
        "1. Зайдите в главное меню 🏠\n"
        "2. Выберите пункт, который вам необходим 📲\n"
        "3. Отправьте свою геолокацию 📍\n"
        "4. Бот выдаст вам ближайшие мусорные баки, производство вывоза мусора или центры переработки мусора 🏢\n\n"
        "Спасибо, что воспользовались нашим ботом ❤️")

    await menu(message)
