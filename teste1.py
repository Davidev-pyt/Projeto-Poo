from classes.Cliente import Cliente
from classes.Conta import Conta
# Testando o código

Cliente1 = Cliente(cpf='123' , nome='João Silva',endereco= 'Rua A')
Cliente2 = Cliente(cpf='224', nome='Mari Souza', endereco='Rua B')

conta1 = Conta(cliente=[Cliente1 , Cliente2], numero= 111, saldo=0)

conta1.depositar(1000)
conta1.sacar(200)
extrato = conta1.extrato
conta1.extrato.gerar_extrato(conta1.numero)