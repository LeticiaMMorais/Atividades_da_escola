from ClasseAutomovel import Automovel

def Caminhao(Automovel):
    def __init__(self, nome:str, cor:str , qntRodas:int , tipoCombustivel:str, pesoSuportadoKG: int, comprimento: float):
        Automovel.__init__(nome, cor, qntRodas, tipoCombustivel)
        self.pesoSuportado = pesoSuportadoKG
        self.comprimento = comprimento

    def ligar(self):
        print(f'O {self.nome} ligou: FOM FOM!!')

    def despejarCarga(self, lugar:str):
        print('O {} está despejando a carga em {}.'.format(self.nome, lugar))

    def pegarCarga(self, lugar:str, material:str):
        print('O {} está pegando uma carga de {} em {}.'.format(self.nome, material, lugar))