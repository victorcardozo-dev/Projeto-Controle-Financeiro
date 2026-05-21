
from rich import print


def mostra_linha(valor=35):
    print("-" * valor)



def exibir_transacoes(lista):

    if lista:

        for transacao in lista:

            print(transacao.exibir_resumo())
            print()

    else:

        print("[red]Nenhuma transação encontrada.[/]")
        