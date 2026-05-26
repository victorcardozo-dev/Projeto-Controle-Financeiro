# Criando a classe Carteira

from database.repository import inserir_transacao, listar_trasacoes, deletar_transacao, atualizar_transacao
from models.receita import Receita
from models.despesa import Despesa


class Carteira:

    def __init__(self):
        self.transacoes = []


    def adicionar_transacao(self, transacao):

        self.transacoes.append(transacao)

        inserir_transacao(transacao)


    def calcular_saldo(self):

        saldo = 0

        for transacao in self.transacoes:

            if transacao.__class__.__name__ == "Receita":
                saldo += transacao.valor

            elif transacao.__class__.__name__ == "Despesa":
                saldo -= transacao.valor

        return saldo
    


    def carregar_transacoes(self):

        dados = listar_trasacoes()

        self.transacoes = []

        for item in dados:

            id_transacao = item[0]
            tipo = item[1]
            valor = item[2]
            descricao = item[3]
            categoria = item[4]
            data = item[5]

            if tipo == "Receita":

                transacao = Receita(
                    valor,
                    descricao,
                    categoria
                )

            else:

                transacao = Despesa(
                    valor,
                    descricao,
                    categoria
                )

            transacao.id = id_transacao
            transacao.data = data

            self.transacoes.append(transacao)
        

    def remover_transacao(self, indice):

        if 0 <= indice < len(self.transacoes):
            
            transacao = self.transacoes[indice]

            deletar_transacao(transacao.id)

            self.transacoes.pop(indice)

            return True
        
        return False
    

    def editar_transacao(self, indice, valor, descricao, categoria):

        if 0 <= indice < len(self.transacoes):

            transacao = self.transacoes[indice]

            transacao.valor = valor
            transacao.descricao = descricao
            transacao.categoria = categoria

            atualizar_transacao(transacao)

            return True
        
        return False
    

    def gerar_relatorio(self):

        total_receita = 0
        total_despesa = 0

        for transacao in self.transacoes:

            if transacao.__class__.__name__ == "Receita":

                total_receita += transacao.valor

            elif transacao.__class__.__name__ == "Despesa":

                total_despesa += transacao.valor

        saldo = total_receita - total_despesa

        return{
            "receita": total_receita,
            "despesa": total_despesa,
            "saldo": saldo
        }
        

    def filtrar_por_categoria(self, categoria):

        resultado = []

        for transacao in self.transacoes:

            if transacao.categoria.strip().lower() == categoria.strip().lower():

                resultado.append(transacao)

        return resultado


    def filtrar_por_tipo(self, tipo):

        resultado = []

        for transacao in self.transacoes:

            if transacao.__class__.__name__ == tipo:
                
                resultado.append(transacao)

        return resultado
    

    def filtrar_por_data(self, data):

        resultado = []

        for transacao in self.transacoes:

            if transacao.data == data:

                resultado.append(transacao)

        return resultado