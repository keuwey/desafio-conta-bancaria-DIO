import csv


def ListarUsuarios():
    with open("data/usuarios.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            nome, data_nascimento, cpf, endereco = row
            return (
                f"Nome: {nome}, Data de Nascimento: {data_nascimento},"
                f"CPF: {cpf}, Endereço: {endereco}"
            )
