# Abstract Base Classes
from abc import ABC, abstractmethod

# 1. Classe Abstrata:
class Veiculo():
    def informarVelocidade(self, velocidade: int):
        return f'A velocidade é de {velocidade} km/h'
    
    def pressaoDosPneus(self, pressaoPneus: int):
        return f'A pressão dos pneus é de {pressaoPneus} libras.'
    
    @abstractmethod #Indicando que o método é abstrato.
    def ligarMotor(self):
        '''Esse método define como o motor é ligado.'''
        pass

    @abstractmethod
    def desligarMotor(self):
        '''Esse método define como o motor é desligado.'''
        pass




