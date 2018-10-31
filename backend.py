import sqlite3 as sql

class BD:
    banco = "clientes.db"
    conexao = None
    cursor = None
    conectado = False

    def conectar(self):
        self.conexao = sql.connect(self.banco)
        self.cursor = self.conexao.cursor()
        self.conectado = True

    def desconectar(self):
        self.conexao.close()
        self.conectado = False

    def executar(self, sql, parametros=None):
        if self.conectado:
            if parametros==None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, parametros)
            return True
        else:
            return False

    def fetchall(self):
        return self.cursor.fetchall()

    def persistir(self):
        if self.conectado:
            self.conexao.commit()
            return True
        else:
            return False

def listar():
    bd = BD()
    bd.conectar()

    bd.executar("SELECT * FROM clientes")
    linhas = bd.fetchall()

    bd.desconectar()
    return linhas


def inserir(nome, sobrenome, email, cpf):
    bd = BD()
    bd.conectar()

    bd.executar("INSERT INTO clientes VALUES(NULL,?,?,?,?)", (nome, sobrenome, email, cpf))

    bd.persistir()
    bd.desconectar()


def buscar(name='', lastname='', email='', cpf=''):
    bd = BD()
    bd.conectar()

    bd.executar("SELECT * FROM client WHERE nome={} or sobrenome={} or email={} or cpf={}".format(name, lastname, email, cpf))
    linhas = bd.fetchall()
    bd.desconectar()

def atualizar(id, nome, sobrenome, email, cpf):
    bd = BD()
    bd.conectar()
    bd.executar("UPDATE clientes SET nome={}, sobrenome={}, email={}, cpf={}".format(nome, sobrenome, email, cpf))
    bd.persistir()
    bd.desconectar()

def apagar(id):
    bd = BD()
    bd.conectar()
    bd.executar("DELETE FROM clientes WHERE id={}".format(id))
    bd.persistir()
    bd.desconectar()

def inicializar_bd():
    bd = BD()
    bd.conectar()
    bd.executar("CREATE TABLE IF NOT EXISTS clientes (id INTERGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    bd.persistir()
    bd.desconectar()

    #Inicializar
    inicializar_bd()
