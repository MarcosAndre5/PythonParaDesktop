# -*- coding:UTF-8 -*-
from tkinter import *
from frontend import *

class Sistema:
    #####################
    # Telas do Sistema
    #####################
    def __init__(self, janela):
        self.jan = None
        self.caixa = Frame(janela)
        self.caixa.grid()

        janela.title('Tela de Login')
        self.titulo = Label(janela, text='Tela de Login do Sistema')
        self.usuario = Label(janela, text='Login: ')
        self.senha = Label(janela, text='Senha: ')
        self.entradaUsuario = Entry(janela)
        self.entradaSenha = Entry(janela, show='*')
        self.entrar = Button(janela, text='Entrar', command=self.ChecarLogin)
        self.status = Label(janela, text='')

        self.titulo.grid(row=0, column=1, pady=10)
        self.usuario.grid(row=1, column=0)
        self.senha.grid(row=2, column=0)
        self.entradaUsuario.grid(row=1, column=1, pady=10)
        self.entradaSenha.grid(row=2, column=1, pady=10)
        self.entrar.grid(row=3, column=1)
        self.status.grid(row=4, column=1, pady=20)

    def JanelaPrincipal(self):
        janela = Tk()
        janela.title('Sistema de Estoque')
        menu = Menu(janela)
        janela.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Produtos", menu=filemenu)
        filemenu.add_command(label="Cadastrar Novo", command=self.Cadastrar)
        filemenu.add_command(label="Saida de Produtos",)
        filemenu.add_command(label="Entrada de Produtos",)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        janela.geometry('1000x500+0+0')

    def Cadastrar(self):
        janela = Tk()
        janela.title('Cadastrar')
        nome = Label(janela, text='Nome: ')
        nomeProd = Entry(janela)
        qtdNovo = Label(janela, text='Quantidade Comprada: ')
        qtdNovoProd = Entry(janela)
        qtdMinima = Label(janela, text='Quantidade Mínima no estoque: ')
        qtdMinimaProd = Entry(janela)
        cadastrar = Button(janela, text='Cadastrar', command=self.cadastrarProd)
        voltar = Button(janela, text='Voltar', command=janela.destroy)

        nomeCadastrada = Label(janela, text='')
        qtdNovoCadastrada = Label(janela, text='')
        qtdMinimaCadastrada = Label(janela, text='')

        nome.grid(row=0, column=0, pady=10)
        nomeProd.grid(row=0, column=1)
        qtdNovo.grid(row=1, column=0, pady=10)
        qtdNovoProd.grid(row=1, column=1)
        qtdMinima.grid(row=2, column=0, pady=10)
        qtdMinimaProd.grid(row=2, column=1)
        cadastrar.grid(row=3, column=1, pady=10)
        voltar.grid(row=3, column=2, pady=10)

        nomeCadastrada.grid(row=4, column=0)
        qtdNovoCadastrada.grid(row=4, column=1)
        qtdMinimaCadastrada.grid(row=4, column=2)

        janela.geometry('1000x500+0+0')

    #####################
    # Funções do Sistema
    #####################
    def ChecarLogin(self):
        login = ''
        senha = ''
        if self.entradaUsuario.get() == login and self.entradaSenha.get() == senha:
            self.JanelaPrincipal()
            self.caixa.destroy()

            self.status['text'] = 'Logado'
            self.status['bg'] = 'green'
        else:
            self.status['text'] = 'Dados Inválidos'
            self.status['bg'] = 'red'

    def cadastrarProd(self):
        self.nomeCadastrada['text'] = self.nomeProd.get()
        self.qtdNovoCadastrada['text'] = self.qtdNovoProd.get()
        self.qtdMinimaCadastrada['text'] = self.qtdMinimaProd.get()


root = Tk()
Sistema(root)
root.geometry('300x200')
root.mainloop()
