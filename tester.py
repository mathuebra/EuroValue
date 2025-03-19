import requests

TOKEN = "8133639212:AAGEvGAvkiHsEk4jpjsWQSuYIMF2IweTr1s"
CHAT_ID = "1352048677"

def enviar_mensagem(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, json=payload)

enviar_mensagem("Bot configurado!")
