class Automovel():
    def __init__(self, nome:str, cor:str , qntRodas:int , tipoCombustivel:str):
        self.nome = nome
        self.cor = cor
        self._rodas = qntRodas
        self._combustivel = tipoCombustivel
    
    def ligar(self):
        print(f'O {self.nome} foi ligado.')
    
    def acelerar(self):
        print(f'O {self.nome} está acelerando.')
    
    def frear(self):
        print(f'O {self.nome} está freando.')

    def desligar(self):
        print(f'O {self.nome} foi desligado.')

    def getDados(self):
        print(f'Nome: {self.nome}\nCor: {self.cor}\nTotal de rodas: {self._rodas}\nTipo de combustível: {self._combustivel}.')