class Automovel():
    def __init__(self, nome:str, cor:str , qntRodas:int , tipoCombustivel:str):
        self.nome = nome
        self.cor = cor
        self.rodas = qntRodas
        self.combustivel = tipoCombustivel
    
    def ligar(self):
        print(f'O {self.nome} foi ligado.')
    
    def acelerar(self):
        print(f'O {self.nome} está acelerando.')
    
    def frear(self):
        print(f'O {self.nome} está freando.')

    def desligar(self):
        print(f'O {self.nome} foi desligado.')