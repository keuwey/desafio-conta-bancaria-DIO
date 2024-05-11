import csv
import os

from modules.get_usuario import get_usuario
from pathlib import Path


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

        # (Daniel Costa: Comecei a resolução às 00:30 - 01/05/2024)

        # Definição do sistema de arquivos (Reformulado por Daniel Costa)
        self.caminho_data = Path("data").absolute()
        # Linha para evitar repetição extensa de código
        # (Introduzida por Daniel Costa)
        self.arquivo_conta = Path("/conta-" + str(self.numero) + ".csv")
        self.arquivo_trans = Path("/transacoes-" + str(self.numero) + ".csv")

        if not self.caminho_data.exists():
            # Cria o diretório, em caso de existência evita erros através
            # do 'exists_ok=True'
            self.caminho_data.mkdir(exist_ok=True)
            # Atribui permissões ao diretório
            self.caminho_data.chmod(0o000600)
            # Cria os arquivos conta e transações caso não existam.
            self.arquivo_conta.touch()
            self.arquivo_trans.touch()
            print("criado com sucesso!")

            # Faz o registro da nova conta criada
            with open(
                    str(self.caminho_data) + str(self.arquivo_conta), "w", newline=""
            ) as f:
                writer = csv.writer(f)
                writer.writerow([self.numero, self.usuario.nome, self.saldo])
        else:
            # Caso exista não faz nada!
            print("PSeudos Eggs:.. But still have not found what im looking for...")

    # Método para DEPOSITAR
    def depositar(self, valor: float) -> str:
        if valor > 0:

            with open(
                    str(self.caminho_data) + str(self.arquivo_conta), "r", newline=""
            ) as f:
                reader = csv.reader(f)
                for row in reader:
                    self.saldo = float(row[2])
                    self.saldo += valor

                # Atualiza o saldo do cliente, cria um arquivo exclusivo para cada
                # conta de cliente com número da conta ao lado
                with open(
                        str(self.caminho_data) + str(self.arquivo_conta), "w+", newline=""
                ) as f:
                    writer = csv.writer(f)
                    writer.writerow([self.numero, self.usuario.nome, self.saldo])

                # Adiciona registro as transações cria um arquivo exclusivo para cada
                # conta de cliente com número da conta ao lado
                with open(
                        str(self.caminho_data) + str(self.arquivo_trans), "w+", newline=""
                ) as f:
                    writer = csv.writer(f)
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

    # Método para SACAR
    def sacar(self, valor: float) -> str:
        if self.saques_diarios >= 3:
            return "Você já atingiu o limite diário de saques."
        if valor > 500:
            return "O valor máximo para saque é de R$ 500,00."
        if self.saldo >= valor:
            self.saldo -= valor
            self.saques_diarios += 1

            # Adiciona registro as transações cria um arquivo exclusivo para cada
            # conta de cliente com número da conta ao lado
            with open(
                    str(self.caminho_data) + str(self.arquivo_trans), "w+", newline=""
            ) as f:
                writer = csv.writer(f)
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

    # Método para EXTRATO
    # def extrato(self) -> str:
    #     extrato = ""
    #     for transacao, valor in self.transacoes:
    #         extrato += f"{transacao}: R$ {valor:.2f}\n"
    #     extrato += f"Saldo atual: R$ {self.saldo:.2f}"
    #     return extrato
