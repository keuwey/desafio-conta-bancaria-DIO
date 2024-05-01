import csv
import re
import os
from pathlib import Path  


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
        
        # (Daniel Costa: Comecei a resolução ás 00:30 - 01/05/2024)

        # Definição do sistema de arquivos (Reformulado por Daniel Costa)
        self.caminho_data = Path('data').absolute()
        # Linha para evitar repetição extensa de código
        self.arquivo_usuario = Path(str(self.caminho_data) + '\\usuarios.csv')
        
        
        if not self.caminho_data.exists():
            
            # Cria o diretório, em caso de existência evita erros através do 'exists_ok=True'
            self.caminho_data.mkdir(exist_ok=True)
            # Atribui permissões ao diretório 
            self.caminho_data.chmod(0o000777)
            
            # Verifica se o arquivo existe, caso não exista cria e concede permissões
            if not self.arquivo_usuario.exists():
                # Cria o arquivo usuarios.csv
                self.arquivo_usuario.touch()
                # Atribui permissões ao arquivo
                self.arquivo_usuario.chmod(0o000777)

            # Caso o arquivo não exista, cria o arquivo e faz a inclusão das informações
                with open(str(self.arquivo_usuario), "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.nome, self.data_nascimento, self.cpf, self.endereco])

        # Senão, caso o arquivo exista vai fazer a verificação se o arquivo existe.
        else:
            
           # Atribui permissões ao diretório 
           # self.caminho_data.chmod(0o000777)
           
           # Verifica se o arquivo existe, caso não exista cria e concede permissões
           if not self.arquivo_usuario.exists():
                # Cria o arquivo usuarios.csv
                self.arquivo_usuario.touch()
                # Atribui permissões ao arquivo
                self.arquivo_usuario.chmod(0o000777)
 
                with open(str(self.caminho_data) + str(self.arquivo_usuario), 'r', newline="") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row[2] != self.cpf:
                            with open(str(self.caminho_data) + str(self.arquivo_usuario), 'a+', newline="") as f:
                                writer = csv.writer(f)
                                writer.writerow([self.nome,self.data_nascimento,self.cpf,self.endereco])

        # # Caso o arquivo não exista, cria o arquivo e faz a inclusão das informações
        # else:
        #     # Cria o diretório, em caso de existência evita erros através do 'exists_ok=True'
        #     self.caminho_data.mkdir(exist_ok=True)
            
        #     with open(str(self.caminho_data) + str(self.arquivo_usuario), "w") as file:
        #         with open(str(self.caminho_data) + str(self.arquivo_usuario), "a", newline="") as file:
        #             writer = csv.writer(file)
        #             writer.writerow([self.nome, self.data_nascimento, self.cpf, self.endereco])
