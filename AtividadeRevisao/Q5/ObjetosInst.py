from Pessoa1 import Pessoa
from Cliente1 import Cliente
from Vendedor1 import Vendedor

leticia = Vendedor('Letícia Maria', '129.485.238-23', 'VEN2008023')
fatinha = Vendedor('Maria de Fátima', '129.384.282-49', 'VEN1980018')
marcos = Vendedor('Marcos Morais', '912.495.293-45', 'VEN1981024')

angelina = Cliente('Anna Angelina', '583.485.293-40', 'A783490', True)
apolo = Cliente('Apolo Vieira', '293.546.247-75', 'A039449', True)
gil = Cliente('Gilberto', '293.456.764-20', 'G934291')

leticia.falar()
apolo.falar()

marcos.atenderPag()
angelina.getCupom()

fatinha.getInfo()
gil.getInfo()


