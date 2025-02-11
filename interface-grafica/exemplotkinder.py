from tkinter import *

class Janela:
    def __init__(self, mestre):
        self.c1 = Frame(mestre)
        self.c1["padx"] = 100 # dá espaçamento dos dois lados horizontal (apenas para esse objeto somar.)
        self.c1["pady"] = 20 # dá espaçamento vertical.
        '''padding é o espaçamento de um elemento. A parte externa da área é a margem e a parte interna é o padding.'''
        self.c1.pack()
        self.titulo = Label(self.c1, text="Somar")
        self.titulo["font"] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.c2 = Frame(mestre)
        self.c2.pack()
        self.t2 = Label(self.c2, text='A')
        self.t2.pack(side=LEFT)
        self.l2 = Entry(self.c2)
        self.l2.pack(side=LEFT)

        self.c3 = Frame(mestre)
        self.c3.pack()
        self.t3 = Label(self.c3,text='B')
        self.t3.pack(side=LEFT)
        self.l3 = Entry(self.c3)
        self.l3.pack(side=LEFT)

        self.c4 = Frame(mestre)
        self.c4.pack()
        self.botao = Button(self.c4, text='somar')
        self.botao['command'] = self.somar
        self.botao.pack()

        self.mensagem = Label(self.c4, text='')
        self.mensagem['pady'] = 10
        self.mensagem.pack()

    def somar(self):
        a = int(self.l2.get())
        b = int(self.l3.get())
        resultado = a + b
        self.mensagem["text"] = "A+B = "+str(resultado)

raiz = Tk()
Janela(raiz)
raiz.mainloop()