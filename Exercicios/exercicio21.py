# Uma empresa possui vários departamentos. Cada produto pertence a um departamento e possui uma quantidade em estoque.
'''
Sem usar max():

1. Crie um dicionário aninhado onde:
A chave principal seja o departamento.
Dentro de cada departamento, as chaves sejam os produtos.
O valor de cada produto seja sua quantidade.
2. Exiba o dicionário completo.
3. Percorra o dicionário e mostre todos os departamentos e seus produtos.
'''
estoque = [
    {'departamento': 'Informática',      'produto': 'Notebook',    'quantidade': 15},
    {'departamento': 'Informática',      'produto': 'Mouse',       'quantidade': 40},
    {'departamento': 'Móveis',           'produto': 'Mesa',        'quantidade': 12},
    {'departamento': 'Informática',      'produto': 'Monitor',     'quantidade': 18},
    {'departamento': 'Móveis',           'produto': 'Cadeira',     'quantidade': 25},
    {'departamento': 'Eletrodomésticos', 'produto': 'Geladeira',   'quantidade': 8},
    {'departamento': 'Eletrodomésticos', 'produto': 'Micro-ondas', 'quantidade': 14},
    {'departamento': 'Móveis',           'produto': 'Armário',     'quantidade': 10},
]

relatorio = dict()
nome_departamento = ''
produto = ''
quantidade = 0

for nome in estoque:

    nome_departamento = nome['departamento']
    produto = nome['produto']
    quantidade = nome['quantidade']


    if nome_departamento not in relatorio:
        relatorio[nome_departamento] = {produto: nome['quantidade']}

    else:
        relatorio[nome_departamento][produto] = nome['quantidade']

print(relatorio)
print()

for departamento, produtos in relatorio.items():
    print(departamento)
    
    for produto, quantidade in produtos.items():

        print(produto, quantidade)
    print('-'*10)