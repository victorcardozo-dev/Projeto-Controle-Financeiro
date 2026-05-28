# main

from database.schema import criar_tabela
from rich import print
from services.carteira import Carteira
from ui.menus import (
    mostrar_menu, adicionar_receita, adicionar_despesa,
    listar_transacoes, mostrar_saldo, remover_transacao,
    editar_transacao, relatorio_financeiro, filtrar_transacoes
)


criar_tabela()

carteira = Carteira()
carteira.carregar_transacoes()


while True:

    escolha = mostrar_menu()

    if escolha < 1  or escolha > 9:
        print("-" * 35)
        print(f"[red]Digite uma opção válida! [/]")
        

    elif escolha == 9:
        break


    elif escolha == 1:
        adicionar_receita(carteira)


    elif escolha == 2:
        adicionar_despesa(carteira)


    elif escolha == 3:
        listar_transacoes(carteira)
    

    elif escolha == 4:
        mostrar_saldo(carteira)


    elif escolha == 5:
        remover_transacao(carteira)


    elif escolha == 6:
        editar_transacao(carteira)


    elif escolha == 7:
        relatorio_financeiro(carteira)


    elif escolha == 8:
        filtrar_transacoes(carteira)
