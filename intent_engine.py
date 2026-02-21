def detectar_intencao(texto):
    texto = texto.lower()

    
    if any(palavra in texto for palavra in ["dispon", "tem", "estoque"]):
        return "disponibilidade"

    if any(palavra in texto for palavra in ["preço", "valor", "quanto", "cust"]):
        return "preco"

    if any(palavra in texto for palavra in ["detalhe", "info", "explica", "saiba"]):
        return "detalhes"

    if any(palavra in texto for palavra in ["comprar", "quero", "pedido", "pagar"]):
        return "compra"

    if any(palavra in texto for palavra in ["top", "legal", "gostei", "show", "amei"]):
        return "elogio"

    return "padrao"