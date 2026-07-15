"""
Exercício 1: Padronizador de Nomes de Produtos (Setor de E-commerce): muitas vezes, os nomes dos produtos entram no sistema de qualquer jeito 
(ex: “iPHonE 13″, ” macbook air “). Crie uma função chamada padronizar_texto que receba uma string como parâmetro e 
retorne esse texto sem espaços extras nas extremidades e com todas as palavras com a primeira letra maiúscula 
(formato de título). Teste a função com uma lista de nomes bagunçados.
"""

produtos_baguncados = ['iphone 13', ' MACBOOK PRO', 'aIrPoDs Pro ', 'iPad mini', ' caixa de som bluetooth ' ]


def organizador_de_produtos(produtos):
    produtos_organizados = list()

    for produto in produtos:
        
        produtos_organizados.append(produto.strip().title())

    return produtos_organizados


resultado = organizador_de_produtos(produtos_baguncados)

for nome in resultado:
    print(nome)