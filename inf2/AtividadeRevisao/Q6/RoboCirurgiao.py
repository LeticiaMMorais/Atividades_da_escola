from RoboC import Robo

class RoboCirurgiao(Robo):
    def __init__(self, codinterno: str, identificador: str, voltagem: int, conexao: int, status: bool = False, operando: bool = False):
        super().__init__(codinterno, identificador, voltagem, status)
        self.conexao = conexao
        self.operando = operando

    def operar(self):
        self.operando = True
        return self.operando
    
    def verConexao(self):
        print(f'A conexão é de {self.conexao}.')
        return True
    
    def buscarConexao(self):
        print('Estamos buscando uma conexão mais estável.')