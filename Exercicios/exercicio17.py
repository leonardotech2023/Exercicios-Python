'''
Sem usar max() para encontrar o maior vendedor, faça um programa que:

Calcule o valor total das vendas.
Crie um dicionário com o total vendido por cada vendedor.
Descubra qual vendedor vendeu mais (usando um for).
Mostre o valor vendido pelo vendedor que mais faturou.
'''

# lista com as vendas realizadas por diferentes vendedores ao longo do ano.
vendas = [
    {'vendedor': 'Ana', 'produto': 'Notebook', 'valor': 3500},
    {'vendedor': 'Carlos', 'produto': 'Mouse', 'valor': 80},
    {'vendedor': 'Ana', 'produto': 'Monitor', 'valor': 1200},
    {'vendedor': 'João', 'produto': 'Teclado', 'valor': 150},
    {'vendedor': 'Carlos', 'produto': 'Notebook', 'valor': 4000},
    {'vendedor': 'João', 'produto': 'Cadeira Gamer', 'valor': 900},
    {'vendedor': 'Ana', 'produto': 'Headset', 'valor': 350},
    {'vendedor': 'Carlos', 'produto': 'Webcam', 'valor': 450},
]

total_vendas = 0
vendedores = dict()
vendedor_mais_vendeu = dict()

# Laço para percorrer na lista
for valor in vendas:
    total_vendas += valor['valor']

    nome_pessoa = valor['vendedor']

    if nome_pessoa not in vendedores:
        vendedores[nome_pessoa] = valor['valor']
    else:
        vendedores[nome_pessoa] += valor['valor']

maior_valor = 0

for nome, valor in vendedores.items():

    if maior_valor == 0:
        maior_valor = valor
        vendedor_mais_vendeu = (nome, valor)
        
    else:
        if maior_valor < valor:
            maior_valor = valor

            vendedor_mais_vendeu = (nome, valor)

    print(nome,valor)
print()
print(f'Total de vendas {total_vendas:.2f}')
print(f'Vendedor que mais vendeu foi {vendedor_mais_vendeu}')