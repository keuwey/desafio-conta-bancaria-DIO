import os
from pathlib import Path

# (Daniel Costa: Comecei a resolução às 00:30 - 01/05/2024)

""" TODO: Atenção esse arquivo é uma nova implementação, e ainda está em fase de desenolvimento."""

# Monta sistema de arquivos da aplicação
def mountDir(dir: str):
    # Definição do sistema de arquivos
    caminho_data = Path(str(dir)).absolute()
    
def mountFile(self,file: str):
    # Linha para evitar repetição extensa de código
    arquivo_usuario = Path(str(self.caminho_data)+'\\'+str(file)+'.csv')
    arquivo_conta = Path(str(self.caminho_data)+'\\'+str(file)+'.csv')   