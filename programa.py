from Produtos import *
from tkinter import *

class Application:
    def __init__(self, master=None):
        root.title('Sistema de Estoque')
        root.geometry('1300x690+0+0')

        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Produtos", menu=filemenu)
        filemenu.add_command(label="Cadastrar Novo", command=self.cadastrar)
        filemenu.add_command(label="Saida de Produtos",)
        filemenu.add_command(label="Entrada de Produtos",)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=root.quit)

    def cadastrar(self):
        janela = Tk()
        janela.title('Cadastrar')
        janela.geometry('500x250+0+50')
        nome = Label(janela, text='Nome: ')
        self.nomeProd = Entry(janela)
        self.qtdNovo = Label(janela, text='Quantidade Comprada: ')
        self.qtdNovoProd = Entry(janela)
        self.qtdMinima = Label(janela, text='Quantidade Mínima no estoque: ')
        self.qtdMinimaProd = Entry(janela)
        cadastrar = Button(janela, text='Cadastrar', command=self.inserirProduto)
        voltar = Button(janela, text='Voltar', command=janela.destroy)
        self.status = Label(janela, text='')
        nome.grid(row=0, column=0, pady=10)
        self.nomeProd.grid(row=0, column=1)
        self.qtdNovo.grid(row=1, column=0, pady=10)
        self.qtdNovoProd.grid(row=1, column=1)
        self.qtdMinima.grid(row=2, column=0, pady=10)
        self.qtdMinimaProd.grid(row=2, column=1)
        cadastrar.grid(row=3, column=1, pady=10)
        voltar.grid(row=3, column=2, pady=10)
        self.status.grid(row=4, column=2, pady=10)

    def inserirProduto(self):
        prod = Produtos()
        prod.nome = self.nomeProd.get()
        prod.qtd = self.qtdNovoProd.get()
        prod.qtdMinima = self.qtdMinimaProd.get()
        self.status["text"] = prod.insertProd()

        self.nomeProd.delete(0, END)
        self.qtdNovoProd.delete(0, END)
        self.qtdMinimaProd.delete(0, END)

root = Tk()
Application(root)
root.mainloop()
