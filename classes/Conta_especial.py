from classes.Conta import Conta
import datetime

class ContaEspecial(Conta):


    def __init__(self, numero, cliente, saldo, limite):
        super().__init__(numero, cliente, saldo)
        self.limite = limite
        
    def sacar(self, valor):
        # Verifica se a soma do saldo disponível + limite cobre o saque
        if (self.saldo + self.limite) < valor:
            print(f"Saldo insuficiente! Disponível: {self.saldo + self.limite:.2f}")
            return False
        
        # Realiza o saque (o saldo pode ficar negativo aqui)
        self.saldo -= valor
        
        # Registra no extrato independente de ter usado o limite ou não
        self.extrato.transacoes.append(["Saque", valor, datetime.datetime.today()])
        
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        return True


