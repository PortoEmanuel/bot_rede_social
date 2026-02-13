def detectar_intencao(texto):
    texto = texto.lower()

    if "dispon" in texto:
        return "disponibilidade"

    if "preço" in texto or "valor" in texto:
        return "preco"

    if "detalhe" in texto or "info" in texto:
        return "detalhes"

    if "comprar" in texto:
        return "compra"

    if "top" in texto or "legal" in texto or "gostei" in texto:
        return "elogio"

    return "padrao"
