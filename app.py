from conta_bancaria import ContaBancaria

conta = ContaBancaria()

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

while True:
    opcao = input(menu).lower()
    if opcao == "d":
        valor = float(input("Digite o valor que você deseja depositar: "))
        print(conta.depositar(valor))
    elif opcao == "s":
        valor = float(input("Digite o valor que você deseja sacar: "))
        print(conta.sacar(valor))
    elif opcao == "e":
        print(conta.extrato())
    elif opcao == "q":
        break
    else:
        print("Operação inválida!")
