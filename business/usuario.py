import csv
import re
import os
from pathlib import Path

caminho_data = Path().absolute()
caminho_data.chmod(0o000600)


class Usuario:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        if not re.match(r"\d{2}/\d{2}/\d{4}", data_nascimento):
            raise ValueError("Data de nascimento inválida")
        if not re.match(r"\d{11}", cpf):
            raise ValueError("CPF inválido")
        if not re.match(r".+, \d+ - .+ - .+/\w{2}", endereco):
            raise ValueError("Endereço inválido")
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

        # Verifica se o arquivo existe e faz as alterações com os novos dados
        # ! Não sei se a linha abaixo funciona. Fazer alguns testes depois
        if os.path.exists(Path(caminho_data, "\\data\\usuarios.csv")):

            with open(str(caminho_data) + "\\data\\usuarios.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[2] != self.cpf:
                        with open(
                            str(caminho_data) + "\\data\\usuarios.csv", "a", newline=""
                        ) as file:
                            writer = csv.writer(file)
                            writer.writerow(
                                [
                                    self.nome,
                                    self.data_nascimento,
                                    self.cpf,
                                    self.endereco,
                                ]
                            )

        # Caso o arquivo não exista, cria o arquivo e faz a inclusão das informações
        else:
            with open(str(caminho_data) + "\\data\\usuarios.csv", "r") as file:
                with open("data\\usuarios.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [self.nome, self.data_nascimento, self.cpf, self.endereco]
                    )
