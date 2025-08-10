# Lista de Carros
carros = [{'Marca':'chevrolet','Modelo':'Cruze','Ano':2017,'Preco':51500},
          {'Marca':'volkswagen','Modelo':'Golf','Ano':2017,'Preco':62000},
          {'Marca':'volkswagen','Modelo':'Jetta','Ano':2013,'Preco':49500},
          {'Marca':'chevrolet','Modelo':'Corsa','Ano':2009,'Preco':18000},
          {'Marca':'ford','Modelo':'Fiesta','Ano':2008,'Preco':21400},
          {'Marca':'chevrolet','Modelo':'Prisma','Ano':2010,'Preco':30900},
          {'Marca':'volkswagen','Modelo':'Jetta','Ano':2015,'Preco':55400},
          {'Marca':'ford','Modelo':'Land Rover','Ano':2012,'Preco':90700},
          {'Marca':'chevrolet','Modelo':'Onix','Ano':2019,'Preco':55500},
          {'Marca':'hyundai','Modelo':'HB20','Ano':2014,'Preco':50000},
          {'Marca':'honda','Modelo':'Civic','Ano':2014,'Preco':71000},
]

# Filtrando os carros da marca chevrolet com a função lambda
carros_chevrolet = list(filter(lambda carro: carro['Marca'] == 'chevrolet', carros))

# Ordenando os carros do maior preço para o menor
carros_chevrolet.sort(key=lambda x: x['Preco'],reverse=True)
print(*carros_chevrolet,sep='\n')

print('-'*60)
