'''
Crie um novo dicionário onde:
Produtos com preço maior ou igual a R$1000 recebem 15% de desconto.
Produtos com preço entre R$300 e R$999 recebem 5% de desconto.
Produtos abaixo de R$300 não aparecem no novo dicionário.
'''
produtos = {
    'Notebook': 3500,
    'Mouse': 80,
    'Monitor': 1200,
    'Teclado': 150,
    'Headset': 350,
    'Webcam': 450,
    'Impressora': 900
}

# dictionary comprehension
desconto = {chave: valor - ((valor * 15) / 100) if valor >= 1000 else( valor - ( valor * 5) / 100) for chave, valor in produtos.items() if valor >= 300}

print(desconto)