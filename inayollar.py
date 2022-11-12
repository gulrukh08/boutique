from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

women = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Zakaz", callback_data="request_women"),
        ],
        [
            InlineKeyboardButton(text="Orqaga", callback_data="womens"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="Menu"),
        ],
    ]
)