from tkinter import *

class GUI:
    def janela(self):
        janela = Tk()
        janela.title("Cadastro de Clientes")

        # Dados texto
        txt_nome = StringVar()
        txt_sobrenome = StringVar()
        txt_email = StringVar()
        txt_cpf = StringVar()

        # Labels
        lbl_nome = Label(janela, text="Nome")
        lbl_sobrenome = Label(janela, text="Sobrenome")
        lbl_email = Label(janela, text="Email")
        lbl_cpf = Label(janela, text="CPF")

        #Entries
        ent_nome = Entry(janela, textvariable=txt_nome)
        ent_sobrenome = Entry(janela, textvariable=txt_sobrenome)
        ent_email = Entry(janela, textvariable=txt_email)
        ent_cpf = Entry(janela, textvariable=txt_cpf)

        #Lista de clientes
        list_clientes = Listbox(janela)
        scroll_clientes = Scrollbar(janela)

        #Botões
        btn_listar = Button(janela, text="Listar")
        btn_buscar = Button(janela, text="Buscar")
        btn_inserir = Button(janela, text="Inserir")
        btn_atualizar = Button(janela, text="Atualizar")
        btn_apagar = Button(janela, text="Apagar")
        btn_fechar = Button(janela, text="Fechar")

        # Posicionando as coisas na janela
        lbl_nome.grid(row=0, column=0)
        lbl_sobrenome.grid(row=1, column=0)
        lbl_email.grid(row=2, column=0)
        lbl_cpf.grid(row=3, column=0)

        ent_nome.grid(row=0, column=1, padx=50, pady=50)
        ent_sobrenome.grid(row=1, column=1)
        ent_email.grid(row=2, column=1)
        ent_cpf.grid(row=3, column=1)

        list_clientes.grid(row=0, column=2, rowspan=10)
        scroll_clientes.grid(row=0, column=6, rowspan=10)

        btn_listar.grid(row=4, column=0, columnspan=2)
        btn_buscar.grid(row=5, column=0, columnspan=2)
        btn_inserir.grid(row=6, column=0, columnspan=2)
        btn_atualizar.grid(row=7, column=0, columnspan=2)
        btn_apagar.grid(row=8, column=0, columnspan=2)
        btn_fechar.grid(row=9, column=0, columnspan=2)

        #Ajustando o posicionamento
        x_pad = 5
        y_pad = 3
        width_entry = 30

        for child in janela.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky="WE", padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)
            elif widget_class == "Scrollbar":
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)
            else:
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)


        def run(self):
            self.janela.mainloop()
