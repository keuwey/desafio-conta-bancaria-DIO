from business.usuario import Usuario

def CadastrarUsuario():

    nome = input("Digite o nome de usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF (somente números): ")
    endereco = input(
        "Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )
    try:
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        return f"Usuário {nome} criado com sucesso!"
    except ValueError as e:
        return e
