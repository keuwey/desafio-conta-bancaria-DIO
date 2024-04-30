import csv
import os

from modules.get_usuario import get_usuario
from pathlib import Path

caminho_data = Path().absolute()
caminho_data.chmod(0o000600)


class Conta:

    contadorConta = 0  # Contador para incrementar os números das contas

    # Construtor da classe Conta
    def __init__(self, cpf: str):
        usuario = get_usuario(cpf)
        self.agencia = "1"
        Conta.contadorConta += 1
        self.numero = Conta.contadorConta
        self.usuario = usuario
        self.saldo = 0.0
        self.saques_diarios = 0

        # Verifica se o arquivo existe, caso existe não faz nada para não
        # duplicar o arquivo.
        # ! Testar se esse str(caminho_data...) funciona
        if os.path.exists(
            str(caminho_data) + "\\data\\conta-" + str(self.numero) + ".csv"
        ):
            print()

        # Caso o arquivo não exista faz o devido cadastro.
        else:
            # Faz o registro da nova conta criada
            with open(
                str(caminho_data) + "\\data\\conta-" + str(self.numero) + ".csv",
                "x+",
                newline="",
            ) as f:
                writer = csv.writer(f)
                writer.writerow([self.numero, self.usuario.nome, self.saldo])

    # Metódo para DEPOSITAR
    def depositar(self, valor: float) -> str:
        if valor > 0:

            with open(
                "\\data\\conta-" + str(self.numero) + ".csv", "r", newline=""
            ) as file:
                reader = csv.reader(file)
                for row in reader:
                    self.saldo = float(row[2])
                    self.saldo += valor

            # Atualiza o saldo do cliente, cria um arquivo exclusivo para cada conta
            # de cliente com numero da conta ao lado
            with open(
                "\\data\\conta-" + str(self.numero) + ".csv", "w+", newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow([self.numero, self.usuario.nome, self.saldo])

            # Adciona registro as transações cria um arquivo exclusivo para cada
            # conta de cliente com numero da conta ao lado
            with open(
                "\\data\\transacoes" + str(self.numero) + ".csv", "a", newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "N: da Conta: " + str(self.numero),
                        " Tipo: Deposito ",
                        "Valor R$: " + str(valor),
                    ]
                )

            # Retorna mensagem ao usuário informando que a operação foi
            # realizada com sucesso
            return (
                f"Depósito de R$ {valor:.2f} realizado com sucesso!"
                f"\nSaldo atual: R$ {self.saldo:.2f}"
            )
        return "Digite um valor positivo"

    # Metódo para SACAR
    def sacar(self, valor: float) -> str:
        if self.saques_diarios >= 3:
            return "Você já atingiu o limite diário de saques."
        if valor > 500:
            return "O valor máximo para saque é de R$ 500,00."
        if self.saldo >= valor:
            self.saldo -= valor
            self.saques_diarios += 1

            # Adciona registro as transações cria um arquivo exclusivo para cada
            # conta de cliente com numero da conta ao lado
            with open(
                "\\data\\transacoes-" + str(self.numero) + ".csv", "a+", newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "Nº Conta: " + str(self.numero),
                        "Tipo: Saque",
                        "Valor R$ : " + str(valor),
                    ]
                )

            # Retorna mensagem ao usuário informando que a operação foi realizada
            # com sucesso
            return (
                f"Saque no valor de R$ {valor:.2f} realizado com sucesso"
                f"\nSaldo atual: R$ {self.saldo:.2f}"
            )
        return "O valor que você deseja sacar é maior que o saldo da sua conta."

    # Metódo para EXTRATO
    # def extrato(self) -> str:
    #     extrato = ""
    #     for transacao, valor in self.transacoes:
    #         extrato += f"{transacao}: R$ {valor:.2f}\n"
    #     extrato += f"Saldo atual: R$ {self.saldo:.2f}"
    #     return extrato
