from abc import ABC, abstractmethod

# 2. Interface
class CarroEletrico():
    @abstractmethod
    def carregarBateria(self):
        '''Esse método deve definir o carregamento da bateria do carro.'''
        pass