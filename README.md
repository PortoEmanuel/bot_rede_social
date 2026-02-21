# 🤖 Bot de Atendimento Automático - Redes Sociais

Este é um bot de atendimento integrado com a API da Meta (Facebook/Messenger), capaz de identificar intenções de usuários, responder automaticamente e gerar relatórios de interações.

## 🚀 Funcionalidades
- **Webhook Flask**: Pronto para receber eventos em tempo real da Meta.
- **Motor de Intenções**: Classifica mensagens em categorias como `preco`, `disponibilidade` e `elogio`.
- **Relatórios Inteligentes**: Gera relatórios sob demanda em formatos **CSV** (dados) e **HTML** (visual/dashboard).
- **Banco de Dados**: Armazenamento local leve utilizando SQLite3.

## ⚖️ Conformidade com a LGPD
Este projeto foi desenvolvido respeitando os princípios da **Lei Geral de Proteção de Dados**:
- **Finalidade**: Os dados são coletados exclusivamente para fins de atendimento e geração de relatórios de desempenho do bot.
- **Transparência**: O banco de dados armazena apenas `user_id`, `user_name` e o conteúdo das mensagens.
- **Segurança**: Os dados sensíveis e o banco de dados não são compartilhados em repositórios públicos (configurado via `.gitignore`).

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



