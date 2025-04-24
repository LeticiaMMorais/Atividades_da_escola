class Campeao():
    def __init__ (self, nome:str, nivel:int):
        self.__nome = nome
        self.__nivel = nivel

    def mostrarDados(self):
        print(f'Nome do Campeão: {self.__nome}\nNível: {self.__nivel} estrelas\n')

    def alterarNivel(self,nnivel):
        if 0 < nnivel <=5:
            nivelantes = self.__nivel 
            self.__nivel = nnivel
            print(f'O nível de {self.__nome} foi alterado de {nivelantes} para {self.__nivel} estrelas.')
        else:
            print('Só aceito números maiores que 0 ou menor ou igual a 5. (0<n<=5)')

        