from AnimalClasse import Animal

cachorro1 = Animal('Alasca', 'Branco', 4)
cachorro2 = Animal('Bob', 'Branco de bolinhas pretas')
cachorro3 = Animal('Alex', 'Caramelo', 1)
cachorro4 = Animal('Pantera', 'Preto', 2)

print(cachorro1._latir())
cachorro2.comer(50, 'Pedigree')
cachorro3.comer(150,'Ração Seca Suprema')
print(cachorro4._latir())