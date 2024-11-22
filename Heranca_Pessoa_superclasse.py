class Pessoa:
	def __init__(self, nomep, cpfp, enderecop):
		self.__nome = nomep
		self.__cpf = cpfp
		self.__endereco = enderecop

	def getAtributos(self):
		print('> Nome: {}\n> CPF {}\n> Endereço: {}'.format(self.__nome,self.__cpf,self.__endereco))

	def falar(self):
		print('Olá!')
