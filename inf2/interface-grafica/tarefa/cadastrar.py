from tkinter import *
import gerenciadordearquivos as ga

class Cadastrar:
    def __init__(self, master=None):
        self.top = Toplevel()
        self.top.title("Janela de cadastro")
        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()

        self.t1 = Label(self.widget1, text='Cadastre uma pessoa:')
        self.t1.pack()

        self.t2 = Label(self.widget1, text='Nome: ')
        self.t2.pack(side=LEFT)
        self.e1 = Entry(self.widget1)
        self.e1.pack(side=LEFT)
        
        self.w2 = Frame(self.top)
        self.w2.pack()
        self.botao = Button(self.w2, text='Salvar')
        self.botao['command'] = self.adicionar
        self.botao.pack()

    def adicionar(self):
        ga.adicionar(self.e1.get())
