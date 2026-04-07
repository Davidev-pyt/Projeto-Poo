import datetime
from classes.Extrato import Extrato


class Conta:
    def __init__(self, cliente, numero, saldo):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Depósito", valor, datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["Saque", valor, datetime.datetime.today()])
            return True

    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            return "Saldo insuficiente para transferência."
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["Transferência", valor, datetime.datetime.today()]
            )
            return "Transferência realizada com sucesso."

    def gerar_saldo(self):
        print(f"numero:{self.numero}\nSaldo:{self.saldo}")
