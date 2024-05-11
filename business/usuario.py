import csv
import re
from pathlib import Path


class Usuario:
    # lista para armazenar CPFs cadastrados para posterior verificação
    cpf_set = set()

    def __init__(
            self,
            nome: str,
            data_nascimento: str,
            cpf: str,
            endereco_logradouro: str,
            endereco_numero: str,
            endereco_bairro: str,
            endereco_cidade: str,
            lista_contas,
    ):
        if not re.match(r"\d{2}/\d{2}/\d{4}", data_nascimento):
            raise ValueError("Data de nascimento inválida")
        if not re.match(r"\d{11}", cpf):
            raise ValueError("CPF inválido")
        if not re.match(r".+", endereco_logradouro):
            raise ValueError("Informação Incorreta!")
        if not re.match(r"\d+", endereco_numero):
            raise ValueError("Número incorreto!")
        if not re.match(r".+", endereco_bairro):
            raise ValueError("Número inválido!")
        if not re.match(r".+/\w{2}", endereco_cidade):
            raise ValueError("Informação Incorreta. Ex: São Paulo/SP!")

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco_logradouro = endereco_logradouro
        self.endereco_numero = endereco_numero
        self.endereco_bairro = endereco_bairro
        self.endereco_cidade = endereco_cidade
        self.contas = [] or lista_contas

        # (Daniel Costa: Comecei a resolução às 00:30 - 01/05/2024)

        # Definição do sistema de arquivos (Reformulado por Daniel Costa)
        self.caminho_data = Path("data").absolute()
        # Linha para evitar repetição extensa de código
        self.arquivo_usuario = Path(str(self.caminho_data) + "\\usuarios.csv")

        # Verifica se é um diretório
        if not self.caminho_data.is_dir():
            # Cria o diretório, em caso de existência evita erros através
            # do 'exists_ok=True'
            self.caminho_data.mkdir(exist_ok=True)
            # Atribui permissões ao diretório
            self.caminho_data.chmod(0o000777)

        # Se o arquivo existir, realiza as instruções abaixo:
        # - Abre o arquivo
        # - Lê campo por campo

    def cpf_exist(self):
        return self.cpf in Usuario.cpf_set

    def add_user(self):
        with open(str(self.arquivo_usuario), "r+") as file:
            reader = csv.reader(file)
            for row in reader:
                # Adiciona CPF a lista de CPFs para comparação
                Usuario.cpf_set.add(row[2])
            if not self.cpf_exist():
                writer = csv.writer(file, lineterminator='\r')
                writer.writerow(
                    [
                        self.nome,
                        self.data_nascimento,
                        self.cpf,
                        self.endereco_logradouro,
                        self.endereco_numero,
                        self.endereco_bairro,
                        self.endereco_cidade,
                        self.contas,
                    ]
                )
            else:
                print(
                    "Não foi possível adicionar usuário, CPF: "
                    + str(self.cpf)
                    + " já cadastrado!"
                )

        # Senão, caso o arquivo não exista realiza as instruções abaixo:
        else:
            # Cria o arquivo usuarios.csv
            self.arquivo_usuario.touch()
            # Atribui permissões ao arquivo
            self.arquivo_usuario.chmod(0o000777)
            # Após criar o arquivo faz a inclusão das informações
            with open(str(self.arquivo_usuario), "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        self.nome,
                        self.data_nascimento,
                        self.cpf,
                        endereco_logradouro,
                        endereco_numero,
                        endereco_bairro,
                        endereco_cidade,
                    ]
                )
