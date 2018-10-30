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
        self.entrar = Button(janela, text='Entrar', command=self.checar)
        self.status = Label(janela, text='')

        self.titulo.grid(row=0, column=1, pady=10)
        self.usuario.grid(row=1, column=0)
        self.senha.grid(row=2, column=0)
        self.entradaUsuario.grid(row=1, column=1, pady=10)
        self.entradaSenha.grid(row=2, column=1, pady=10)
        self.entrar.grid(row=3, column=1)
        self.status.grid(row=4, column=1, pady=20)

    def checar(self):
        login = 'marcos'
        senha = '1'
        if self.entradaUsuario.get() == login and self.entradaSenha.get() == senha:
            self.JanelaPrincipal()
            self.status['text'] = 'Logado'
            self.status['bg'] = 'green'
        else:
            self.status['text'] = 'Dados Inválidos'
            self.status['bg'] = 'red'

    def JanelaPrincipal(self):
        # Verifica se já foi criada
        if self.jan is None:
            self.jan = Tk()
            self.jan.title('ok')
            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_jan)
            self.l = Label(self.jan, text='Janela sistema')
            self.l.grid()
            self.jan.geometry('1000x500+0+0')
        else:
            # Se já foi, basta colocá-la na frente
            self.jan.lift()

    def fecha_jan(self):
        # Seta de novo em None para recriar quando abrir
        self.jan.destroy()
        self.jan = None


root = Tk()

Sistema(root)
root.geometry('300x200')

root.mainloop()
Sistema()
