saldo = 1000

# Menu do caixa eletronico

while True:
    print("""Caixa Eletronico
      1 - Verificar Saldo
      2 - Depositar Dinheiro
      3 - Sacar Dinheiro
      4 - Sair'""")
    escolha = int(input('Escolha uma opção (1-4): '))
    if escolha == 1:
        print(f'\033[1;4;32mSeu saldo é R$: {saldo:.2f}\033[m')

    elif escolha == 2:
        valor = float(input('Digite o valor do deposito R$: '))
        saldo += valor
        print(f'\033[1;4;32mDeposito de R$ {valor} realizado com sucesso!\033[m')

    elif escolha == 3:
        valor = float(input('Digite o valor do saque R$: '))
        if valor > saldo:
            print('\033[1;4;31mValor de Saldo invalido ou saldo insuficiente.\033[m')

        else:
            saldo -= valor
            print(f'\033[1;4;31mSaque de R$ {valor} realizado com sucesso!\033[m')

    if escolha == 4:
        break
