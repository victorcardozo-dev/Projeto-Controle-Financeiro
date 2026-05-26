from database.connection import conectar


def inserir_transacao(transacao):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO transacoes(
            id,
            tipo,
            valor,
            descricao,
            categoria,
            data
        )

        VALUES(?, ?, ?, ?, ?, ?)  
    """, (

        transacao.id,
        transacao.__class__.__name__,
        transacao.valor,
        transacao.descricao,
        transacao.categoria,
        transacao.data

    ))

    conexao.commit()

    conexao.close()


def listar_trasacoes():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM transacoes
    """)

    dados = cursor.fetchall()

    conexao.close()

    return dados


def deletar_transacao(id_transacao):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM transacoes
        WHERE id = ?
    """, (id_transacao,))

    conexao.commit()

    conexao.close()


def atualizar_transacao(transacao):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE transacoes
        SET 
            valor = ?,
            descricao = ?,
            categoria = ?
                   
        WHERE id = ?
    """, (

        transacao.valor,
        transacao.descricao,
        transacao.categoria,
        transacao.id

    ))

    conexao.commit()

    conexao.close()