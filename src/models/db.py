import sqlite3

def criar_db():
    """Cria a tabela de feriados caso ela não exista"""
    conn = sqlite3.connect('database.db')
    # Cria um cursor para executar comanddos SQL
    cursor = conn.cursor()
    # Cria a tabela com data e nome
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feriados (
        data TEXT NOT NULL,
        nome TEXT NOT NULL,
        UNIQUE (data, nome)
        )
    ''')

    conn.commit()
    conn.close()