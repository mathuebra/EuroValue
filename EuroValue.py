import requests
import time
import os

# Token e Chat ID do Telegram
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Função para enviar mensagem pelo bot
def enviar_mensagem(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, json=payload)

# Função para obter a cotação do Euro
def obter_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
    resposta = requests.get(url).json()
    return round(float(resposta["EURBRL"]["bid"]), 2)  # Mantém 2 casas decimais

# Caminho do arquivo de cache
cache_path = "ultimo_valor.txt"

# Verifica se o arquivo existe, senão cria com valor padrão
if not os.path.exists(cache_path):
    with open(cache_path, "w") as f:
        f.write("0.00")

# Lê o último valor do cache
with open(cache_path, "r") as f:
    ultimo_valor = float(f.read().strip())

# Obtém a nova cotação
cotacao = obter_cotacao()

# Compara e envia mensagem, se necessário
if cotacao > ultimo_valor:
    enviar_mensagem(f"🔺 Euro subiu para R$ {cotacao:.2f}")
elif cotacao < ultimo_valor:
    enviar_mensagem(f"🔻 Euro caiu para R$ {cotacao:.2f}")
else:
    enviar_mensagem(f"🔹 Euro está estável em R$ {cotacao:.2f}")

# Salva a nova cotação no cache
with open(cache_path, "w") as f:
    f.write(str(cotacao))
