from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! DXN botiga xush kelibsiz!")

async def katalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mahsulotlar = (
        "📦 DXN mahsulotlari:\n"
        "1. Lingzhi Black Coffee – Ganoderma + Qahva\n"
        "2. Vita Cafe – Tongkat Ali + Ganoderma\n"
        "3. Lion's Mane Coffee – Lion's Mane qo‘ziqorini\n"
        "4. Limonzhi choyi – Limon + Rozella + Gano\n"
        "5. EU Coffee – Gano + Hindiston yong‘og‘i suti\n"
    )
    await update.message.reply_text(mahsulotlar)

async def pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📄 Katalog yuklab olish: https://example.com/dxn_katalog.pdf")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("katalog", katalog))
app.add_handler(CommandHandler("pdf", pdf))
app.run_polling()