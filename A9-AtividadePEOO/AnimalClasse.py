class Animal():
    def __init__ (self, Nome = '', Cor = '', Idade = 0):
        self.Nome = Nome
        self._Cor = Cor
        self._Idade = Idade
    
    def _latir(self):
        return f'{self.Nome} diz: AU AU!'
    
    def comer(self, qnt=0, nomeRação=''):
        print(F'{self.Nome} está comendo {qnt}g de {nomeRação}.')