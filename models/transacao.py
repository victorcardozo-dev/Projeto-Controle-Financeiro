#Classe Transação

import uuid
from datetime import datetime

class Transacao():

    def __init__(self, valor = 0, descricao = "Não informado", categoria = "Não informado"):

        self.id = str(uuid.uuid4())
        self.data = datetime.now().strftime("%d/%m/%Y")
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria


    def exibir_resumo(self):

        mensagem =(
            f"{self.__class__.__name__:-^45}" 
            f"\nID: {self.id}"
            f"\nDATA: {self.data}"
            f"\nVALOR: R${self.valor:.2f}"
            f"\nDESCRIÇÃO: {self.descricao}"
            f"\nCATEGORIA: {self.categoria}"
        )
        
        return mensagem
    

