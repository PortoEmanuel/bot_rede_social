from logger import log

def init_db():
    log("DATABASE", "Banco de dados inicializado")

def save_interaction(event, intent, response):
    log("DATABASE", f"Salvando interação → user: {event['user_id']} | intent: {intent}")
