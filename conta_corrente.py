from usuario import usuarios

contas = {}


class ContaCorrente:
    proximo_numero = 1

    def __init__(self, cpf: str):
        if cpf not in usuarios:
            raise ValueError("Usuário não encontrado")
        self.agencia = "0001"
        self.numero = ContaCorrente.proximo_numero
        ContaCorrente.proximo_numero += 1
        self.usuario = usuarios[cpf]
        self.saldo = 0.0
        self.transacoes: list = []
        self.saques_diarios = 0
        self.usuario.contas.append(self)
        contas[self.numero] = self

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
