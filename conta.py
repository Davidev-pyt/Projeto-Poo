#Código da classe
from time import sleep
class Conta:
    def __init__(self, numero, cpf,  titular, saldo):
     self.numero = numero
     self.cpf = cpf
     self.titular = titular
     self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False #Não é possivel sacar. saldo insuficiente
        else:
            self.saldo -= valor
            return True #Saque realizado com sucesso
    
    def gerar_extrato(self):
        print(f'Número {self.numero} CPF {self.cpf} Nome: {c1.titular} Saldo R${self.saldo:.2f}')

    def transferir(self, conta_destino, valor):
        if self.saldo < valor:
            return('\033[31m Não foi possivel transferir. saldo insuficiente. \033[m') #Não é possível transferir. Saldo insuficiente
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            return('Transferência realizada com sucesso.') #Transferência realizada com sucesso
#Código de teste
c1 = Conta(123, '123.456.789-00', 'Davi Henrique', 1000.00)
c2 = Conta(456, '987.657.321-00', 'Maria Silva', 500.00)
c1.depositar(500)
valor_saque = (200)
resultado_saque = c1.sacar(valor_saque)

if resultado_saque:
    print(f'Saque de R${valor_saque:.2f} realizado com sucesso.')
else:
    print(f'\033[31m Não foi possível realizar o saque de R${valor_saque:.2f}. Saldo insuficiente.\033[m')

print('Realizando transferência...')
sleep(1)
print(c1.transferir(c2, 200))
print('Gerando extrato...')
sleep(1)
c1.gerar_extrato()
c2.gerar_extrato()

