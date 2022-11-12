from aiogram.types import Message, CallbackQuery
from aiogram import executor
from config import dp, bot
from reply import *
from inline import *
from inerkaklar import *
from inayollar import *
from inbolalar import *
from ballar import *

import logging



@dp.message_handler(commands='start')
async def start(message: Message):
    txt = f"🌝Assalomu aleykum {message.from_user.full_name}! \nLa Boutique ga xush kelibsiz!" \
          f"\nBu bot orqali 💠La Botique dan onlayn haridni amalga oshirishingiz mumkin\n\n" \
          f"❓ Yordam uchun /help buyrug'ini yuboring"
    await message.answer_photo(open("image/logo.jpg", "rb"), caption=txt, reply_markup=menuStart)


@dp.message_handler(commands='help')
async def helpme(message: Message):
    txt = "⁈ Savol va Takliflar uchun @aabdurakhimovaa ga murojaat qilishingiz mumkin"
    await message.answer_photo(open("image/help.jpg", "rb"), caption=txt)

@dp.message_handler(text="Contact📞")
async def contact(message: Message):
    await message.answer("Savol va murojaatlar uchun biz bilan bog'lanishingiz mumkin 📞📲", reply_markup=boglaning)

@dp.callback_query_handler(text_contains="boglanish")
async def one(call: CallbackQuery):
    await call.message.answer_photo(open("image/logo.jpg", "rb"), caption="💬Ijtimoiy tarmoqlarda bizning manzillarimiz:", reply_markup=admin_btn)
    await call.answer(cache_time=60)

@dp.message_handler(text="Bosh menyu")
async def menu(message: Message):
    await message.answer("Kerakli bo'limni tanlang:", reply_markup=menuStart)


@dp.message_handler(text="Erkaklar uchun👨")
async def erkaklarm(message: Message):
    txt = "🛍Men's Clothing\nErkaklar uchun kiyimlar\nKiyim tanlash uchun pastdan kerakli ruknni tanlang!" \
          "\n\n* * * * * * * * * *" \
          "\n💠La Boutique - kiyim do'koni" \
          "\n\nt.me/Botique_shopping_bot"
    await message.answer_photo(open("image/menslogo.jpg", 'rb'), caption=txt, reply_markup=erkaklar)

@dp.message_handler(text="Ayollar uchun👩")
async def ayollarm(message: Message):
    txt = "🎀WOMEN's Clothing\nAyollar uchun kiyimlar\nKiyim tanlash uchun pastdan kerakli ruknni tanlang!" \
          "\n\n* * * * * * * * * *" \
          "\n💠La Boutique - kiyim do'koni" \
          "\n\nt.me/Botique_shopping_bot"
    await message.answer_photo(open("image/womenslogo.jpg", 'rb'), caption=txt, reply_markup=ayollar)

@dp.message_handler(text="Bolalar uchun👶")
async def bolalarm(message: Message):
    txt = "👼Kids' Clothing\nBolalar uchun kiyimlar\nKiyim tanlash uchun pastdan kerakli ruknni tanlang!" \
          "\n\n* * * * * * * * * *" \
          "\n💠La Boutique - kiyim do'koni" \
          "\n\nt.me/Botique_shopping_bot"
    await message.answer_photo(open("image/kidslogo.jpg", 'rb'), caption=txt, reply_markup=bolalar)





@dp.message_handler(text="Ko'ylak👔")
async def e_k(message: Message):
    await message.answer_photo(open("erkaklar/koylak/1.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/2.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/3.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/4.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/5.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/6.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/7.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/8.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/9.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/koylak/10.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)

@dp.message_handler(text="Shim👖")
async def e_sh(message: Message):
    await message.answer_photo(open("erkaklar/shim/1.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/2.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/3.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/4.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/5.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/6.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/7.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/8.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/9.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/shim/10.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=men)

@dp.message_handler(text="Oyoq kiyim👞")
async def e_o(message: Message):
    await message.answer_photo(open("erkaklar/oyoqkiyim/1.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/2.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/3.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/4.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/5.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/6.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/7.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/8.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/9.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)
    await message.answer_photo(open("erkaklar/oyoqkiyim/10.jpg", "rb"), "Razmer: 38-45\nNarx:", reply_markup=men)



@dp.message_handler(text="Ko'ylak👗")
async def a_k(message: Message):
    await message.answer_photo(open("ayollar/koylak/1.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/2.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/3.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/4.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/5.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/6.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/7.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/8.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/9.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/koylak/10.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)


@dp.message_handler(text="Yubka")
async def a_y(message: Message):
    await message.answer_photo(open("ayollar/yubka/1.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/2.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/3.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/4.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/5.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/6.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/7.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/8.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/9.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/yubka/10.jpg", "rb"), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=women)

@dp.message_handler(text="Oyoq kiyim👠")
async def a_o(message: Message):
    await message.answer_photo(open("ayollar/oyoqkiyim/1.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/2.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/3.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/4.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/5.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/6.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/7.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/8.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/9.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)
    await message.answer_photo(open("ayollar/oyoqkiyim/10.jpg", 'rb'), "Razmer: 35-40\nNarx:", reply_markup=women)


@dp.message_handler(text="Ko'ylak👕")
async def b_k(message: Message):
    await message.answer_photo(open("bolalar/koylak/1.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/2.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/3.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/4.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/5.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/6.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/7.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/8.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/9.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/koylak/10.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)

@dp.message_handler(text="Shim🩳")
async def b_sh(message: Message):
    await message.answer_photo(open("bolalar/shim/1.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/2.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/3.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/4.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/5.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/6.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/7.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/8.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/9.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/shim/10.jpg", 'rb'), "Razmer: S-M-L-XL-2XL\nNarx:", reply_markup=kid)

@dp.message_handler(text="Oyoq kiyim👟")
async def b_o(message: Message):
    await message.answer_photo(open("bolalar/oyoqkiyim/1.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/2.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/3.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/4.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/5.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/6.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/7.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/8.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/9.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)
    await message.answer_photo(open("bolalar/oyoqkiyim/10.jpg", 'rb'), "Razmer: 20-36\nNarx:", reply_markup=kid)

@dp.message_handler(text="Zakazlar")
async def zkzlar(message: Message):
    await message.answer(f"{Ans.summa} ta zakaz mavjud", reply_markup=otmen)

@dp.message_handler(text="Zakazni bekor qilish")
async def zkzlar(message: Message):
    Ans.summa = 0
    await message.answer(f"{Ans.summa} ta zakaz mavjud", reply_markup=menuStart)

@dp.callback_query_handler(text_contains="Menu")
async def menu2(call: CallbackQuery):
    await call.message.answer("Kerakli bo'limni tanlang:", reply_markup=menuStart)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="mens")
async def mf(call: CallbackQuery):
    await call.message.answer("Erkaklar kiyimlari:", reply_markup=erkaklar)

@dp.callback_query_handler(text_contains="womens")
async def wf(call: CallbackQuery):
    await call.message.answer("Ayollar kiyimlari:", reply_markup=ayollar)

@dp.callback_query_handler(text_contains="kids")
async def kf(call: CallbackQuery):
    await call.message.answer("Bolalar kiyimlari:", reply_markup=bolalar)

w = 0
m = 0
k = 0
@dp.callback_query_handler(text_contains="request_men")
async def locate(call: CallbackQuery):
    await call.message.answer("Raqamingizni yuboring:", reply_markup=send_contact)

@dp.callback_query_handler(text_contains="request_kids")
async def locate(call: CallbackQuery):
    await call.message.answer("Raqamingizni yuboring:", reply_markup=send_contact)

@dp.callback_query_handler(text_contains="request_women")
async def locate(call: CallbackQuery):
    await call.message.answer("Raqamingizni yuboring:", reply_markup=send_contact)

@dp.message_handler(content_types='contact')
async def tekshir(message: Message):
    await message.answer("Manzilingizni iyuboring:", reply_markup=send_location)

@dp.message_handler(content_types='location')
async def buyurtma(message: Message):
    await message.answer("Buyurtma muvaffaqiyatli qabul qilindi! Tez orada yetkazib beramiz)")
    a = Ans()



if __name__ == '__main__':
    executor.start_polling(dp)