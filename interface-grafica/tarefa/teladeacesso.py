from tkinter import *
import pickle
from listar import Listar
from cadastrar import Cadastrar

class Application:
    def __init__(self, mestre=None):
        self.top = Toplevel()
        self.top.title('Janela de acesso')
        self.c1 = Frame(self.top)
        self.c1['padx'] = 100
        self.c1['pady'] = 10
        self.c1.pack()
        self.titulo = Label(self.c1, text='Fazer cadastro ou listar pessoas?')
        self.titulo["font"] = ("Arial", '16', 'bold')
        self.titulo['fg'] = 'orange'
        self.titulo.pack()

        self.c2 = Frame(self.top)
        self.c2['padx'] = 100
        self.c2['pady'] = 10
        self.c2.pack()
        self.botao1 = Button(self.c2, text='Listar')
        self.botao1['command'] = self.listar
        self.botao1.pack(side=LEFT)
        self.botao2 = Button(self.c2, text='Cadastrar')
        self.botao2['command'] = self.cadastrar
        self.botao2.pack(side=RIGHT)

        self.nomeArquivo = 'pessoas.txt'

    def listar(self):
        Listar()

    def cadastrar(self):
        Cadastrar()


