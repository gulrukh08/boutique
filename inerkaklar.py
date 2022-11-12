from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
import logging

men = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Zakaz", callback_data="request_men"),
        ],
        [
            InlineKeyboardButton(text="Orqaga", callback_data="mens"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="Menu"),
        ]
    ]
)