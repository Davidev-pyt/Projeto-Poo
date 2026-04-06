
class Extrato: # Use Capital Case para classes
    def __init__(self):
        self.transacoes = []

    def gerar_extrato(self, conta):
        print(f'Extrato da conta {conta}') # Espaço adicionado
        for transacao in self.transacoes:
            # Removido o ":" extra antes do .strftime
            print(f'{transacao[0]:}: {transacao[1]:.2f}: {transacao[2].strftime("%d/%b/%Y")}')
