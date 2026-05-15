# Função para ler um número inteiro e mostrar uma linha

from rich import print

def leiaint(msg):
  while True:
      try:
          n = int(input(msg))
      except(ValueError, TypeError):
          print("[red]ERRO: Por favor digite uma número inteiro válido: [/]")
          continue
      except(KeyboardInterrupt):
          print("[red]O usuário preferiu não digitar o valor![/]")
          return 0
      else:
          return n


def leia_float(msg):
      while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("[red]ERRO: Por favor digite uma número válido: [/]")
            continue
        except(KeyboardInterrupt):
            print("[red]O usuário preferiu não digitar o valor![/]")
            return 0
        else:
            return n


def mostra_linha():
    print("-" * 60)