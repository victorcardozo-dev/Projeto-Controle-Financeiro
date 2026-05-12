# Criando a classe Carteira


class Carteira:
    def __init__(self):
        self.transacoes = []


    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


    def calcular_saldo(self):

        saldo = 0

        for transacao in self.transacoes:

            if transacao.__class__.__name__ == "Receita":
                saldo += transacao.valor

            elif transacao.__class__.__name__ == "Despesa":
                saldo -= transacao.valor

        return saldo