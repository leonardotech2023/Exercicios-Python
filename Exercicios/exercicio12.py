loja = [{'nome': 'Teclado',             'categoria': 'Informatica', 'preco': 29.90},
        {'nome': 'Monitor',             'categoria': 'Informatica', 'preco': 300},
        {'nome': 'O Senhor dos aneis',  'categoria': 'Livros',      'preco': 59.90},
        {'nome': 'Mouse',               'categoria': 'Informatica', 'preco': 22.90},
        {'nome': 'Moto Edge',           'categoria': 'Celulares',   'preco': 1998},
        {'nome': 'Python',              'categoria': 'Livros',      'preco': 30.00},
        {'nome': 'Notebook',            'categoria': 'Informatica', 'preco': 4000},
        {'nome': 'Pai Rico Pai Pobre',  'categoria': 'Livros',      'preco': 60.00},
        {'nome': 'Moto G 86',           'categoria': 'Celulares',   'preco': 990},
        {'nome': 'Samsung S24',         'categoria': 'Celulares',   'preco': 3000}]

# Funcao que cria uma lista de produtos abaixo de 100 reais usando lambda
def produtos():
    produtos_menos_de_cem_reais = list(filter(lambda nome: nome['preco'] <= 100, loja))
    return produtos_menos_de_cem_reais


resultado = produtos()


print(*resultado, sep='\n')