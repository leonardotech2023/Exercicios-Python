aprovados = list()
# # Dicionário aninhado contendo os alunos e suas respectivas notas em disciplinas
turma = {
    'Leonardo': {'matematica':8.5, 'portugues':7, 'ciencia':5.5},
    'Joao': {'matematica':5, 'portugues':9, 'ciencia':7.5},
    'Mariana': {'matematica':4, 'portugues':6, 'ciencia':10}
}


def calculando_media():
    # Laço para percorrer no dicionario
    for nome, materia in turma.items():
        # Somando os valores e dividindo pelo tamanho da lista
        media = sum(materia.values()) / len(materia)
        materia['media'] = media

        if materia['media'] >= 7:
            aprovados.append((nome, materia['media']))


calculando_media()

for posicao, valor in aprovados:
    print(f'{posicao} {valor:.2f}')