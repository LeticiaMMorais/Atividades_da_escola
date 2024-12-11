class Pessoa():
    def __init__ (self, nome:str = '', cpf:str = ''):
        self._nome = nome
        self._cpf = cpf

    def verProduto(self, produtoBuscado:str):
        print(f'Alguém ({self._nome}) está procurando por {produtoBuscado}.')

    def falar(self):
        print('Olá!')

