class Estudante(): # Uma CLASSE estudante está sendo criada
    def __init__ (self, nome: str, cpf: str, idade: int, matricula: int, escola: str,sexo: str):
        self._nome = nome  # Aqui nós temos os ATRIBUTOS adquirindo seus valores.
        self.__cpf = cpf # Está sendo feito um ENCAPSULAMENTO
        self._idade = idade
        self._matricula = matricula
        self._escola = escola
        self.__sexo = sexo  # Está sendo feito um ENCAPSUMENTO

    def  estudar(self):  # Aqui foi criado um MÉTODO, um comportamento que um "Estudante" apresenta.
        print(f'{self._nome} está estudando.')
    
    def checarHorario(self):
        print(f'{self._nome} está checando o horário dele...')