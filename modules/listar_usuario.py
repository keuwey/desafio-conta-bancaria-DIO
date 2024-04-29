import csv

from business.usuario import Usuario

def ListarUsuarios():
    with open('data/usuarios.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            nome, data_nascimento, cpf, endereco = row
            print(f"Nome: {nome}, Data de Nascimento: {data_nascimento}, CPF: {cpf}, Endereço: {endereco}")