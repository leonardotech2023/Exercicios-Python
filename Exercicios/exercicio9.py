alunos = [['maria', 8],['Joao',4],['Carlos',6]]

while True:

    for chave, valor in enumerate(alunos):
        print(chave,valor)
    
    escolha = int(input('Qual aluno deseja ver ((999) Sair): '))
    if escolha == 999:
        break
    
    #condicional ternário
    situacao = 'Aprovado' if alunos[escolha][1] >= 7 else 'Recuperacao' if alunos[escolha][1] > 5 and alunos[escolha][1] < 7 else 'Reprovado'

    print(f'\033[1;35mNome: {alunos[escolha][0]} Situação: {situacao} Media {alunos[escolha][1]}\033[m')
