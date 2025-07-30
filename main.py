from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def home():
    return "Bot beží!"

@app.route(f"/webhook", methods=["POST"])
def webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]
    message_text = data["message"]["text"]

    response = {
        "chat_id": chat_id,
        "text": f"Odpoveď na: {message_text}"
    }

    requests.post(TELEGRAM_API_URL, json=response)
    return {"ok": True}
