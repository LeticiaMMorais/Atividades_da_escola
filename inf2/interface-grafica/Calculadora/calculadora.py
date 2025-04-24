from tkinter import *

class Janela:
    def __init__(self, mestre):
        self.c1 = Frame(mestre)
        self.c1["padx"] = 100 
        self.c1["pady"] = 10 
        self.c1.pack()
        self.t1 = Label(self.c1, text="Calculadora")
        self.t1["font"] = ('Arial', '10', 'bold')
        self.t1.pack()

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
        self.botao1 = Button(self.c4, text='somar')
        self.botao1['command'] = self.somar
        self.botao1.pack(side=LEFT)

        self.botao2 = Button(self.c4, text='subtrair')
        self.botao2['command'] = self.subtrair
        self.botao2.pack(side=RIGHT)

        self.c5 = Frame(mestre)
        self.c5.pack()
        self.botao3 = Button(self.c5, text='multiplicar')
        self.botao3['command'] = self.multiplicar
        self.botao3.pack(side=LEFT)

        self.botao4 = Button(self.c5, text='dividir')
        self.botao4['command'] = self.dividir
        self.botao4.pack(side=RIGHT)

        self.c6 = Frame(mestre)
        self.c6['pady'] = 15
        self.c6.pack()
        self.mensagem = Label(self.c6, text='')
        self.mensagem['pady'] = 10
        self.mensagem.pack()

    def somar(self):
        a = int(self.l2.get())
        b = int(self.l3.get())
        resultado = a + b
        self.mensagem["text"] = "A+B = "+str(resultado)
    
    def subtrair(self):
        a = int(self.l2.get())
        b = int(self.l3.get())
        resultado = a - b
        self.mensagem["text"] = "A-B = "+str(resultado)
    
    def multiplicar(self):
        a = int(self.l2.get())
        b = int(self.l3.get())
        resultado = a * b
        self.mensagem["text"] = "A*B = "+str(resultado)
    
    def dividir(self):
        a = int(self.l2.get())
        b = int(self.l3.get())
        resultado = a / b
        self.mensagem["text"] = "A/B = "+str(resultado)

raiz = Tk()
Janela(raiz)
raiz.mainloop()