from classes.Conta import Conta
from classes.Poupanca import Poupanca

class remunerada(Conta, Poupanca):

    def __init__(self, cliente, numero, saldo, taxa_remuneracao):
        Conta.__init__(self, cliente, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)
        
        
    def remunerar(self, valor):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30) # Supondo que a remuneração seja diária, dividimos a taxa por 30
        