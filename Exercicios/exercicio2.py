import random

#Lista com nomes de ruas
rua = ['RUA SAO PEDRO','RUA QUINZE','RUA SAO JOAO','RUA SAO FRANCISCO',
        'RUA SETE DE SETEMBRO','RUA 4','RUA DEZESSEIS','RUA SAO SEBASTIAO',
        'RUA PARANA','RUA BELA VISTA','RUA SANTA LUZIA','RUA SAO JORGE',
        'RUA DEZENOVE','RUA CASTRO ALVES','RUA DUQUE DE CAXIAS','RUA PROJETADA',
        'RUA RUI BARBOSA']

#Lista com nomes de bairros
bairro = ['Centro','Florida','Jardim Niceia','Vila Dutra','Estoril','Joinvilhe',
          'Ibirapuera','Capão Redondo','Liberdade']

#Lista com nomes de paises
pais = ['Brasil','Argentina','Uruguai','Chile','Estados Unidos',
        'Canada','França','Mexico','Japão','China','Israel'
        ]

lista_temporaria = list()
lista = list()


#Função que gera as listas
def gerador():
    chave = 1
    for contador in range(1,1000+1):
        valor1 = random.choice(rua).upper()
        valor3 = random.choice(bairro).upper()
        valor2 = random.choice(pais).upper()
        
        lista_temporaria.append(valor1[:])
        lista_temporaria.append(valor3[:])
        lista_temporaria.append(valor2[:])
        
        lista_temporaria.append(chave)
        chave = chave + 1
        lista.append(lista_temporaria[:])
        lista_temporaria.clear()

    return lista

#Chamando a função
gerador()

#Imprimindo a lista pronta
for cont in lista:
    print(cont)