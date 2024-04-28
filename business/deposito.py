from modules.get_conta import get_conta
from business.conta import depositar

def realizarDeposito():
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor que você deseja depositar: "))
    try:
        conta = get_conta(numero)
       # print(conta.depositar(valor))
        depositar(valor)
    except ValueError:
        print("Conta não encontrada")