menu = """

Selecione uma opção:

[1] Depósito
[2] Extrato
[3] Saque
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Insira o valor do depósito: "))
        if valor_deposito <= 0:
            print("Operação falhou: não é possível fazer depósito de valores negativos ou iguais a zero.")
        else:
            saldo += valor_deposito
            extrato += f"+ R${valor_deposito:.2f}\n"
            print("Depósito realizado com sucesso!")


    elif opcao == "2":

        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Saldo atual: {saldo}")

    elif opcao == "3":

        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Insira o valor do saque: "))

            if valor_saque > saldo:
                print("Operação falhou: saldo insuficiente.")

            elif valor_saque > 500:
                print("Operação falhou: valor superior ao limíte máximo de R$500 por saque.") 

            else:
                saldo -= valor_saque
                extrato += f"- R${valor_saque:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso")

        else:
            print("Operação falhou: limíte máximo diário de saques alcançado.")


    elif opcao == "4":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")

