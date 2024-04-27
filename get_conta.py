import csv

from conta_corrente import ContaCorrente


def get_conta(numero: int) -> ContaCorrente:
    with open("contas.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if int(row[0]) == numero:
                return ContaCorrente(row[1])
    raise ValueError("Conta não encontrada")
