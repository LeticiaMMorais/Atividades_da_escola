class UsuarioAutenticado:
    nome = ''
    __senha = ''
    nivel = ''

    def setDados(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
    
    def getDados(self):
        print("> Nome: "+self.nome)
        print("> Nivel: "+self.nivel)
    
    def setSenha(self, senha: str):
        if len(senha) > 8:
            self.__senha = senha
    
    def getSenha(self):
        return self.__senha