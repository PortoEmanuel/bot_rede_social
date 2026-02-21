import requests
from config import PAGE_ACCESS_TOKEN, API_VERSION
from logger import log

def get_user_name(user_id):
    url = f"https://graph.facebook.com/{API_VERSION}/{user_id}?fields=first_name&access_token={PAGE_ACCESS_TOKEN}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("first_name", "Cliente")
        return "Cliente"
    except:
        return "Cliente"

def send_message(recipient_id, message_text):
    log("BOT", f"Enviando resposta real para {recipient_id}")
    
    url = f"https://graph.facebook.com/{API_VERSION}/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            log("BOT", "✅ Mensagem entregue com sucesso!")
        else:
            log("ERROR", f"Falha na Meta: {response.status_code} - {response.text}")
    except Exception as e:
        log("ERROR", f"Erro de conexão: {e}")