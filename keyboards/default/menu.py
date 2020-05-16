from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Молоко"),
        ],
        [
            KeyboardButton(text="Кофе"),
            KeyboardButton(text="Другое")
        ],
    ],
    resize_keyboard=True
)
