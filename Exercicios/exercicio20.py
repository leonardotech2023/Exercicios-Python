# Lista com as vendas de produtos realizadas em diferentes lojas.
'''
Desafio

Sem usar max():

Calcule o valor total das vendas.
Crie um dicionário aninhado onde:
A chave principal seja a loja.
Dentro de cada loja existam:
total_vendas
quantidade_vendas
Descubra qual loja teve o maior faturamento.
Exiba todas as informações.
'''
total_vendas = 0

vendas = [
    {'loja': 'Centro', 'produto': 'Notebook', 'valor': 3500},
    {'loja': 'Centro', 'produto': 'Mouse', 'valor': 80},
    {'loja': 'Shopping', 'produto': 'Notebook', 'valor': 4200},
    {'loja': 'Centro', 'produto': 'Monitor', 'valor': 1200},
    {'loja': 'Shopping', 'produto': 'Teclado', 'valor': 150},
    {'loja': 'Bairro', 'produto': 'Mouse', 'valor': 70},
    {'loja': 'Shopping', 'produto': 'Monitor', 'valor': 1100},
    {'loja': 'Bairro', 'produto': 'Notebook', 'valor': 3000},
]
relatorio = dict()
nome_loja = ''
maior_faturamento = tuple()
maior = 0

for venda in vendas:

    total_vendas += venda['valor']
    nome_loja = venda['loja']

    if nome_loja not in relatorio:
        relatorio[nome_loja] = {'total_vendas': venda['valor']}
        relatorio[nome_loja]['quantidade_vendas'] = 1

    else:
        relatorio[nome_loja]['total_vendas'] += venda['valor']
        relatorio[nome_loja]['quantidade_vendas'] += 1

for chave, valor  in relatorio.items():

    if maior < valor['total_vendas']:
        maior = valor['total_vendas']
        maior_faturamento = (chave, valor['total_vendas'])

print(f'Total das vendas: {total_vendas}')
for chave, valor in relatorio.items():
    print(chave, valor)

print(f'Maior Faturamento foi {maior_faturamento}')