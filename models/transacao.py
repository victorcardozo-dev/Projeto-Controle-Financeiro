#Classe Transação

class Transacao():
    def __init__(self, valor = 0, descricao = "Não informado", categoria = "Não informado"):
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria

    def exibir_resumo(self):
        mensagem = (
            f"{self.__class__.__name__:-^30}" 
            f"\nVALOR: R${self.valor:.2f}"
            f"\nDESCRIÇÃO: {self.descricao}"
            f"\nCATEGORIA: {self.categoria}"
            )
        return mensagem
