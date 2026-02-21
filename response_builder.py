import urllib.parse
from config import WHATSAPP_NUMBER, MSG_WHATSAPP_BASE

def build_response(intent, user_name=None):
    name = user_name or "Olá"
    
    # Criando o link de forma segura
    texto_personalizado = f"Oi! Sou o(a) {name}. {MSG_WHATSAPP_BASE}"
    link_whatsapp = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(texto_personalizado)}"

    respostas = {
        "disponibilidade": f"{name}, sim! Ainda temos em estoque. Posso separar um para você? 👍",
        "preco": f"{name}, os valores variam. Para eu te passar a tabela atualizada, clica aqui: {link_whatsapp}",
        "detalhes": f"{name}, claro! Tenho um PDF com os detalhes. Me chama no Whats que te envio: {link_whatsapp}",
        "compra": f"{name}, excelente! Vamos finalizar seu pedido por aqui para ser mais rápido: {link_whatsapp}",
        "elogio": f"{name}, fico feliz que gostou! 😊 Se precisar de algo, é só chamar.",
        "padrao": f"{name}, obrigado pelo contato! Como posso te ajudar? ✨"
    }

    return respostas.get(intent, respostas["padrao"])