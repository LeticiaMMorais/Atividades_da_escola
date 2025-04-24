from Pessoa1 import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome:str, cpf:str, cadastro:str, cupom: bool = False):
        super().__init__(nome, cpf)
        self.__cadastro = cadastro
        self.__cupom = cupom

    def getCupom(self):
        if self.__cupom:
            print(f'Sim, o cliente {self._nome} tem um cupom.')
        else:
            print(f'Não, o cliente {self._nome} não tem um cupom.')

    def getInfo(self):
        print(f'Cliente: {self._nome}\nCPF: {self._cpf}\nCadastro: {self.__cadastro}')

    def falar(self):
        print('Oi, gostaria de comprar algo.')