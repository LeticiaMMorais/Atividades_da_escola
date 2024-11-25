#Importando a classe Veiculo e interface CarroEletrico
from ClasseAbstrataVeiculo import Veiculo
from InterfaceCarroEletrico import CarroEletrico

#Quais características da marca podem ser implementadas?
class Tesla(Veiculo, CarroEletrico):
    cor = ''
    velocidade = 0
    _pressaoPneu = 30
    _bateriaDoCarro = 0
