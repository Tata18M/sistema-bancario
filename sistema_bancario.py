""""Desafio 1

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operacoes e para isso
escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operacoes: depósito, saque e extrato."""


nome = input("Digite seu nome:")
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[f] Saldo
[q] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


# Boas vindas ao Next_Bank 
print(f"""
Olá {nome}, bem-vindo!

Por gentileza, digite sua operação:""")


# Código referente a operação desejada
while True:
    opcao = input(menu)


# Operação com depósito
    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

# Operação com Saque   
    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação negada! Saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operação negada! O valor de saque excede o limite.")

        elif excedeu_saques:
            print("Operação negada! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")


# Operação com Extrato
    elif opcao == "e":
        print("\n================= EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=============================================")


# Operação para visualizar apenas o saldo
    elif opcao == "f":
        print(f"Seu saldo é de R$ {saldo:.2f}")


# Operação para sair da conta
    elif opcao == "q":
        print("Next_Bank agradece, até a próxima!")
    break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")

