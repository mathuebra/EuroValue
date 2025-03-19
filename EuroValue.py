import requests
import time
from datetime import datetime

TOKEN = "8133639212:AAGEvGAvkiHsEk4jpjsWQSuYIMF2IweTr1s"
CHAT_ID = "1352048677"

def enviar_mensagem(mensagem):
    agora = datetime.now().strftime("%H:%M:%S")
    mensagem = f"{mensagem}\n🕒 {agora}"  # Adiciona horário para evitar mensagens idênticas
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, json=payload)

def obter_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
    resposta = requests.get(url).json()
    print(f"📊 Cotação obtida: {resposta}")  # Depuração
    return float(resposta["EURBRL"]["bid"])

ultimo_valor = obter_cotacao()
enviar_mensagem(f"📢 Monitoramento iniciado. Cotação atual: R$ {ultimo_valor:.2f}")

while True:
    cotacao = obter_cotacao()
    
    if cotacao != ultimo_valor:  # Qualquer mudança, notifica
        if cotacao > ultimo_valor:
            enviar_mensagem(f"🔺 Euro subiu para R$ {cotacao:.2f}")
        else:
            enviar_mensagem(f"🔻 Euro caiu para R$ {cotacao:.2f}")

        ultimo_valor = cotacao  # Atualiza o último valor
    
    time.sleep(1800)  # Espera 30 minutos antes de verificar de novo
