import csv
from pathlib import Path

caminho_data = Path().absolute()
caminho_data.chmod(0o000600)


def get_conta(numero: int):
    # Acessa o arquivo conta - <numero-da-conta>.csv em modo de leitura "r"
    with open(str(caminho_data) + "\\data\\conta-" + str(numero) + ".csv", "r") as file:
        reader = csv.reader(file)
        # Para cada campo dentro dentro do arquivo lido retorna uma lista
        for row in reader:
            # Se o campo na posição 0 for igual ao numero digitado
            if int(row[0]) == numero:
                # Acesa o arquivo usuarios.csv em modo de leitura
                with open(str(caminho_data) + "\\data\\usuarios.csv", "r") as file:
                    reader = csv.reader(file)
                    # Para cada campo dentro dentro do arquivo lido retorna uma lista
                    for row in reader:
                        # Retorna o campo na posição 2, no campo o campo onde contem o
                        # CPF, logo retorna o CPF do usuário
                        return Conta(row[2])
    raise ValueError("Conta não encontrada")
