# -*- coding:UTF-8 -*-
from tkinter import *

class Sistema:
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

    def ChecarLogin(self):
        login = ''
        senha = ''
        if self.entradaUsuario.get() == login and self.entradaSenha.get() == senha:
            self.JanelaPrincipal()
            self.status['text'] = 'Logado'
            self.status['bg'] = 'green'
        else:
            self.status['text'] = 'Dados Inválidos'
            self.status['bg'] = 'red'

    def JanelaPrincipal(self):
        self.jan = Tk()

        self.jan.title('Sistema de Estoque')
        self.menu1 = Button(self.jan, text='Cadastrar Produto', command=self.Cadastrar)
        self.menu2 = Button(self.jan, text='Saída de Produto')
        self.menu3 = Button(self.jan, text='Estoque')
        self.sair = Button(self.jan, text='Sair do Sistema', command=self.sair)

        self.menu1.grid(row=0, column=0)
        self.menu2.grid(row=0, column=1)
        self.menu3.grid(row=0, column=2)
        self.sair.grid(row=0, column=3)

        self.jan.geometry('1000x500+0+0')

    def sair(self):
        exit()

    def cadastrarProd(self):
        self.nomeCadastrada['text'] = self.nomeProd.get()
        self.qtdNovoCadastrada['text'] = self.qtdNovoProd.get()
        self.qtdMinimaCadastrada['text'] = self.qtdMinimaProd.get()

    def Cadastrar(self):
        self.jan = Tk()
        self.jan.title('Cadastrar')
        self.nome = Label(self.jan, text='Nome: ')
        self.nomeProd = Entry(self.jan)
        self.qtdNovo = Label(self.jan, text='Quantidade Comprada: ')
        self.qtdNovoProd = Entry(self.jan)
        self.qtdMinima = Label(self.jan, text='Quantidade Mínima no estoque: ')
        self.qtdMinimaProd = Entry(self.jan)
        self.cadastrar = Button(self.jan, text='Cadastrar', command=self.cadastrarProd)

        self.nomeCadastrada = Label(self.jan, text='')
        self.qtdNovoCadastrada = Label(self.jan, text='')
        self.qtdMinimaCadastrada = Label(self.jan, text='')

        self.nome.grid(row=0, column=0, pady=10)
        self.nomeProd.grid(row=0, column=1)
        self.qtdNovo.grid(row=1, column=0, pady=10)
        self.qtdNovoProd.grid(row=1, column=1)
        self.qtdMinima.grid(row=2, column=0, pady=10)
        self.qtdMinimaProd.grid(row=2, column=1)
        self.cadastrar.grid(row=3, column=1, pady=10)

        self.nomeCadastrada.grid(row=4, column=0)
        self.qtdNovoCadastrada.grid(row=4, column=1)
        self.qtdMinimaCadastrada.grid(row=4, column=2)

        self.jan.geometry('1000x500+0+0')

root = Tk()
Sistema(root)
root.geometry('300x200')
root.mainloop()
Sistema()
