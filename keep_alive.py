from flask import Flask
from threading import Thread
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot ishlayapti!"
def run():
    app.run(host='0.0.0.0', port=8082)
def keep_alive():
    t = Thread(target=run)
    t.start()
