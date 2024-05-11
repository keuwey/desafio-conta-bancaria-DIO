from modules.cadastro_usuario import cadastrar_usuario
from modules.cadastro_conta import cadastrar_conta
from modules.listar_usuario import listar_usuarios
from modules.listar_conta import listar_contas
from business.deposito import realizar_deposito

menu = """
[cu] Cadastrar Usuário
[cc] Cadastrar Conta
[lu] Listar usuários
[lc] Listar contas de um usuário
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

while True:

    opcao = input(menu).lower()

    match opcao:
        case "cu":
            cadastrar_usuario()
        case "cc":
            print(cadastrar_conta())
        case "lu":
            listar_usuarios()
        case "lc":
            listar_contas()
        case "d":
            realizar_deposito()
        case "s":
            realizar_deposito()
        case "e":
            realizar_deposito()
        case "q":
            break
        case _:
            print("Operação inválida!")
