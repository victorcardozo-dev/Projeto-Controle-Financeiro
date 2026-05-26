from database.connection import conectar

def criar_tabela():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (

            id TEXT PRIMARY KEY,
            tipo TEXT, 
            valor REAL,
            descricao TEXT,
            categoria TEXT, 
            data TEXT       
                   
        )

    """)

    conexao.commit()

    conexao.close()