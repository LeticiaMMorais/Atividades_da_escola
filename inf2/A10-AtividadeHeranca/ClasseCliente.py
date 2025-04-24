from SuperclassePessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nomep, cpfp, enderecop, limitecomprap):
        Pessoa.__init__(self, nomep, cpfp, enderecop)
        self.__limitecompra = limitecomprap
    
    def getLimite(self):
        print('Limite: ',self.__limitecompra)
    
    def falar(self):
        print("Olá! Gostaria de realizar uma compra.")