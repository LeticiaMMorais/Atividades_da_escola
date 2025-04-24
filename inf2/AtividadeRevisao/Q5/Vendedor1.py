from Pessoa1 import Pessoa

class Vendedor(Pessoa):
    def __init__(self, nome:str, cpf:str, identificacao:str):
        super().__init__(nome, cpf)
        self.__identificacao = identificacao

    def falar(self):
        print('Olá, está tudo certo aí? Nós temos produtos exclusivos, gostaria de dar uma olhada?')

    def getInfo(self):
        print(f'Vendedor: {self._nome}\nCPF: {self._cpf}\nIdentificação: {self.__identificacao}')

    def atenderPag(self):
        print('Gostaria de pagar no cartão? Débito ou Crédito?')
    
