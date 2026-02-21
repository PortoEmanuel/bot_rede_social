# 🤖 Bot de Atendimento Automático - Redes Sociais

Este é um bot de atendimento integrado com a API da Meta (Facebook/Messenger), capaz de identificar intenções de usuários, responder automaticamente e gerar relatórios de interações.

## 🚀 Funcionalidades
- **Webhook Flask**: Pronto para receber eventos em tempo real da Meta.
- **Motor de Intenções**: Classifica mensagens em categorias como `preco`, `disponibilidade` e `elogio`.
- **Relatórios Inteligentes**: Gera relatórios sob demanda em formatos **CSV** (dados) e **HTML** (visual/dashboard).
- **Banco de Dados**: Armazenamento local leve utilizando SQLite3.

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.11+
- **Framework**: Flask
- **Banco de Dados**: SQLite3
- **Integração**: Meta Graph API

## 📋 Como Configurar
1. Clone o repositório.
2. Crie um ambiente virtual: `python3 -m venv .venv`
3. Ative o ambiente e instale as dependências: `pip install -r requirements.txt`
4. Renomeie o seu arquivo de configuração ou crie o `config.py` com seus tokens.

## 📊 Geração de Relatórios e Testes
Para  testar e extrair os dados das interações, utilize:
```bash
python3 test_api.py
python3 gerar_relatorio.py



