import csv

from modules.get_usuario import get_usuario

def ListarContas():

    cpf = input("Digite o CPF do usuário (somente números): ")
    try:
        usuario = get_usuario(cpf)
        for conta in usuario.contas:
            print(f"Número da conta: {conta.numero}, Saldo: R$ {conta.saldo:.2f}")
    except ValueError:
        print("Usuário não encontrado")