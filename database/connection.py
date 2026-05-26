import sqlite3

def conectar():

    conexao = sqlite3.connect("database/financeiro.db")

    return conexao