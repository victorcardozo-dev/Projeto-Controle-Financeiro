# Criando a classe Carteira

import json
from models.receita import Receita
from models.despesa import Despesa


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
    
    def salvar_transacoes(self):
        
        dados = []

        for transacao in self.transacoes:

            dados.append({
                "id": transacao.id,
                "data": transacao.data,
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "descricao": transacao.descricao,
                "categoria": transacao.categoria
            })

        with open("data/dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)


    def carregar_transacoes(self):
        
        try:

            with open("data/dados.json", "r", encoding="utf-8") as arquivo:

                dados = json.load(arquivo)
                    
                for item in dados:

                    if item["tipo"] == "Receita":

                        transacao = Receita(
                            item["valor"],
                            item["descricao"],
                            item["categoria"]
                        )

                    elif item["tipo"] == "Despesa":

                        transacao = Despesa(
                            item["valor"],
                            item["descricao"],
                            item["categoria"]
                        )

                    transacao.id = item["id"]
                    transacao.data = item["data"]
                    
                    self.transacoes.append(transacao)

        except (FileNotFoundError, json.JSONDecodeError): # Se o arquivo .json estiver vazio, quebrado ou inválido o sistema vai iniciar com ele vazio.
            self.transacoes = []

    
    def remover_transacao(self, indice):

        if 0 <= indice < len(self.transacoes):

            removida = self.transacoes.pop(indice)

            return removida
        
        return None
    

    def editar_transacao(self, indice, valor, descricao, categoria):

        if 0 <= indice < len(self.transacoes):

            transacao = self.transacoes[indice]

            transacao.valor = valor
            transacao.descricao = descricao
            transacao.categoria = categoria

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