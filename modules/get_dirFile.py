from pathlib import Path

# (Daniel Costa: Comecei a resolução às 00:30 - 01/05/2024)

"""
TODO: Atenção esse arquivo é uma nova implementação, e ainda está
em fase de desenolvimento.

"""


# Monta sistema de arquivos da aplicação
def mount_dir(dir: str):
    # Definição do sistema de arquivos
    caminho_data = Path(str(dir)).absolute()
    return caminho_data


def mount_file(file: str):
    # Definição dos arquivos
    if file == "usuarios":
        arquivo_usuario = Path(str(file) + ".csv")
        return arquivo_usuario
    if file == "contas":
        arquivo_conta = Path(str(file) + ".csv")
        return arquivo_conta
