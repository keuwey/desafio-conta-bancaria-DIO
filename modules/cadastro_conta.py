from business.conta import Conta
from modules.get_usuario import get_usuario


def cadastrar_conta():
    cpf = input("Digite o CPF do usuário (somente números): ")
    try:
        Conta(cpf)
        return f"Conta criada com sucesso para o usuário {get_usuario(cpf).nome}!"
    except ValueError as e:
        return e
