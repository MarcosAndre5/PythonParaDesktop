from tkinter import *

class Sistema:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)
        self.menuSistema = Menu(self.menu)

        self.menuSistema.add_command(label='Cadastrar Produto')
        self.menu.add_cascade(label='Cadastro', menu=self.menuSistema.login)
        master.config(menu=self.menu)


janela = Tk()
janela.title('Sistema de Estoque')
Sistema(janela)
janela.geometry('500x500')
janela.mainloop()
