import csv
from modules.get_dirFile import *
from business.usuario import Usuario

# Testando nova implementação do sistema de arquivos
data = mount_dir("data")
usuarios = mount_file("usuarios")


def get_usuario(cpf: str):
    with open(str(data) + "\\" + str(usuarios), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == cpf:
                return Usuario(*row)
    raise ValueError("Usuário não encontrado")
