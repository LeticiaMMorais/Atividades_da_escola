from ClasseAutomovel import Automovel

def Caminhao(Automovel):
    def __init__(self, nome:str, cor:str , qntRodas:int , tipoCombustivel:str, pesoSuportadoKG: int, comprimento: float):
        Automovel.__init__(nome, cor, qntRodas, tipoCombustivel)
        self._pesoSuportado = pesoSuportadoKG
        self._comprimento = comprimento

    def ligar(self):
        print(f'O {self.nome} ligou: FOM FOM!!')

    def despejarCarga(self, lugar:str):
        print('O {} está despejando a carga em {}.'.format(self.nome, lugar))

    def pegarCarga(self, lugar:str, material:str):
        print('O {} está pegando uma carga de {} em {}.'.format(self.nome, material, lugar))

    def getDados(self):
        print(f'Nome: {self.nome}\nCor: {self.cor}\nTotal de rodas: {self._rodas}\nTipo de combustível: {self._combustivel}\nPeso que suporta: {self._pesoSuportado}kg\nComprimento: {self._comprimento} m.')