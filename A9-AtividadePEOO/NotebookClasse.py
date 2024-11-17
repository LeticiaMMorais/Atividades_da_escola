class Notebook:
    def __init__ (self, nomeNotebook: str, modelo: str, marca: str, sistemaOperacional: str, dono: str):
        self.nomeNotebook = nomeNotebook
        self.__modelo = modelo
        self.__marca = marca
        self.sistemaOperacional = sistemaOperacional
        self.__dono = dono
        self._armazenamento = []
    
    def getDados(self):
        print(f'Nome do Notebook: {self.nomeNotebook}\nModelo: {self.__modelo}\nMarca: {self.__marca}\nSistema Operacional: {self.sistemaOperacional}\nDono: {self.__dono}\nArmazenamento: {self._armazenamento}')

    def pesquisar(self, pesquisa: str, navegador: str):
        return f'Está sendo feita uma pesquisa sobre {pesquisa} no navegador {navegador} do {self.nomeNotebook}.'
    
    def baixarFotos(self, qnt: int):
        print(f'{qnt} fotos estão sendo baixadas no {self.nomeNotebook}.')
        for i in range(len(self._armazenamento), len(self._armazenamento) + qnt):
            self._armazenamento.append('FOTO '+str(i))

    def jogar(self):
        print(f'Alguém está jogando no {self.nomeNotebook}.')

    def criarArquivo(self, nomeArquivo: str, programa: str):
        self._armazenamento.append(nomeArquivo.upper())
        return f'Foi armazenado o arquivo {nomeArquivo}, criado no programa {programa}.'
    
    def _deletarArquivo(self,nomeArquivo: str):
        if nomeArquivo.upper() in self._armazenamento:
            self._armazenamento.remove(nomeArquivo.upper())
            print('O arquivo foi deletado.')
        else:
            print('Esse arquivo não existe no armazenamento.')
