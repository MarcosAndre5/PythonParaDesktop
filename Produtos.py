from Banco import Banco

class Produtos(object):
    def __init__(self, idproduto=0, nome='', nomeNovo='', qtd='', qtdMinima='', codigo=''):
        self.info = {}
        self.idproduto = idproduto
        self.nome = nome
        self.nomeNovo = nomeNovo
        self.qtd = qtd
        self.qtdMinima = qtdMinima
        self.codigo = codigo

    def insertProd(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO produtos (nome, qtd, qtdMinima, codigo) VALUES ('" + self.nome + "', '" + self.qtd + "', '" + self.qtdMinima + "', '" + self.codigo + "' )")
            banco.conexao.commit()
            c.close()
            return 'Produto cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do produto.'

    def updateProd(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE produtos SET nome = '" + self.nome + "', qtd = '" + self.qtd + "', qtdMinima = '" + self.qtdMinima + "' where codigo = " + self.codigo + " ")
            banco.conexao.commit()
            c.close()
            return 'Produto atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do produto.'

    def deleteProd(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM produtos WHERE codigo = '" + self.codigo + "' ")
            banco.conexao.commit()
            c.close()
            return 'Produto excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do produto.'

    def selectProd(self, codigo):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM produtos WHERE codigo = '" + codigo + "'  ")
            for linha in c:
                self.nome = linha[0]
                self.qtd = linha[1]
                self.qtdMinima = linha[2]
            c.close()
            return 'Busca feita com sucesso!'
        except:
            return 'Ocorreu um erro na busca do produto.'
