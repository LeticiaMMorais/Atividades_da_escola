from tkinter import messagebox

def ler(narquivo='pessoa.txt'):
    with open(narquivo, 'r') as arquivo:
        lista = arquivo.readlines()
    arquivo.close()
    messagebox.showinfo('Aviso', message='Informações carregadas com sucesso!')
    return lista

def adicionar(infonova, narquivo='pessoa.txt'):
    with open(narquivo, 'a') as arquivo:
        arquivo.write(str(infonova)+'\n')
    arquivo.close()
    messagebox.showinfo('Aviso', message='Informações adicionadas no arquivo!')