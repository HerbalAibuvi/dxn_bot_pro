import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# OpenAI (modern SDK)
from openai import OpenAI

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Init OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)

# Simple reply keyboard
keyboard = ReplyKeyboardMarkup(
    [["❓ Savol berish", "📞 Aloqa"], ["🌿 Dorivor giyohlar", "☕ DXN mahsulotlari"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! @Aibuvi_bot — DXN mahsulotlari va dorivor giyohlar bo‘yicha savollaringizga javob beradi.",
        reply_markup=keyboard
    )

async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # Compose a short system prompt to keep replies on-topic
    system_prompt = (
        "Siz DXN mahsulotlari va dorivor giyohlar bo‘yicha foydalanuvchiga sodda, qisqa va foydali javob beradigan Telegram bot yordamchisiz. "
        "Kerak bo'lsa, sog'lom turmush bo'yicha ham qisqa maslahat bering."
    )

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            temperature=0.6,
        )
        answer = resp.choices[0].message.content
    except Exception as e:
        logging.exception("OpenAI error")
        answer = "Kechirasiz, hozir javob bera olmadim. Birozdan so‘ng yana urinib ko‘ring."

    await update.message.reply_text(answer)

if __name__ == "__main__":
    if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
        raise RuntimeError("TELEGRAM_TOKEN va OPENAI_API_KEY .env yoki environment’da berilishi shart.")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    print("Aibuvi bot running (polling)...")
    app.run_polling()