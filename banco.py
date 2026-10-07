import sqlite3

def conectar():
    return sqlite3.connect("modulos.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS modulos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rotulo TEXT NOT NULL UNIQUE,
        tipo TEXT NOT NULL,
        prioridade INTEGER NOT NULL,
        criticidade INTEGER NOT NULL,
        integridade BOOLEAN NOT NULL,
        detalhes TEXT
    )
""")

    conexao.commit()
    conexao.close()

def listar_modulos_db():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
            SELECT rotulo, tipo, prioridade, criticidade, integridade, detalhes
            FROM modulos
        """)

    modulos_db = cursor.fetchall()

    conexao.close()
    return modulos_db