menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "D":
        print("Depósito")
        deposito = float(input("Quanto deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            print("Valor depositado com sucesso.")
            extrato += f"Depósito de R$:{deposito:.2f} reais\n"
            
        while deposito <= 0:
            print("Operação falhou! O valor informado é inválido insira novamente o valor desejado.")
            deposito = float(input("Quanto deseja depositar: "))

    elif opcao == "S":
        print("Saque")
        print(f"Limite diário de {LIMITE_SAQUES} saques\nApenas R$:500,00 reais liberados por saque.")
        print(f"Saques efetuados: {numero_de_saques}") 
        saque = float(input("Digite o valor que deseja sacar: "))
        
        while saque > limite:
            print("Operação falhou! O valor informado é acima do limite diário digite novamente quanto deseja sacar.")
            saque = float(input("Digite o valor que deseja sacar: "))
            
        while saque <= 0:
            print("Operação falhou! O valor informado é inválido digite novamente um valor válido.")
            saque = float(input("Digite o valor que deseja sacar: "))
            
        if numero_de_saques >= LIMITE_SAQUES:
            print("Limites de saques diário excedido tente novamente amanhã!")
            
        elif saldo <= saque:
            print("Não foi possível realizar o saque, saldo insuficiente.")
            
        elif saldo > saque:
            print("Saque efetuado com sucesso!")
            saldo -= saque
            numero_de_saques += 1
            extrato += f"Saque de R$:{saque:.2f} reais\n"

    elif opcao == "E":
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo Atual R$:{saldo:.2f} reais")
        print("===============================================")

    elif opcao == "Q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
