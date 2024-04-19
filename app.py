from usuario import Usuario, usuarios
from conta_corrente import ContaCorrente, contas

menu = """
[cu] Criar usuário
[cc] Criar conta corrente
[lu] Listar usuários
[lc] Listar contas de um usuário
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

while True:
    opcao = input(menu).lower()
    if opcao == "cu":
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Digite o CPF (somente números): ")
        endereco = input(
            "Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        try:
            usuario = Usuario(nome, data_nascimento, cpf, endereco)
            usuarios[cpf] = usuario
            print(f"Usuário {nome} criado com sucesso!")
        except ValueError as e:
            print(e)
    elif opcao == "cc":
        cpf = input("Digite o CPF do usuário (somente números): ")
        try:
            ContaCorrente(cpf)
            print(f"Conta corrente criada com sucesso para o usuário {
                  usuarios[cpf].nome}!")
        except ValueError as e:
            print(e)
    elif opcao == "lu":
        for cpf, usuario in usuarios.items():
            print(f"Nome: {usuario.nome}, CPF: {cpf}")
    elif opcao == "lc":
        cpf = input("Digite o CPF do usuário (somente números): ")
        if cpf in usuarios:
            for conta in usuarios[cpf].contas:
                print(f"Número da conta: {
                      conta.numero}, Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Usuário não encontrado")
    elif opcao == "d":
        numero = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor que você deseja depositar: "))
        try:
            print(contas[numero].depositar(valor))
        except KeyError:
            print("Conta não encontrada")
    elif opcao == "s":
        numero = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor que você deseja sacar: "))
        try:
            print(contas[numero].sacar(valor))
        except KeyError:
            print("Conta não encontrada")
    elif opcao == "e":
        numero = int(input("Digite o número da conta: "))
        try:
            print(contas[numero].extrato())
        except KeyError:
            print("Conta não encontrada")
    elif opcao == "q":
        break
    else:
        print("Operação inválida!")
