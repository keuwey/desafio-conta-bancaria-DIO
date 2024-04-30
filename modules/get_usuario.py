import csv
from pathlib import Path

caminho_data = Path().absolute()
caminho_data.chmod(0o000600)


from business.usuario import Usuario


def get_usuario(cpf: str):
    with open(str(caminho_data) + "\\data\\usuarios.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == cpf:
                return Usuario(*row)
    raise ValueError("Usuário não encontrado")
