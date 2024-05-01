import csv
from pathlib import Path

caminho_data = Path().absolute()
caminho_data.chmod(0o000600)


def ListarUsuarios():
    with open(str(caminho_data) + "\\data\\usuarios.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            nome, data_nascimento, cpf, endereco = row
            return (
                f"Nome: {nome}, Data de Nascimento: {data_nascimento},"
                f"CPF: {cpf}, Endereço: {endereco}"
            )
