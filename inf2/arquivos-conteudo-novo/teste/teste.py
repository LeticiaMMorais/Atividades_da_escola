import random

def escreverNumerosAleatorios(qtdNumeros, nomeArquivo):
    arquivoNumeros = open(nomeArquivo,'r+')
    for i in range(qtdNumeros):
        arquivoNumeros.write(str(random.randint(0,100)))
        arquivoNumeros.write('\n')

    arquivoNumeros.close()

# escreverNumerosAleatorios(100, 'aleatorios.txt')
def escreverMedia(qtdNumeros,nomeArquivo):
    arquivoNumeros = open(nomeArquivo)
    soma = 0
    for i in range(qtdNumeros):
        num = float(arquivoNumeros.readline())
        soma+=num

    arquivoNumeros.close()
    return soma/qtdNumeros

print(escreverMedia(100, 'aleatorios.txt'))

arquivoNumeros = open('aleatorios.txt')
for linha in arquivoNumeros:
    print(linha, end='')
