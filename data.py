# Salomlashuv matni
welcome_text = (
"🧕 *Assalomu alaykum azizim!*\n"
    "🌿 *TabibAiBuvi* botiga xush kelibsiz! 🌸\n\n"
    "🤖 Sun’iy intellekt + 30 yillik tabobat tajribasi bir joyda.\n\n"
    "📌 Ushbu bot orqali siz:\n"
    "💚 Tabiiy davolash bo‘yicha maslahatlar\n"
    "☕️ DXN mahsulotlari bo‘yicha tavsiyalar\n"
    "🧭 Shaxsiy rivojlanish bo‘yicha yo‘l‑yo‘riqlar\n"
    "🔥 Har tongki ruhlantiruvchi motivatsiya\n"
    "👶 Bolalar va yoshlarga mo‘ljallangan sog‘lomlik yo‘nalishlari\n\n"
    "👇 Quyidagilardan birini tanlang va sog‘lom hayot sari birinchi qadamingizni tashlang!"
)
# Yordam matni
help_text = (
    "🆘 Bot bo‘yicha yordam:\n\n"
    "📌 Asosiy menyudan kerakli bo‘limni tanlang.\n"
    "📬 Agar dardingizni aytmoqchi bo‘lsangiz, 'Salomatlik bo‘yicha maslahat'ni tanlang.\n"
    "📚 DXN mahsulotlari bo‘yicha savollaringiz bo‘lsa, 'DXN mahsulotlari' tugmasini bosing.\n"
    "🔥 Har kuni motivatsiya kerak bo‘lsa, 'Motivatsiya' bo‘limiga murojaat qiling.\n"
    "\n🚑 Sizning sog‘lig‘ingiz — biz uchun muhim."
)
# Bot haqida matn
# Bot haqida matn
about_text = (
    "📚 *TabibAiBuvi* — bu sun’iy intellekt va 30 yillik dorivor tajribasi asosida yaratilgan maslahatchi bot.\n\n"
    "🧵 Misol: agar sizda qon bosimi, melisa choyi yoki dorivor o‘simlik bo‘yicha savol bo‘lsa,\n"
    "— men sizga aniq protokollar va tavsiyalar beraman.\n"
    "😊 Bu bot orqali siz ruhiy ko‘mak, tabiiy sog‘lomlashtirish va haqiqiy maslahat olasiz.\n"
)
# Aloqa uchun matn
contact_text = (
    "📱 Biz bilan bog‘laning:\n"
    "Telegram: @TabibAiBuvijon\n"
    "Telefon: +998 976 351 616\n"
    "Yopiq kanal: https://t.me/TabibAibuvi\n\n"
    "‼️ Sizdan kelgan har bir savolga mejburiy va samimiy javob olasiz."
)

# Motivatsiya – har safar random tanlanadi
from random import choice
motivations = [
    "Harakat qiling – hayotingiz o‘zgaradi. Siz bunga munosibsiz.",
    "Bugun boshlanmasangiz, hech qachon boshlamaysiz.",
    "Kuchli bo‘ling, siz bunga haqli va loyiqsiz.",
    "Orzularingiz kutmoqda — ularga hoziroq intiling.",
    "Siz ichingizdagi yulduzingizni yo‘qotmang. Yorug‘lik siz bilan.",
    "Har bir yangi tong – yangi imkoniyat.",
    "Buguni qadrlang, harakat qiling, g‘alaba sizniki bo‘ladi.",
    "Sog‘ligingiz — sizga eng katta sovg‘a.",
    "Tinchlik va ruhiy salomatlik — har bir nafasda.",
    "Sen kuchlisan. Ishora senga bardosh!"
]
def get_random_motivation():
   return choice(motivations)
# data.py

motivatsiya_matnlari = [
    "Harakat qiling, hayotingiz o'zgaradi.",
    "Bugun boshlanmasangiz, hech qachon boshlamaysiz.",
    "Kuchli bo‘ling, siz bunga loyiqsiz!",
    "Har kuni kichik qadamlar katta natijalarga olib keladi.",
    "Siz o‘zgarishni istaysizmi? Unda hoziroq boshlang!",
    "Ishonch bilan boshlang — natijalar keladi!",
    "Harakat – bu muvaffaqiyatning kaliti!",
    "Sizda cheksiz imkoniyatlar bor, harakatni to‘xtatmang!",
    "Bugun qilgan har bir harakatingiz ertangi sizga xizmat qiladi.",
    "Orqaga emas, faqat oldinga!"
]

# Keyingi yangilanishlarda boshqa matnlar, holatlar qo‘shilishi mumkin








 








