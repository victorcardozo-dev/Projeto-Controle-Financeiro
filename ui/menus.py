from rich import print
from models.despesa import Despesa
from models.receita import Receita
from ui.exibicao import exibir_transacoes, mostra_linha
from ui.inputs import leia_float, leiaint


def mostrar_menu():

    print(
    f"[green]{' MENU DO SISTEMA ':-^35}[/]"
    f"\n[blue]1- Adicionar Receita"
    f"\n2- Adicionar Despesa"
    f"\n3- Listar Transações"
    f"\n4- Mostrar Saldo"
    f"\n5- Remover transação"
    f"\n6- Editar transação"
    f"\n7- Relatório Financeiro"
    f"\n8- Filtrar Transações"
    f"\n9- Sair[/]"
    f"\n[green]{'-' * 35}[/]"
)
    escolha = leiaint("Qual sua opção: ")
    
    return escolha

def adicionar_receita(carteira):

    mostra_linha()
    valor = leia_float("Qual o valor da receita: ")
    descricao = str(input("Qual a descrição da receita: "))
    categoria = str(input("Qual a categoria da receita: "))

    receita = Receita(valor, descricao, categoria)
    carteira.adicionar_transacao(receita)
    print()


def adicionar_despesa(carteira):
        
    mostra_linha()

    valor = leiaint("Qual o valor da despesa: ")
    descricao = str(input("Qual a descrição da despesa: "))
    categoria = str(input("Qual a categoria da despesa: "))

    despesa = Despesa(valor, descricao, categoria)
    carteira.adicionar_transacao(despesa)
    print()


def listar_transacoes(carteira):

    mostra_linha()

    for indice, transacao in enumerate(carteira.transacoes):

        print(f"[yellow]ÍNDICE: {indice} [/]")
        print(transacao.exibir_resumo())
        print()


def mostrar_saldo(carteira):

    mostra_linha()

    print(f"[green on white]O saldo atual da sua carteira é de R${carteira.calcular_saldo():.2f}[/]")
    print()


def remover_transacao(carteira):
    
    mostra_linha()

    for indice, transacao in enumerate(carteira.transacoes):
        print(f"[yellow]ÍNDICE: {indice}[/]")
        print(transacao.exibir_resumo())
        print()

    mostra_linha()

    indice_remover = leiaint("Qual transação deseja remover? Passe o ÍNDICE: ")

    removida = carteira.remover_transacao(indice_remover)

    if removida:

        print(f"[green]Transação de ÍNDICE: {indice_remover} removido com sucesso.[/]\n")

    else:

        print(f"[red]ÍNDICE inválido.[/]\n")


def editar_transacao(carteira):

    mostra_linha()

    for indice, transacao in enumerate(carteira.transacoes):
        print(f"[yellow]ÍNDICE: {indice}[/]")
        print(transacao.exibir_resumo())
        print()

    mostra_linha()
        
    indice_editar = leiaint("Qual transação deseja editar? Passe o ÍNDICE: ")

    if 0 <= indice_editar < len(carteira.transacoes):
        
        valor = leia_float("Novo valor: ")
        descricao = str(input("Descrição: "))

        categoria = str(input("Categoria: "))

        atualizado = carteira.editar_transacao(
            indice_editar,
            valor, 
            descricao, 
            categoria
        )

        print("[green]Atualização realizada com sucesso.[/]")

    else:

        print("[red]ÍNDICE inválido.[/]")


def relatorio_financeiro(carteira):

    mostra_linha()

    print()

    relatorio = carteira.gerar_relatorio()

    print(f"[green]Total Receita:[/] R${relatorio['receita']:.2f}")
    print(f"[red]Total Despesas:[/] R${relatorio['despesa']:.2f}")
    print(f"[yellow]Saldo:[/] R${relatorio['saldo']:.2f}")
    print()

def filtrar_transacoes(carteira):

    mostra_linha()

    print(
        f"[blue]1- Filtrar por CATEGORIA"
        f"\n2- Filtrar por TIPO"
        f"\n3- Filtrar por DATA[/]"
    )

    mostra_linha()

    filtro = leiaint("Escollha o filtro: ")

    if filtro == 1:

        mostra_linha()
        
        categoria = str(input("Qual a categoria: "))

        resultado = carteira.filtrar_por_categoria(categoria)

        exibir_transacoes(resultado)


    elif filtro == 2:
        
        mostra_linha()

        print(
            f"[blue]1- Receita"
            f"\n2- Despesa[/]"
        )

        mostra_linha()
        
        tipo_digitado = leiaint("Qual o tipo: ")

        tipos = {
            1: "Receita",
            2: "Despesa"
        }

        tipo = tipos.get(tipo_digitado)

        resultado = carteira.filtrar_por_tipo(tipo)

        exibir_transacoes(resultado)


    elif filtro == 3:
        
        mostra_linha()
        
        data = str(input("Qual a data da transação (dd/mm/aaaa): "))

        resultado = carteira.filtrar_por_data(data)

        exibir_transacoes(resultado)


    else:
        print("[red]Filtro inválido.[/]")
