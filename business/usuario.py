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
        cpf_list = [] # lista para armezar cpfs cadastrados, para posterior verificação
        
        # (Daniel Costa: Comecei a resolução ás 00:30 - 01/05/2024)

        # Definição do sistema de arquivos (Reformulado por Daniel Costa)
        self.caminho_data = Path('data').absolute()
        # Linha para evitar repetição extensa de código
        self.arquivo_usuario = Path(str(self.caminho_data) + '\\usuarios.csv')
        
        # Verfica se é um diretório
        if not self.caminho_data.is_dir():
           # Cria o diretório, em caso de existência evita erros através do 'exists_ok=True'
           self.caminho_data.mkdir(exist_ok=True)
           # Atribui permissões ao diretório
           self.caminho_data.chmod(0o000777)
        
        # Se o arquivo existir, realiza as intruções abaixo: abre o arquivo e lê campo por campo
        if self.arquivo_usuario.exists():
            with open(str(self.arquivo_usuario), "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    # Adiciona CPF a lista de cpfs para comparação
                    cpf_list.append(row[2])
            # Se o CPF não estiver na lista adiciona novo Usuário        
            if self.cpf not in cpf_list:
                # Faz a inclusão das novas informações caso o cpf do usuário não exista na lista
                with open(str(self.arquivo_usuario), "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.nome, self.data_nascimento, self.cpf, self.endereco])
                    print("Usuário " + str(self.nome) + " criado com sucesso!")
            else: 
                print("Não foi possível adicionar usuário, CPF: "+ str(self.cpf) +" já cadastrado!")
                
        # Senão, caso o arquivo não exista realiza as instruções abaixo:        
        else:
            # Cria o arquivo usuarios.csv
            self.arquivo_usuario.touch()
            # Atribui permissões ao arquivo
            self.arquivo_usuario.chmod(0o000777)
            # Após criar o arquivo faz a inclusão das informações
            with open(str(self.arquivo_usuario), "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.nome, self.data_nascimento, self.cpf, self.endereco])