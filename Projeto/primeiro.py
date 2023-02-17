import textwrap

def menu():
    menu = """\n
    ======================= MENU =======================
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NV]\tNova Conta
    [LC]\tListar Contas
    [NU]\tNovo Usuário
    [Q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$: {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso! ===")
    else:
        print("\n@@@ Operacao falhou! O valor informado e invalido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("\n@@@ Operacao falhou! Voce nao tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operacao falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operacao falhou! Numero maximo de saques excedidos. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$: {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso ===")
    else:
        print("\n@@@ Operacao falhou! O valor informado e invalido. @@@")
    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato): 
    print("\n======================= EXTRATO =======================")
    print("Nao foram realizadas movimentacoes." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\n@@@ Ja existe usuario com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe endereco (Logradouro, numero - bairro - cidade/siglaestado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuario criado com sucesso ===")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuario nao encontrado, fluxo de criacao de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
    
        if opcao == "D":
            valor = float(input("Quanto deseja depositar: "))
            saldo , extrato = depositar(saldo,valor,extrato)         
                
        elif opcao == "S":
            valor = float(input("Digite o valor que deseja sacar: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
                
        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "NU":
            criar_usuario(usuarios)
        
        elif opcao == "NV":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "Q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()
