import requests

# A URL onde seu servidor Flask está rodando
url = "http://localhost:5000/webhook"

# O "pacote" de dados que simula uma mensagem do Facebook
payload = {
    "object": "page",
    "entry": [{
        "messaging": [{
            "sender": {"id": "12345"},
            "message": {"text": "Qual o preço desse item?"} # Pode mudar o texto aqui
        }]
    }]
}

try:
    print("🚀 Enviando teste para o bot...")
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print(f"✅ Sucesso! O servidor respondeu: {response.text}")
    else:
        print(f"❌ Erro! Status: {response.status_code}")
        print(f"Detalhes: {response.text}")

except Exception as e:
    print(f"🚨 Erro de conexão: {e}")