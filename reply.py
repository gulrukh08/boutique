from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging



menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Erkaklar uchun👨"),
            KeyboardButton(text="Ayollar uchun👩"),
            KeyboardButton(text="Bolalar uchun👶"),
        ],
        [
            KeyboardButton(text="Contact📞"),
            KeyboardButton(text="Zakazlar")
        ],
    ],
    resize_keyboard=True
)


erkaklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ko'ylak👔"),
            KeyboardButton(text="Shim👖"),
            KeyboardButton(text="Oyoq kiyim👞"),
        ],
        [
            KeyboardButton(text="Bosh menyu"),
        ],
    ],
    resize_keyboard=True
)

ayollar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ko'ylak👗"),
            KeyboardButton(text="Yubka"),
            KeyboardButton(text="Oyoq kiyim👠"),
        ],
        [
            KeyboardButton(text="Bosh menyu"),
        ],
    ],
    resize_keyboard=True
)

bolalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ko'ylak👕"),
            KeyboardButton(text="Shim🩳"),
            KeyboardButton(text="Oyoq kiyim👟"),
        ],
        [
            KeyboardButton(text="Bosh menyu"),
        ],
    ],
    resize_keyboard=True
)

send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Phone number📞", request_contact=True),
        ],
    ],
    resize_keyboard=True
)

send_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Location🚩", request_location=True)
        ],
        [
            KeyboardButton(text="Bosh menyu")
        ]
    ],
    resize_keyboard=True
)

otmen = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Zakazni bekor qilish"),
            KeyboardButton(text="Bosh menyu")
        ]
    ],
    resize_keyboard=True
)