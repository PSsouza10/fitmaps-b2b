import os

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            caminho = os.path.join(root, file)
            try:
                with open(caminho, 'rb') as f:
                    data = f.read()
                if b'\x00' in data:
                    print(f"Limpando arquivo: {caminho}")
                    nova_data = data.replace(b'\x00', b'')
                    with open(caminho, 'wb') as f:
                        f.write(nova_data)
            except Exception as e:
                print(f"Erro ao processar {caminho}: {e}")

print("Limpeza finalizada.")
