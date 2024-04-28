import csv

from business.conta import Conta

def get_conta(numero: int) -> Conta:
    with open("contas.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])
            if int(row[0]) == numero:
                with open("usuarios.csv", "r") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        return Conta(row[2])
    raise ValueError("Conta não encontradatrtr434d")
