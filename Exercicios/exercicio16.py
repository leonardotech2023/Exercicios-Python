'''
Escreva um programa em Python para criar um novo dicionário contendo apenas os pares chave-valor de um dicionário existente, 
onde o valor atenda a uma condição específica.
manter apenas as pontuações maiores que60
'''
scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}

pontuacao = [valor for valor in scores.items() if valor[1] > 60]
pontuacao.sort(key=lambda nome: nome[1], reverse=True)

pontuacao = dict(pontuacao)

for nome in pontuacao.items():
    print(nome)