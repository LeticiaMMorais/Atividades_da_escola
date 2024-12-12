from RoboC import Robo

class RoboAspirador(Robo):
    def __init__(self, codinterno: str, identificador: str, voltagem: int, nivelBateria: int, status: bool = False, aspirando: bool = False):
        super().__init__(codinterno, identificador, voltagem, status)
        self.aspirando = aspirando
        self.nivelBateria = nivelBateria

    def aspirar(self):
        return self.aspirando
    
    def verNivelBateria(self):
        return self.nivelBateria
    
    def irCarregar(self):
        return 'O robô aspirador está carregando.'
