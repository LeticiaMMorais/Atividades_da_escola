from EstudanteClasse import Estudante
from EstudanteIFRNClasse import EstudanteIFRN

# Dois OBJETOS serão instanciados:
Victor = Estudante('Victor Costa Lobo', '123.485.230-03', 22, 202023012253, 'UERN', 'Masculino')
leticia = EstudanteIFRN('Letícia Maria Morais', '120.495.123-43', 16, 20231094010064, 'Feminino', 'Informática', 2)

Victor.estudar()
leticia.estudar()
