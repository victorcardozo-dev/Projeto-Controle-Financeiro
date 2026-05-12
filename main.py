# main

from models.transacao import Transacao
from models.despesa import Despesa
from models.receita import Receita
from services.carteira import Carteira


r1 = Receita(1500,"Salário","Entrada")

d1 = Despesa(400,"Alimentação","Saída")
d2 = Despesa(100, "Academia", "Saída")
d3 = Despesa(500, "Saúde", "Saída")

carteira = Carteira()

carteira.adicionar_transacao(r1)
carteira.adicionar_transacao(d1)
carteira.adicionar_transacao(d2)

for transacao in carteira.transacoes:
    print(transacao.exibir_resumo())