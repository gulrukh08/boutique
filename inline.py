from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
import logging

admin_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram", url="https://t.me/aabdurakhimovaa"),
            InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/abdulvokhidovna_/")
        ],
        [
            InlineKeyboardButton(text="Ulashing", switch_inline_query="\nAssalomu aleykum! La Botique🌸 onlayn - do'konining rasmiy botiga xush kelibsiz! "
                                                                      "\nBu bot orqali onlayn xaridni amalga oshirishingiz mumkin😊\n/Botdan foydalanish uchun /start buyrug'ini yuboring."
                                                                      "⁉ Savol va murojaatlar uchun /help buyrug'ini bosing")
        ]
    ]
)

boglaning = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Biz bilan bog'laning", callback_data="boglanish"),
        ]
    ],
)