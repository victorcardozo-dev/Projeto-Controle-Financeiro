# main

from rich import print
from models.despesa import Despesa
from models.receita import Receita
from services.carteira import Carteira
from utils.funcoes_uteis import leiaint, mostra_linha, leia_float


carteira = Carteira()
carteira.carregar_transacoes()

while True:
    print(
        f"[green]{' MENU DO SISTEMA ':-^60}[/]"
        f"[blue]\n1- Adicionar Receita"
        f"\n2- Adicionar Despesa"
        f"\n3- Listar Transações"
        f"\n4- Mostrar Saldo"
        f"\n5- Sair[/]"
        f"[green]\n{'-' * 60}[/]"
        )
    
    escolha = leiaint("Qual sua opção: ")
    if escolha < 1  or escolha > 5:
        mostra_linha()
        print(f"[red]Digite uma opçao válida! [/]")
        

    elif escolha == 5:
        carteira.salvar_transacoes()
        break

    elif escolha == 1:
        mostra_linha()
        valor = leia_float("Qual o valor da receita: ")
        descricao = str(input("Qual a descrição da receita: "))
        categoria = str(input("Qual a categoria da receita: "))

        receita = Receita(valor, descricao, categoria)
        carteira.adicionar_transacao(receita)
        print()
    
    elif escolha == 2:
        mostra_linha()
        valor = leiaint("Qual o valor da despesa: ")
        descricao = str(input("Qual a descrição da despesa: "))
        categoria = str(input("Qual a categoria da despesa: "))

        despesa = Despesa(valor, descricao, categoria)
        carteira.adicionar_transacao(despesa)
        print()

    elif escolha == 3:
        mostra_linha()
        for transacao in carteira.transacoes:
            print(transacao.exibir_resumo())
            print()
    
    elif escolha == 4:
        mostra_linha()
        print(f"[green on white]O saldo atual da sua carteira é de R${carteira.calcular_saldo():.2f}[/]")
        print()
