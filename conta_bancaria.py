class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.transacoes = []
        self.saques_diarios = 0

    def depositar(self, valor: float) -> str:
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(('Depósito', valor))
            return f"Depósito de R$ {valor:.2f} realizado com sucesso!\nSaldo atual: R$ {self.saldo:.2f}"
        return "Digite um valor positivo"

    def sacar(self, valor: float) -> str:
        if self.saques_diarios >= 3:
            return "Você já atingiu o limite diário de saques."
        if valor > 500:
            return "O valor máximo para saque é de R$ 500,00."
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(('Saque', -valor))
            self.saques_diarios += 1
            return f"Saque no valor de R$ {valor:.2f} realizado com sucesso\nSaldo atual: R$ {self.saldo:.2f}"
        return "O valor que você deseja sacar é maior que o saldo atual da sua conta."

    def extrato(self) -> str:
        extrato = ""
        for transacao, valor in self.transacoes:
            extrato += f"{transacao}: R$ {valor:.2f}\n"
        extrato += f"Saldo atual: R$ {self.saldo:.2f}"
        return extrato
