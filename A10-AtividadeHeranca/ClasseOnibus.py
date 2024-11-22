from ClasseAutomovel import Automovel

class Onibus(Automovel):
    def __init__(self, nome:str, cor:str , qntRodas:int , tipoCombustivel:str, qntPessoas: int):
        Automovel.__init__(nome,cor,qntRodas,tipoCombustivel)
        self._capacidade = qntPessoas

    def ligar(self):
        print(f'O {self.nome} foi ligado: BIBIIIIP!!')

    def pararNoPonto(self, nomeponto:str):
        print(f'O ônibus ({self.nome}) está parando no ponto: {nomeponto}.')

    def getDados(self):
        print(f'Nome: {self.nome}\nCor: {self.cor}\nTotal de rodas: {self._rodas}\nTipo de combustível: {self._combustivel}\nCapacidade de pessoas: {self._capacidade}')