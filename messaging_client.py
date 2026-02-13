from logger import log

def send_message(user_id, message):
    log("BOT", f"Enviando mensagem para {user_id}")
    log("BOT", f"Conteúdo: {message}")
