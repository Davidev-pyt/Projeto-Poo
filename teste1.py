from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.Conta_especial import ContaEspecial
from classes.Remunerada import remunerada
# Testando o código

Cliente1 = Cliente(cpf='123' , nome='João Silva',endereco= 'Rua A')
Cliente2 = Cliente(cpf='224', nome='Mari Souza', endereco='Rua B')
Cliente3 = Cliente(cpf='333', nome='Zezinho', endereco='Rua C')
Cliente4 = Cliente(cpf='444', nome='Mariazinha', endereco='Rua D')

conta1 = Conta(cliente=[Cliente1], numero= 1, saldo=2000)
conta2 = Conta(cliente=[Cliente2], numero=2, saldo=2000)
conta3 = ContaEspecial(cliente=[Cliente3], numero=3, saldo=2000,limite=1000)
conta4 = remunerada(cliente=[Cliente4], numero=4, saldo=2000, taxa_remuneracao=0.10)


conta4.depositar(500)
conta4.remunerar(0.10)
conta4.gerar_saldo()