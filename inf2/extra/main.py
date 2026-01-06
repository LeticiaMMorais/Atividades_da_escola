def multiplica_matrizes(matriz1, matriz2):
    '''
    Docstring for multiplica_matrizes
    
    :param matriz1: matriz
    :param matriz2: matriz
    matriz = vetor de vetores
    '''
    if len(matriz1[0]) == len(matriz2): #Se o número de colunas da matriz 1 for igual ao número de linhas da matriz 2...
        matriz_resultante = []
        for row1 in range(len(matriz1)):  # 0
            
            
            for column1 in range(len(matriz1[row1])): #0
                linha_matriz_resultante = []
                elemento_matriz_resultado = 0
                # for row2 in range(len(matriz2)): #1
                for column2 in range(len(matriz2[0])): #0
                    elemento_matriz_resultado += matriz1[row1][column1] * matriz2[column1][column2] # 00 * 00 + 00 * 01 + 
                linha_matriz_resultante.append(elemento_matriz_resultado)
            matriz_resultante.append(linha_matriz_resultante)

        print(matriz_resultante)



            
    else: 
        print("Operação impossível")


matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
    ]
matriz2 = [
    [7, 8],
    [9, 10],
    [11, 12]
    ]

print(multiplica_matrizes(matriz1, matriz2))
