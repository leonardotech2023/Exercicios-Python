from time import sleep
from os import system

jogadores = dict()
gols_lista = list()
time = list()

# Funcao para imprimir uma linha colorida
def linha():
    print('\033[1;34m=-\033[m'*30)


def funcao_jogadores():

    while True:
        jogadores['nome'] = input('Nome do Jogador: ').title()
        partida = int(input(f'Quantas partidas {jogadores["nome"]} jogou: '))

        for contador in range(1, partida + 1):
            gols = int(input(f'Quantos Gols na Partida {contador}: '))
            gols_lista.append(gols)

        jogadores['gols'] = gols_lista.copy()
        jogadores['total'] = sum(gols_lista)

        linha()

        time.append(jogadores.copy())
        gols_lista.clear()

        continuar = str(input('Quer Continuar [S/N]: ')).lower()[0]

    # os.system limpa a tela para digitar o proximo jogador
        system('clear')
        if continuar == 'n':
            break
    print()

    linha()

    # Jogador que fez mais gols 
    print('\t-- ARTILHEIRO DO CAMPEONATO --')

    # Esta funcao lambda tras o jogador que fez mais gols
    artilheiro = max(time, key=lambda jogador: jogador['total'])
    print(artilheiro)

    linha()
    print(f'{"cod nome":<25} {"gols":<20} {"total":<15}')
    for chave, valor in enumerate(time):
        print(f'{chave:<3} {valor["nome"]:<20} {str(valor["gols"]):<22} {valor["total"]}')
    
funcao_jogadores()

while True:

    try:
        opcao = int(input('Mostrar dados de qual jogador? (999 para parar): '))

        if  opcao == 999:
            sleep(1)
            print('Saindo...')
            break
        elif opcao != 999:         
    
            print(f' -- LEVANTAMENTO DO JOGADOR: {time[opcao]["nome"]}')
            for jogo, gol in enumerate(time[opcao]['gols']):
                sleep(1)
                print(f'\tNo jogo {jogo} fez {gol} gols.')
            
            linha()

    except (IndexError,ValueError):
        print('\033[1;31mVALOR INVALIDO, TENTE NOVAMENTE!\033[m')
