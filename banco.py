import sqlite3
import os

CAMINHO_DB = os.path.join(os.path.dirname(__file__), "modulos.db")

def conectar():
    return sqlite3.connect(CAMINHO_DB)

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

def cadastrar_modulo(rotulo, tipo, prioridade, criticidade, integridade, detalhes):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO modulos
        (rotulo, tipo, prioridade, criticidade, integridade, detalhes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        rotulo,
        tipo,
        prioridade,
        criticidade,
        integridade,
        detalhes
    ))

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