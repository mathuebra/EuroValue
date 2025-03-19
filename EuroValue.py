import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
COTACAO_FILE = "ultimo_valor.txt"

def enviar_mensagem(mensagem):
    """Envia uma mensagem para o Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, json=payload)

def obter_cotacao():
    """Obtém a cotação atual do Euro em relação ao Real"""
    url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
    resposta = requests.get(url).json()
    return round(float(resposta["EURBRL"]["bid"]), 2)  # Arredonda para 2 casas decimais

# Tenta ler o último valor salvo
if os.path.exists(COTACAO_FILE):
    with open(COTACAO_FILE, "r") as f:
        try:
            ultimo_valor = float(f.read().strip())
        except ValueError:
            ultimo_valor = None
else:
    ultimo_valor = None

# Obtém a nova cotação
cotacao = obter_cotacao()

if ultimo_valor is not None:
    if cotacao > ultimo_valor:
        enviar_mensagem(f"🔺 Euro subiu para R$ {cotacao:.2f}")
    elif cotacao < ultimo_valor:
        enviar_mensagem(f"🔻 Euro caiu para R$ {cotacao:.2f}")
    else:
        enviar_mensagem(f"🔹 Euro está estável em R$ {cotacao:.2f}")

# Salva a nova cotação no arquivo
with open(COTACAO_FILE, "w") as f:
    f.write(str(cotacao))
