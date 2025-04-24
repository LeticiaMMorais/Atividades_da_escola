from tkinter import *
from teladeacesso import Application

class Janela:
    def __init__(self, mestre):
        raiz.title("janela")
        self.c1 = Frame(mestre)
        self.c1['padx'] = 100
        self.c1['pady'] = 10
        self.c1.pack()
        self.titulo = Label(self.c1, text='Dados do Usuário')
        self.titulo["font"] = ("Arial", '10', 'bold')
        self.titulo.pack()

        self.c2 = Frame(mestre)
        self.c2.pack()
        self.t2 = Label(self.c2, text='Nome')
        self.t2.pack(side=LEFT)
        self.l2 = Entry(self.c2)
        self.l2.pack(side=LEFT)

        self.c3 = Frame(mestre)
        self.c3.pack()
        self.t3 = Label(self.c3, text="Senha")
        self.t3.pack(side=LEFT)
        self.l3 = Entry(self.c3)
        self.l3['show'] = '*'
        self.l3.pack(side=LEFT)

        self.c4 = Frame(mestre)
        self.c4.pack()
        self.botao = Button(self.c4, text='autenticar')
        self.botao["command"] = self.autenticar
        self.botao.pack()

        self.mensagem = Label(self.c4, text="")
        self.mensagem.pack()

    def autenticar(self):
        nome = self.l2.get()
        senha = self.l3.get()
        if nome == "ciro" and senha == "123":
            self.mensagem["text"] = "sucesso!"
            Application()
        else:
            self.mensagem["text"] = "erro!"

raiz = Tk()
Janela(raiz)
raiz.mainloop()