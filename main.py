# main

from models.transacao import Transacao
from models.despesa import Despesa
from models.receita import Receita

t1 = Transacao(500, "Saúde", "Saída")
print(t1.exibir_resumo())

d1 = Despesa(400,"Alimentação","Saída")
print(d1.exibir_resumo())

r1 = Receita(1500,"Salário","Entrada")
print(r1.exibir_resumo())