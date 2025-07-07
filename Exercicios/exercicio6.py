# Lista com dicionarios dentro
lista = [
     {'nome': 'Leonardo', 'sobrenome': 'Oliveira','idade':'31'},
     {'nome': 'Mariana', 'sobrenome': 'Oliveira','idade':'36'},
     {'nome': 'Daniel', 'sobrenome': 'Silva','idade':'27'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira','idade':'25'},
     {'nome': 'Aline', 'sobrenome': 'Souza','idade':'34'},
]
# Função para exibir a lista
def exibir(item):
    for contador in item:
        print(contador)
    print()

# Ultilizando função lambda
l1 = sorted(lista, key=lambda item: item['idade'],reverse=True)
l2 = sorted(lista, key=lambda item: item['nome'])

exibir(l1)
exibir(l2)
