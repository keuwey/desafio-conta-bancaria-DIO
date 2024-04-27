import csv

from usuario import Usuario


def get_usuario(cpf: str) -> Usuario:
    with open("usuarios.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == cpf:
                return Usuario(*row)
    raise ValueError("Usuário não encontrado")
