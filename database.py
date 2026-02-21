import sqlite3
import csv
from datetime import datetime
from logger import log

DB_NAME = "bot.db"

def init_db():
    """Cria a tabela se ela ainda não existir"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                user_id TEXT,
                user_name TEXT,
                comment TEXT,
                intent TEXT,
                response TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        log("ERROR", f"Falha ao inicializar banco: {e}")

def save_interaction(user_id, intent, response, user_name="Cliente", comment=""):
    try:
        # Agora sim a função existe e pode ser chamada!
        init_db() 
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        timestamp = datetime.now().isoformat()
        
        cursor.execute('''
            INSERT INTO interactions (timestamp, user_id, user_name, comment, intent, response)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (timestamp, user_id, user_name, comment, intent, response))
        
        conn.commit()
        conn.close()
        log("DATABASE", f"Registro salvo para {user_name} 💾")
    except Exception as e:
        log("ERROR", f"Erro ao gravar no SQLite: {e}")

def export_to_csv():
    """Gera o relatório CSV apenas quando você rodar este comando"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM interactions")
        rows = cursor.fetchall()
        
        column_names = [description[0] for description in cursor.description]
        
        filename = f"relatorio_vendas_{datetime.now().strftime('%d_%m_%H%M')}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(column_names)
            writer.writerows(rows)
            
        conn.close()
        log("DATABASE", f"Relatório gerado: {filename} 📊")
        return filename
    except Exception as e:
        log("ERROR", f"Erro ao exportar CSV: {e}")


def export_to_html():
    """Gera um relatório visual em HTML que abre no navegador"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM interactions ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        
        filename = f"relatorio_vendas_{datetime.now().strftime('%d_%m_%H%M')}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"""
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Relatório do Bot</title>
                <style>
                    body {{ font-family: sans-serif; margin: 40px; background: #f4f7f6; }}
                    table {{ border-collapse: collapse; width: 100%; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
                    th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; }}
                    th {{ background-color: #007bff; color: white; text-transform: uppercase; font-size: 14px; }}
                    tr:hover {{ background-color: #f1f1f1; }}
                    .intent-badge {{ background: #e1f5fe; color: #01579b; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; }}
                </style>
            </head>
            <body>
                <h2>📊 Relatório de Interações do Bot</h2>
                <p>Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                <table>
                    <tr> {''.join(f'<th>{col}</th>' for col in column_names)} </tr>
                    {''.join(f'<tr>{" ".join(f"<td>{str(val)}</td>" for val in row)}</tr>' for row in rows)}
                </table>
            </body>
            </html>
            """)
            
        conn.close()
        log("DATABASE", f"Relatório HTML gerado: {filename} 🌐")
        return filename
    except Exception as e:
        log("ERROR", f"Erro ao exportar HTML: {e}")