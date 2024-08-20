# Lista de Carros com nome, ano e preço
carros = [['Gol',2009,20000],['Civic',2010,30000],
          ['Prisma',2015,29000],['Corola',2014,35000],['HB20',2018,32500],]

carros_novos = list()

# For tradiconal filtrando os carros acima de 2010 e com valor maior de 30000
for contador in carros:
    if contador[1] > 2010 and contador[2] > 30000:
        carros_novos.append(contador)

# Lista Comprehensions filtrando os carros acima de 2010 e com valor maior de 30000

carros_novos2 = [x for x in carros_novos if x[1] > 2010 and x[2] > 30000]
print()

print('Lista Completa')
for contador in carros:
    print(contador)

print('-='*15)

# Lista pronta dos carros mais novos
for contador in carros_novos2:
    print(contador)
