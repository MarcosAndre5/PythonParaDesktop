from Banco import Banco

class Produtos(object):
    def __init__(self, idproduto=0, nome="", qtd="", qtdMinima=""):
        self.info = {}
        self.idproduto = idproduto
        self.nome = nome
        self.qtd = qtd
        self.qtdMinima = qtdMinima

    def insertProd(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into produtos (nome, qtd, qtdMinima) values ('" + self.nome + "', '" + self.qtd + "', '" + self.qtdMinima + "' )")
            banco.conexao.commit()
            c.close()
            return "Produto cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do produto"
