import textwrap

def menu():
    menu = """\n
    ================ MENU ================

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta Corrente
    [6] Listar Contas
    [7] Sair
    \n=> """

    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

        print("\n!!! Operação realizada com sucesso! !!!")   

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n!!! Operação realizada com sucesso! !!!")   

    else:
        print("Operação falhou! O valor informado é inválido.")    

    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("\n==========================================")

def criar_usuario(usuarios):
    cpf = input("\nInsira seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n !!! Já existe usuário com esse CPF! !!!")

    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Insira seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário criado com sucesso! ===")

def criar_conta_corrente(agencia, usuarios, contas):
    cpf = input("\nInsira o seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    numero_conta = len(contas) + 1

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    else:
        print("\n !!! Usuário não encontrado, processo de criação de conta encerrado! !!! ")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):

    if contas:
        for conta in contas:
            linha = f"""
                Agência: {conta['agencia']}
                C/C: {conta['numero_conta']}
                Titular:{conta['usuario']['nome']}
            """
            print("\n" + "=" * 25)
            print(textwrap.dedent(linha))
            print("=" * 25)
    else:
        print("\n !!! Nenhuma conta registrada !!! ")

def main():

    # DEFAULT

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    # WHILE 

    while True:

        opcao = menu()

        if opcao == "1": #Depósito
            valor = float(input("\nInforme o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":  #Saque
            valor = float(input("\nInforme o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES)

        elif opcao == "3":
            mostrar_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            criar_conta_corrente(AGENCIA, usuarios, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# CHAMADO DA MAIN

main()