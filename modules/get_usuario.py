import csv

from business.usuario import Usuario

def get_usuario(cpf: str):
    with open("data/usuarios.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == cpf:
                return Usuario(*row)
    raise ValueError("Usuário não encontrado")
