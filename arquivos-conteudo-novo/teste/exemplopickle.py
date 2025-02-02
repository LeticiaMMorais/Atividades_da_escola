'''import pickle

class Pessoa():
    def __init__(self):
        self.nome = 'Ciro'
        self.felicidade = 0

p = Pessoa()
arquivo = open('serializacao.txt','wb')
pickle.dump(p, arquivo)

arquivo = open('serializacao.txt','rb')
retorno = pickle.load(arquivo)

print(retorno.nome)
'''


'''Modifique o código do exemplo anterior para
que sejam salvos vários objetos Pessoa ao
invés de apenas um.'''

import pickle

class Pessoa():
    def __init__(self, nome):
        self.nome = nome
        self.felicidade = 0

pessoas = []
a = Pessoa('Ciro')
b = Pessoa('Caio')
c = Pessoa('Guilherme')
pessoas.extend([a,b,c])

arquivo = open('serializacao.txt','wb')
for pessoa in pessoas:
    pickle.dump(pessoa, arquivo)

arquivo = open('serializacao.txt','rb')
for num in range(len(pessoas)):
    retorno = pickle.load(arquivo)
    print(retorno.nome)


