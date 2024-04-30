import csv
from business.conta import Conta


def get_operacoes(self, operacaoTipo: str):
    
    
    with open("data/conta-"+str(Conta.numero)+".csv", "r",newline='') as file:
        reader = csv.reader(file)
        for row in reader:
                    
                if(operacaoTipo == "deposito"):
                    Conta.saldo = float(row[2])
                    Conta.saldo += Conta.valor
                if(operacaoTipo == "saque"):
                    Conta.saldo = float(row[2])
                    Conta.saldo -= Conta.valor
    # Atualiza o saldo do cliente, cria um arquivo exclusivo para cada conta de cliente com numero da conta ao lado
    with open("data/conta-" + str(Conta.numero) + ".csv","w+",newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Conta.numero,Conta.usuario.nome,Conta.saldo])

    # Adciona registro as transações cria um arquivo exclusivo para cada conta de cliente com numero da conta ao lado
    with open("data/transacoes" + str(Conta.numero) + ".csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["N: da Conta: "+ str(Conta.numero), " Tipo: "+{operacaoTipo}+"", "Valor R$: "+ str(Conta.valor)])
                
    # Retorna mensagem ao usuário informando que a operação foi realizada com sucesso
    return f"{operacaoTipo} de R$ {Conta.valor:.2f} realizado com sucesso!\nSaldo atual: R$ {Conta.saldo:.2f}"