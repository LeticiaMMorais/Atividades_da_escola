import random

def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num-1)
    
def permutacao(entrada) -> list:
    fatorial_entrada = fatorial(len(entrada))
    combinacoes = []
    opcoes = list(entrada)
    while len(combinacoes) < fatorial_entrada:
        novo_elemento = []
        while len(novo_elemento) < len(entrada):
            novo_algarismo = random.choice(opcoes)
            if novo_algarismo not in novo_elemento:
                novo_elemento.append(novo_algarismo)
        if novo_elemento not in combinacoes:
            numero = ''
            for alg in novo_elemento:
                numero = numero+alg

            combinacoes.append(int(numero))
    return sorted(combinacoes)

entrada = input('numero com algarismos distintos: ')
combinacoes = permutacao(entrada)
n = 1
for numero in combinacoes: #cada linha é um número
    print(n, '   --  ',numero )
    n+=1