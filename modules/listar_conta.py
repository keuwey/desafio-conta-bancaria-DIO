from modules.get_usuario import get_usuario


def listar_contas():

    cpf = input("Digite o CPF do usuário (somente números): ")
    try:
        usuario = get_usuario(cpf)
        for conta in usuario.contas:
            return f"Número da conta: {conta.numero}\nSaldo: R$ {conta.saldo:.2f}"
    except ValueError:
        return "Usuário não encontrado"
