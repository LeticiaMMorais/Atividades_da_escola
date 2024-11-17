class Animal():
    def __init__ (self, Nome: str, Cor: str, Idade: int):
        self.Nome = Nome
        self._Cor = Cor
        self._Idade = Idade
    
    def _latir(self):
        return f'{self.Nome} diz: AU AU!'
    
    def comer(self, qnt: int, nomeRação: str):
        print(F'{self.Nome} está comendo {qnt}g de {nomeRação}.')