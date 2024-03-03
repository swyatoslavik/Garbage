from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨‍💻Помощь"),
            KeyboardButton(text="🤔Проблемы и факты")
        ],
        [
            KeyboardButton(
                text='♻️Полезная информация с видами мусора и как правильно его сортировать ')
        ],
        [
            KeyboardButton(text='📍Мусорные баки'),
            KeyboardButton(text='📍Вывоз мусора'),
            KeyboardButton(text='📍Переработка мусора')
        ]
    ],
    resize_keyboard=True
)
