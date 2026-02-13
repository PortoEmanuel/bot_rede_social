from logger import log
from intent_engine import detectar_intencao
from response_builder import build_response
from messaging_client import send_message
from database import init_db, save_interaction


def process_comment(event):

    log("EVENT", "Novo comentário recebido")

    comment_text = event["text"]
    user_id = event["user_id"]
    user_name = event.get("user_name")

    log("DATA", f"Texto: {comment_text}")
    log("DATA", f"Usuário: {user_name} ({user_id})")

    intent = detectar_intencao(comment_text)
    log("INTENT", f"Intenção detectada: {intent}")

    response = build_response(intent, user_name)
    log("RESPONSE", f"Mensagem construída: {response}")

    send_message(user_id, response)

    save_interaction(event, intent, response)


if __name__ == "__main__":

    init_db()

    test_events = [

        {"text": "Esse item ainda está disponível?", "user_id": "1", "user_name": "Ana"},
        {"text": "Qual o preço?", "user_id": "2", "user_name": "Carlos"},
        {"text": "Me passa mais detalhes", "user_id": "3", "user_name": "João"},
        {"text": "Quero comprar", "user_id": "4", "user_name": "Marina"},
        {"text": "Muito top isso", "user_id": "5", "user_name": "Pedro"},
        {"text": "Oi", "user_id": "6", "user_name": "Lucas"},
    ]

    for event in test_events:
        process_comment(event)
