import os
import openai
from flask import Flask, request
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TOKEN)
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

# /start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! TabibAIbuvi botiga xush kelibsiz!")

# Matnga javob berish
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Siz foydalanuvchiga foydali, qulay va iliq tilda maslahat beruvchi TabibAIbuvi botisiz."},
                {"role": "user", "content": message.text},
            ]
        )
        reply = response['choices'][0]['message']['content']
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi. Iltimos, keyinroq urinib ko‘ring.")

# Flask route
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

# Webhook sozlash
@app.route('/')
def index():
    return 'Bot ishga tushdi!', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
