import csv
from modules.get_dirFile import *
from business.usuario import Usuario

# Testando nova implemtação do sistema de arquivos
data = mountDir('data')
usuarios = mountFile('usuarios')

def ListarUsuarios():
    with open(str(data) +'\\'+str(usuarios), 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nome, data_nascimento, cpf, endereco = row
            print('Nome: '+str(nome)+', Data de Nascimento: '+str(data_nascimento)+', CPF: '+str(cpf)+', Endereço:' +str(endereco))