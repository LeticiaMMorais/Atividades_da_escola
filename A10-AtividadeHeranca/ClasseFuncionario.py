from SuperclassePessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nomep, cpfp, enderecop, cargop, salariop):
        Pessoa.__init__(self, nomep, cpfp, enderecop)
        self.__cargo = cargop
        self.__salario = salariop

    def getCargo(self):
        print('Cargo: '+self.__cargo)

    def falar(self):
        print('Olá! Como posso ajudar?')