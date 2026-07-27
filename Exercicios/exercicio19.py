'''
Sem usar max():

1. Calcule a soma de todas as notas.
2. Crie um dicionário com a soma das notas de cada aluno.
3. Crie outro dicionário com a quantidade de provas de cada aluno.
4. Calcule a média de cada aluno.
5. Descubra qual aluno teve a maior média.
6. Exiba:

A soma de todas as notas.
A média de cada aluno.
O aluno com a maior média.
'''

notas = [
    {'aluno': 'Ana', 'nota': 8},
    {'aluno': 'Carlos', 'nota': 7},
    {'aluno': 'Ana', 'nota': 9},
    {'aluno': 'João', 'nota': 6},
    {'aluno': 'Carlos', 'nota': 10},
    {'aluno': 'João', 'nota': 8},
    {'aluno': 'Ana', 'nota': 7},
]
soma_nota = 0
soma_notas_cada_aluno = dict()
nome_cada_aluno = ''
quantidade_provas_cada_aluno = dict()
media_aluno = dict()
maior_media_valor = 0
maior_media = tuple()


for nota in notas:

    soma_nota += nota['nota']

    nome_cada_aluno = nota['aluno']

    # se o nome do aluno nao estiver no dicionario ele adiciona o nome e a nota
    if nome_cada_aluno not in soma_notas_cada_aluno:
        soma_notas_cada_aluno[nome_cada_aluno] = nota['nota']
        quantidade_provas_cada_aluno[nome_cada_aluno] = 1

    else:
        # se o nome do ja estiver no dicionario ele soma as notas dele
        soma_notas_cada_aluno[nome_cada_aluno] += nota['nota']

        quantidade_provas_cada_aluno[nome_cada_aluno] += 1

for aluno in soma_notas_cada_aluno:
    # Calculando a media de cada aluno
    media_aluno[aluno] = soma_notas_cada_aluno[aluno] / quantidade_provas_cada_aluno[aluno]

for chave, valor in media_aluno.items():
    # Verificando qual aluno tem a maior media
    if maior_media_valor == 0:
        maior_media_valor = valor
        maior_media = (chave, valor)

    else:

        if maior_media_valor < valor:
            maior_media_valor = valor
            maior_media = (chave, valor)


print(f'Soma das notas {soma_nota}')
print(f'Soma das notas de cada aluno: {soma_notas_cada_aluno}')
print(f'Quantidade de prova de cada aluno {quantidade_provas_cada_aluno}')

for nome, media in media_aluno.items():
    print(f'{nome} {media:.1f}')
print(f'Maior media {maior_media}')