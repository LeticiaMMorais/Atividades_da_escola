from tkinter import *
class Application:
    def __init__(self, master=None):
        self.top = Toplevel()
        self.top.title("janela 2")
        self.widget1 = Frame(self.top)
        self.widget1["padx"] = 100
        self.widget1["pady"] = 10
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Outra janela")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["command"] = self.top.destroy
        self.sair.pack()