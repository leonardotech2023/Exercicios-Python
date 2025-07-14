# Lista Alunos
alunos = [
    {'nome':'Mariana','media':7.5},
    {'nome':'Pedro','media':8},
    {'nome':'Rafael','media':6.5},
    {'nome':'Leonardo','media':9},
    {'nome':'Joao','media':4.5}
]
# Criando uma list comprehension com os alunos que tiraram nota maior que 7
novos_alunos = [{**aluno} for aluno in alunos if aluno['media'] > 7]

# Ordenando a nova lista com a funcao lambda, do maior para o menor da posicao media
novos_alunos.sort(key=lambda item: item['media'], reverse=True)
print(*novos_alunos,sep='\n')