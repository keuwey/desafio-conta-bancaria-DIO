from business.conta import Conta
from modules.get_usuario import get_usuario

def CadastrarConta() -> Conta:
    cpf = input("Digite o CPF do usuário (somente números): ")
    try:
        Conta(cpf)
        print(f"Conta criada com sucesso para o usuário {get_usuario(cpf).nome}!")
    except ValueError as e:
        print(e)