# Lista dos alunos, com nome, idade e media
alunos = [{'nome':'Leonardo','idade':18,'media':7.5},{'nome':'Mariana','idade':23,'media':8},
          {'nome':'Joao','idade':22,'media':4},{'nome':'Luiz','idade':28,'media':5.5},
          {'nome':'Ana','idade':37,'media':8.5},{'nome':'Pamela','idade':40,'media':3},]
alunos_reprovados = list()
print('\t\t\033[1;36mLista de Alunos\033[m')

# Função que percorre a lista e adiciona o alunos com media a baixo de 5
# em uma lista de reprovados.
def funcao_alunos(item):
    for contador in item:
        if contador['media'] < 5:
            alunos_reprovados.append(contador)

funcao_alunos(alunos)
for contador in alunos:
    print(contador)

print('-='*25)

print(f'\t\t\033[1;31mAlunos reprovados:\033[m')
for cont in alunos_reprovados:
    print(cont)