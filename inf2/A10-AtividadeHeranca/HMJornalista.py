from HMUsuario import Usuario
from HMUsuarioAutenticado import UsuarioAutenticado


'''Crie uma outra classe que herde de Usuario e 
UsuarioAutenticado, mas que possua outro nível 
e uma outra forma de adicionar o código.'''

class Jornalista(Usuario, UsuarioAutenticado):
    def cadastro(self):
        nome = input("Digite o nome do jornalista: ")
        senha = input("Digite a senha do jornalista: ")
        cod = 'jor' +str(range.randint(10000, 99999))
        self.setCodigo(cod)
        self.setDados(nome, "Jornalista")
        self.setSenha(senha)
    
    def getDados(self):
        print("> Nome: "+self.nome)
        print("> Nivel: "+self.nivel)
        print("> Codigo: "+self.codigo)