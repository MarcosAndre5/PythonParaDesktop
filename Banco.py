import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS produtos (
                     nome TEXT,
                     qtd INTEGER,
                     qtdMinima INTEGER,
                     codigo INTEGER)""")

        c.execute("""CREATE TABLE IF NOT EXISTS estoque (
                     codigo INTERGER,
                     nome_interessado TEXT,
                     data DATE,
                     qtd INTEGER,
                     entrada_saida INTEGER)""")
        self.conexao.commit()
        c.close()
