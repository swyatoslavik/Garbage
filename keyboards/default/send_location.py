from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_send_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить геолокацию", request_location=True)
        ],
    ],
    resize_keyboard=True
)
