def build_response(intent, user_name=None):

    name = user_name or "Olá"

    if intent == "availability":
        return f"{name}, sim! Ainda está disponível 👍"

    if intent == "pricing":
        return f"{name}, vou te passar os valores 😉"

    if intent == "details":
        return f"{name}, deixa eu te explicar melhor 👇"

    if intent == "purchase":
        return f"{name}, perfeito! Vou te chamar no privado 💬"

    if intent == "compliment":
        return f"{name}, fico muito feliz que gostou 😊"

    return f"{name}, obrigado pelo contato ✨"
