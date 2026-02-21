from flask import Flask, request
from config import VERIFY_TOKEN
from intent_engine import detectar_intencao
from response_builder import build_response
from messaging_client import send_message, get_user_name  # <-- Adicionei get_user_name aqui
from database import save_interaction
from logger import log

app = Flask(__name__)

@app.route("/webhook", methods=['GET'])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        log("API", "Webhook validado com sucesso pela Meta! ✅")
        return challenge, 200
    
    log("ERROR", "Tentativa de validação com Token inválido.")
    return "Token Inválido", 403

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.get_json()

    if data.get("object") == "page":
        for entry in data.get("entry", []):
            for event in entry.get("messaging", []):
                sender_id = event["sender"]["id"]
                message_text = event.get("message", {}).get("text", "")

                if message_text:
                    log("EVENT", f"Nova mensagem de: {sender_id}")
                    
                    # 1. Busca o nome real do usuário na Meta
                    # Se o Token estiver errado, ele retornará "Cliente" por padrão
                    nome_real = get_user_name(sender_id)
                    
                    # 2. Identifica a intenção
                    intent = detectar_intencao(message_text)
                    log("INTENT", f"Detectado: {intent} para o usuário: {nome_real}")

                    # 3. Constrói a resposta usando o nome real
                    response_text = build_response(intent, user_name=nome_real)
                    
                    # 4. Ações de Saída
                    send_message(sender_id, response_text)
                    save_interaction(sender_id, intent, response_text)
                    
                    log("BOT", f"Resposta enviada para {nome_real}. Fluxo concluído.")

        return "EVENT_RECEIVED", 200
    return "Not Found", 404

if __name__ == "__main__":
    log("API", "Servidor API iniciado em http://localhost:5000")
    app.run(port=5000, debug=True)