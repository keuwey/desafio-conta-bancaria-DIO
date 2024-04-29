from modules.get_conta import get_conta
from business.conta import Conta

def realizarDeposito():
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor que você deseja depositar: "))
    try:
        conta = get_conta(numero)
<<<<<<< HEAD
        print(Conta.depositar(conta,valor))
=======
        print(depositar(conta,valor))
>>>>>>> c250ee8c654981e21d3e91df2a502031ead9f0fe
    except ValueError:
        print("Conta não encontrada")