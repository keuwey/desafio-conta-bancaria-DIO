from modules.cadastro_usuario import CadastrarUsuario
from modules.cadastro_conta import CadastrarConta
from modules.listar_usuario import ListarUsuarios
from modules.listar_conta import ListarContas
from business.deposito import realizarDeposito

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
            CadastrarUsuario()
            print("funcionando")
        case "cc":
            CadastrarConta()
            print("funcionando")
        case "lu":
            ListarUsuarios()
            print("funcionando")
        case "lc":
            ListarContas()
            print("funcionando")
        case "d":
            realizarDeposito()
            print("funcionando")
        case "s":
            #
            realizarDeposito()
        case "e":
            #
            realizarDeposito()
        case "q":    
            break
        case _:
            print("Operação inválida!")


"""
* TODO: fix: When a user wants to make a transaction and the system creates duplicated data,
e.g.: a duplicated user or a duplicated account.
"""

