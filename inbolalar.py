from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

kid = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Zakaz", callback_data="request_kids"),
        ],
        [
            InlineKeyboardButton(text="Orqaga", callback_data="kids"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="Menu"),
        ],
    ],
)