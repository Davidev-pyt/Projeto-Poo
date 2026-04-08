#Tratamento de Exceções
class exceptioncustom(Exception):
    pass

def divisao(a, b):
    return a / b


try:
        resultado = divisao(10, 0)
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
else:
    print(f'O resultado da divisão é {resultado}.')

def validar_idade(idade):
     if idade < 0:
          raise exceptioncustom('A idade não pode ser negativa.')
try: validar_idade(-10)
except exceptioncustom as ex:
        print(f'Erro: {ex}')