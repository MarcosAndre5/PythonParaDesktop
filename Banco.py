import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists produtos (
                     idproduto integer primary key autoincrement ,
                     nome text,
                     qtd text,
                     qtdMinima text)""")
        self.conexao.commit()
        c.close()

