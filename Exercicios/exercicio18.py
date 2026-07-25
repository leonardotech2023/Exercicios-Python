'''
Calcular a quantidade total de produtos em estoque.
Criar um dicionário com o total de itens por categoria.
Descobrir qual categoria possui a maior quantidade de itens sem usar max().
Exibir a categoria e a quantidade.
'''

estoque = [
    {'produto': 'Arroz',      'categoria': 'Alimentos', 'quantidade': 20},
    {'produto': 'Feijão',     'categoria': 'Alimentos', 'quantidade': 15},
    {'produto': 'Sabão',      'categoria': 'Limpeza',   'quantidade': 10},
    {'produto': 'Detergente', 'categoria': 'Limpeza',   'quantidade': 25},
    {'produto': 'Macarrão',   'categoria': 'Alimentos', 'quantidade': 30},
    {'produto': 'Shampoo',    'categoria': 'Higiene',   'quantidade': 18},
    {'produto': 'Sabonete',   'categoria': 'Higiene',   'quantidade': 22},
]

quantidade_total = 0
total_items = ''
item_por_categoria = dict()
maior_qtd_de_items = tuple()


for valor in estoque:

    quantidade_total += valor['quantidade']

    total_items = valor['categoria']

    if total_items not in item_por_categoria:
        item_por_categoria[total_items] = valor['quantidade']

    else:
        item_por_categoria[total_items] += valor['quantidade']

quantidade = 0
for chave, valor in item_por_categoria.items():

    if quantidade == 0:
        quantidade = valor
        maior_qtd_de_items = (chave, valor)

    else:
        if quantidade < valor:
            quantidade = valor
            maior_qtd_de_items = (chave, valor)
    print(chave, valor)

print(f'Total de {quantidade_total} produtos.')
print(f'Categoria que possue maior tipo de items {maior_qtd_de_items}')