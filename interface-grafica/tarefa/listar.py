from tkinter import *
import gerenciadordearquivos as ga

class Listar:
    def __init__(self,mestre=None):
        self.top = Toplevel()
        self.top.title("Janela de \"listagem\"")
        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()

        self.t1 = Label(self.widget1, text='Lista')
        self.t1['font'] = ('Arial', '12')
        self.t1.pack()

        self.c2 = Frame(self.top)
        self.c2['pady'] = 10
        self.c2.pack()
        pessoas = ga.ler()
        for num in range(len(pessoas)):
            self.message = Entry(self.c2) #dessa vez, vamos mostrar uma informação e não obter com Entry
            self.message['fg'] = 'black' #mudando a cor do texto
            self.message['font'] = ('Arial', '10', 'italic') #mudando a fonte
            self.message.grid(row=num, column=0)
            self.message.insert(END, pessoas[num]) #Aqui você primeiro coloca a posição em que o elemento será inserido depois a string.
        
        self.espaco = Label(self.c2, text=' ')
        self.espaco['pady'] = 10
        self.espaco.pack()