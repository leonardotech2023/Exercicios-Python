# Introdução a Matrizes
from random import randint
# Criando uma matriz com valores 0
matriz_a = [[0,0,0],[0,0,0],[0,0,0]]

# Colocando valores aleatorio na Matriz A
for linha in range(0,3):
    for coluna in range(0,3):
        matriz_a[linha][coluna] = randint(10,50)
# Criando Matriz B
matriz_b = [[0,0,0],[0,0,0],[0,0,0]]
# For na Matriz A e adcionando o valor dobrado da Matriz A na Matriz B
for a in range(0,3):
    for b in range(0,3):
        matriz_b[a][b] = matriz_a[a][b] * 2

print()
# Mostrando os valores da Matriz A
print('\033[1;32mMatriz A\033[m')
for linha in range(0,3):
    for coluna in range(0,3):
        print(matriz_a[linha][coluna], end=' ')
    print()
print()

# Mostrando os valores da Matriz B
print('\033[1;36mMatriz B \033[m')
for linha in range(0,3):
    for coluna in range(0,3):
        print(matriz_b[linha][coluna], end=' ')
    print()
# O programa fez duas matriz A e B sendo o dobro da A