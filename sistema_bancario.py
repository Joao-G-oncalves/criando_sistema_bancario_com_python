menu = '''
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
=>>>  '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower().strip()[0]

    if opcao == 'd':
        deposito = float(input('Quando você deseja depositar? R$ '))
        if deposito > 0:
            saldo += deposito
            print(f'Você depositou R$ {deposito:.2f}')
            extrato += f' + Depósito realizado de R$ {deposito:.2f}\n'
        else:
            print("Não foi possível realizar esse depósito, tente novamente mais tarde!")


    elif opcao == 's':

        if LIMITE_SAQUES > 0:
            saque = float(input('Qual o valor deseja sacar? R$ '))

            if saque <= 0:
                print('Valor inválido, tente novamente mais tarde!')

            elif saque <= 500 and saque <= saldo:
                LIMITE_SAQUES -= 1
                saldo -= saque
                print(f'Você sacou R$ {saque:.2f}')
                extrato += f' - Saque realizado de    R$ {saque:.2f}\n'

            elif saque > saldo:
                print('Você não tem saldo disponível, consulte seu extrato!')



            else:
                print('Seu limite de saque é de R$ 500,00 por operação')

        else:
            print('Você excedeu o seu limite diário de 3 saques. Tente novamente amanhã!')


    elif opcao == 'e':
        print('''=============== EXTRATO ===============''')
        if extrato in '':
            print(f'Não foram realizadas movimentações.\nSaldo: R$ {saldo:.2f}')
        else:
            print(extrato + f'   Seu saldo atual:      R$ {saldo:.2f}')
        print('''=======================================''')
    elif opcao == 'q':
        print('Muito obrigado pelo acesso, até a próxima!')
        break

    else:
        print('Operação inválida! Por favor selecione uma opção novamente')
