import os
from pathlib import Path

# (Daniel Costa: Comecei a resolução às 00:30 - 01/05/2024)

""" TODO: Atenção esse arquivo é uma nova implementação, e ainda está em fase de desenolvimento."""


# Monta sistema de arquivos da aplicação
def mountDir(dir: str):
    # Definição do sistema de arquivos
    caminho_data = Path(str(dir)).absolute()
def mountFile(file: str):
    # Linha para evitar repetição extensa de código
    arquivo_usuario = Path('\\'+str(file)+'.csv')   
    

def isNotDir():

    # Verifica se o diretório existe, caso não exista cria e concede permissões
    if not mountDir.caminho_data.exists():
        # Cria o diretório, em caso de existência evita erros através do 'exists_ok=True'
        mountDir.caminho_data.mkdir(exist_ok=True)
        # Atribui permissões ao diretório
        mountDir.caminho_data.chmod(0o000777)


def isNotFile():

    # Verifica se o arquivo existe, caso não exista cria e concede permissões
    if not mountFile.arquivo_usuario.exists():
        # Cria o arquivo usuarios.csv
        mountFile.arquivo_usuario.touch()
        # Atribui permissões ao arquivo
        mountFile.arquivo_usuario.chmod(0o000777)
        
def isDir():
    if mountDir.caminho_data.exists():
        # Atribui permissões ao diretório
        mountDir.caminho_data.chmod(0o000777)
