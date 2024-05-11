import csv
from modules.get_dirFile import *

# Testando nova implemtação do sistema de arquivos
data = mount_dir("data")
usuarios = mount_file("usuarios")


def listar_usuarios():
    with open(str(data) + "\\" + str(usuarios), "r") as file:
        reader = csv.reader(file)
        for row in reader:
            (
                nome,
                data_nascimento,
                cpf,
                endereco_logradouro,
                endereco_numero,
                endereco_bairro,
                endereco_cidade,
            ) = row
            print(
                "Nome: "
                + str(nome)
                + ", Data de Nascimento: "
                + str(data_nascimento)
                + ", CPF: "
                + str(cpf)
                + ", Endereço: "
                + str(endereco_logradouro)
                + ", "
                + str(endereco_numero)
                + " - "
                + str(endereco_bairro)
                + " - "
                + str(endereco_cidade)
            )
