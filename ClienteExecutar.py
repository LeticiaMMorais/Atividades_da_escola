from ClienteClasse import Cliente

leticia = Cliente()
leticia.nome = 'Letícia Maria Morais'
leticia.setEndereco()
leticia.setIdade()
leticia.setCPF()
leticia.validarCPF()

print()

leo = Cliente()
leo.nome = 'Léo Morais'
leo.setEndereco()
leo.setIdade()
leo.setCPF()
leo.validarCPF()

print()

ciro = Cliente()
ciro.nome = 'Ciro Moura'
ciro.setEndereco()
ciro.setIdade()
ciro.setCPF()
ciro.validarCPF()

leticia.getDados()
leo.getDados()
ciro.getDados()