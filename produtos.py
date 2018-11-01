from Banco import Banco

class Produtos(object):
    def __init__(self, idproduto=0, nome='', qtd='', qtdminima=''):
        self.info = {}
        self.idproduto = idproduto
        self.nome = nome
        self.qtd = qtd
        self.qtdminima = qtdminima


    def insertProd(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (nome, qtd, qtdminima) values ('" + self.nome + "', '" + self.qtd + "', '" + self.qtdminima + "' )")
            banco.conexao.commit()
            c.close()
            return "Produto cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do produto!"

    '''def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from usuarios where idusuario = " + idusuario + "  ")
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
'''
