import csv
import re
import os

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
<<<<<<< HEAD

        # Verifica se o arquivo existe e faz as alterações com os novos dados
        if os.path.exists("data/usuarios.csv"):
    
            with open("data/usuarios.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if (row[2] != self.cpf):
                        with open("data/usuarios.csv", "a", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow([self.nome, self.data_nascimento, self.cpf, self.endereco])
                            
        # Caso o arquivo não exista, cria o arquivo e faz a inclusão das informações      
        else:
            with open("data/usuarios.csv", "x") as file:
                with open("data/usuarios.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.nome, self.data_nascimento, self.cpf, self.endereco])
=======
        self.contas: list = []
        
        with open("usuarios.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.nome, self.data_nascimento, self.cpf, self.endereco])
>>>>>>> c250ee8c654981e21d3e91df2a502031ead9f0fe
