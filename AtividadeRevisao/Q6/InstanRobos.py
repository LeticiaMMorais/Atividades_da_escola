from RoboC import Robo
from RoboAspirador import RoboAspirador
from RoboCirurgiao import RoboCirurgiao

r1 = RoboAspirador('00101010010101100101101010110101010101...', 'RoboAspironx2930', 220, 84, False, False)

r2 = RoboCirurgiao('00101010010101100101101010110101010101...', 'RoboCirurtion2931', 110, 2, False, False)

r2.operar()
r2.buscarConexao()

r1.alterarStatus()
print(r1.verNivelBateria())
