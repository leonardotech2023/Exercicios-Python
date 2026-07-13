alunos = [['Leonardo','8','9'],['Mariana', '7', '5'],['Rafael', '3','5']]


for aluno in alunos:
    # Convertendo as notas para o tipo float
    aluno[1:] = map(float, aluno[1:])
    # Somando as notas e dividindo para criar a media
    media = sum(aluno[1:]) / len(aluno[1:])
    aluno.append(media)
    print(aluno)