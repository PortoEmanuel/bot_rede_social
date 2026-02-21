from database import export_to_csv, export_to_html
if __name__ == "__main__":
    print("📂 Acessando banco de dados...")
    arquivo = export_to_csv(), export_to_html()
    if arquivo:
        print(f"✨ Sucesso! O arquivo '{arquivo}' foi criado na sua pasta.")
    else:
        print("❌ Ops, algo deu errado ao gerar o arquivo.")


        
