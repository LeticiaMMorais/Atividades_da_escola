class Robo():
    def __init__(self, codinterno: str, identificador: str, voltagem: int, status: bool = False):
        self.__codinterno = codinterno
        self.identificador = identificador
        self.voltagem = voltagem
        self.status = status

    def getCodinterno(self):
        return self.__codinterno
    
    def setidentificador(self, nidentificador: int):
        self.identificador = nidentificador

    def getidentificador(self):
        return f'Identificador do Robô: {self.identificador}'
    
    def getVoltagem(self):
        return self.voltagem
    
    def alterarStatus(self):
        if self.status:
            self.status = False
        else:
            self.status = True
