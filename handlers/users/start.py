from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from handlers.users.menu import menu
from loader import dp


@dp.message_handler(IsPrivate(), Command("start"), state="*")
async def command_start(message: types.Message, state: FSMContext = False):
    if state:
        await state.finish()

    await message.answer(
        "Приветствуем вас в нашем проекте! Мы создали данного бота для поднятия важной и острой проблемы связанной с экологией 🌿\n"
        "Для чего же нужен данный бот? 🧐\n"
        "•Он полезен для жителей города или района, чтобы узнавать, где находятся ближайшие мусорные баки, где производят вывоз мусора, а также где находятся центры переработки мусора 📍\n"
        "•Полезная информация с видами мусора и как правильно его сортировать ♻️\n"
        "•Бот может помочь облегчить жизнь людям, позволяя им быть более организованными и предусмотрительными в отношении утилизации мусора ❗️\n"
        "•Расскажет о проблемах и фактах, связанных с мусором 🥸\n"
        "Надеемся данная информация будет полезна для вас, удачного пользования ☺️\n")

    await menu(message)
