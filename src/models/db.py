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

def inserir_feriado(lista_feriado):
    """Insere uma lista de dicionários ao database.db"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT OR IGNORE INTO feriados (data, nome)
        VALUES (:date, :name)
    ''', lista_feriado)

    conn.commit()
    print('Sucesso: novos feriados adicionados ao banco de dados. ')
    conn.close()

def visualizar_tabela():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM feriados ORDER BY data;')

    linhas = cursor.fetchall()

    for linha in linhas:
        print(linha)

    conn.close()
    