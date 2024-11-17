from NotebookClasse import Notebook

note1 = Notebook('Laptop da Letícia', 'Book', 'Samsung', 'Windows', 'Letícia')

note2 = Notebook('Frufru', 'Inspiron 14', 'Dell', 'Windows', 'Fátima')

note1.jogar()
print(note1.criarArquivo('Ata financeira', 'Excel'))
note2.baixarFotos(10)
note2._deletarArquivo('Foto 9')

print()

note1.getDados()
print()
note2.getDados()