import csv

from conta_corrente import ContaCorrente
from get_conta import get_conta
from get_usuario import get_usuario
from usuario import Usuario

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
            print(f"Usuário {nome} criado com sucesso!")
        except ValueError as e:
            print(e)
    elif opcao == "cc":
        cpf = input("Digite o CPF do usuário (somente números): ")
        try:
            ContaCorrente(cpf)
            print(f"Conta corrente criada com sucesso para o usuário {
                  get_usuario(cpf).nome}!")
        except ValueError as e:
            print(e)
    elif opcao == "lu":
        with open('usuarios.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                nome, data_nascimento, cpf, endereco = row
                print(f"Nome: {nome}, Data de Nascimento: {
                      data_nascimento}, CPF: {cpf}, Endereço: {endereco}")
    elif opcao == "lc":
        cpf = input("Digite o CPF do usuário (somente números): ")
        try:
            usuario = get_usuario(cpf)
            for conta in usuario.contas:
                print(f"Número da conta: {
                      conta.numero}, Saldo: R$ {conta.saldo:.2f}")
        except ValueError:
            print("Usuário não encontrado")


    elif opcao == "d":
        numero = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor que você deseja depositar: "))
        try:
            conta = get_conta(numero)
            print(conta.depositar(valor))
        except ValueError:
            print("Conta não encontrada")
    elif opcao == "s":
        numero = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor que você deseja sacar: "))
        try:
            conta = get_conta(numero)
            print(conta.sacar(valor))
        except ValueError:
            print("Conta não encontrada")
    elif opcao == "e":
        numero = int(input("Digite o número da conta: "))
        try:
            conta = get_conta(numero)
            print(conta.extrato())
        except ValueError:
            print("Conta não encontrada")
    elif opcao == "q":
        break
    else:
        print("Operação inválida!")


"""
* TODO: fix: when a user wants to make a deposit (option 'd')
and types in the account number, it goes to the ValueError exception
and returns 'Conta não encontrada'.
"""
