from EstudanteClasse import Estudante # Importando a classe que será herdada

class EstudanteIFRN(Estudante): # A classe EstudanteIFRN está HERDANDO Estudante
    def __init__ (self, nome: str, cpf: str, idade: int, matricula: int, sexo: str, curso:str, ano:int, escola: str = 'IFRN'):
        super().__init__(nome, cpf, idade, matricula, escola, sexo) # Iniciando a superclasse
        self._curso = curso
        self._ano = ano


    def estudar(self): #POLIMORFISMO:  o método estudar() já existe na superclasse, mas eu a sobrescrevi.
        print(f'{self._nome} está estudando desesperado (elo não teve tempo de estudar antes).')

    def reclamarDaMerenda(self):
        print(f'{self._nome}: a merenda é bolacha de novooo?? AFF')


