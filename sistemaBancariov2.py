def menu():
    menu = """
    ======= MENU =======
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [7] Sair

    Digite sua opção:
    """
    return int(input(menu))


def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("Depósito realizado com Sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato


def sacar(*,saldo,valor,extrato,limite,numeroSaques,limiteSaques):
    if valor <= saldo:
        if numeroSaques < limiteSaques:
            if valor <= limite:
                if valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R${valor:.2f}\n"
                    numeroSaques += 1
                    print("Saque realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado é inválido.")
            else:
                print("Operação falhou! O valor do saque excede o limite.")
        else:
            print("Operação falhou! Excedido limite de saque.")    
    else:
        print("Operação falhou! Você não tem saldo suficiente.")

    return saldo,extrato


def exibirExtrato(saldo,/,*,extrato):
    print("==========EXTRATO==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("===========================")


def criarUsuarios(usuarios):
    cpf = input("Informe o cpf (apenas números) ")
    usuario = filtrarUsuario(cpf,usuarios)

    if usuario:
        print("Já existe um usuario com esse cpf")
        return
    
    nome = input("Informe o nome completo: ")
    dataNascimento = input("Informa a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "dataNascimento": dataNascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com SUCESSO!")


def filtrarUsuario(cpf,usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None   


def criarConta(agencia,numeroConta,usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrarUsuario(cpf,usuarios)

    if usuario:
        print("Conta criada com SUCESSO")
        return {"agencia": agencia, "numeroConta": numeroConta,"usuario": usuario}
    
    print("Usuario não encontrado, fluxo de criação de conta encerrado!")



def listarContas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta["agencia"]}
        C/C: {conta["numeroConta"]}
        Titular: {conta["usuario"]["nome"]}
        """
    print(linha)



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numeroSaques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            saldo,extrato = depositar(saldo,valor,extrato)
        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))

            saldo,extrato = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numeroSaques=numeroSaques,limiteSaques=LIMITE_SAQUES)
        elif opcao == 3:
            exibirExtrato(saldo,extrato=extrato)
        elif opcao == 4:
            numeroConta = len(contas) + 1
            conta = criarConta(AGENCIA,numeroConta,usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 5:
            listarContas(contas)
        elif opcao == 6:
            criarUsuarios(usuarios)
        elif opcao == 7:
            break
        else:
            print("Operação inválida, por favor selecione novamente!! ")

main()