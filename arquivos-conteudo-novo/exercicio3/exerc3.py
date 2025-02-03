""" Exercício 3:
Alterem o código em anexo para que o estoque seja armazenado em um arquivo.
Na primeira execução, o arquivo de estoque estará vazio. Então também será necessário criar uma função que adiciona um item ao estoque. Com o estoque preenchido, será possível salva-lo no arquivo. Depois você conseguirá carregar o estoque do arquivo para o programa.
Dessa forma, você precisará das funções:
- Carregar Estoque do Arquivo;
- Salvar Estoque no Arquivo;
- Adicionar Item ao Estoque;
- Ver o Estoque;
- Realizar Venda;
- Calcular Total.
"""

#Estoque em um dicionário, mas precisará estar vazio {} já que os dados virão do arquivo.
estoque={}

#vendas em uma matriz, mas pode ficar vazia, já que existe uma função que adiciona as venda.
venda = []

#total tá vazio, mas ao executar a função verTotal esse valor será atualizado
total = 0

nome_arquivo = 'estoque.txt'

def salvarEstoque(estoque): #salvar estoque no arquivo
    global nome_arquivo
    with open(nome_arquivo, 'w') as arquivo:
        for chave, dados in estoque.items():
            arquivo.write(f'{chave}#{dados}\n')


def carregarEstoque():
    estoque = {}
    with open(nome_arquivo, 'r') as arquivo:
        carregamento = arquivo.readlines()
        for linha in carregamento:
            retorno = linha.strip().split('#')
            produto = retorno[0]
            dados = retorno[1]
            dados = dados.replace('[','')
            dados = dados.replace(']','')
            quant, valor = dados.strip().split(',')
            estoque[produto] = [int(quant), float(valor)]
    return estoque    


def adicionarItem():
    global estoque
    item = input('Nome do novo item:\n').strip().lower()
    quantidade = int(input('Quantidade de {}\n'.format(item)))
    preco = float(input('O preço de {} será:\n'.format(item)))
    estoque[item] = [quantidade, preco]
    salvarEstoque(estoque)


def Venda(): #realizar venda
    global venda
    item = input("Nome do item: ").strip().lower()
    quantidade = int(input("Quantidade do item: "))
    venda.append([item, quantidade])
    estoque = carregarEstoque()
    for produto, dados in estoque.items():
        if produto == item:
            dados[0] -= quantidade
    salvarEstoque(estoque)


#Aqui as vendas são efetivadas, reduzindo a quantidade do estoque e atualizando o valor do total
def verTotal(): #Calcular Total
    global total
    print("Vendas:\n")
    for operacao in venda:
        produto, quantidade = operacao
        preco = estoque[produto][1]
        custo = preco * quantidade
        print("%12s: %3d x %6.2f = %6.2f" %(produto, quantidade,preco,custo))
        estoque[produto][0] -= quantidade
        total += custo
    print(" Custo total: %21.2f\n" % total)


def verEstoque(): #ver estoque
    estoque = carregarEstoque()
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descricao: ", chave)
        print("Quantidade: ", dados[0])
        print("Preco: %6.2f\n" % dados[1])




        




###Adicionar item no estoque
#lembrar que cada dado tem seu tipo
#estoque[item] = [quantidade, valor]
#resta criar a função e pedir pro usuário informar os dados

###Carregar Estoque do Arquivo
#Após abrir o arquivo em modo de leitura
#Percorrer linha a linha
#em cada linha fazer algo como:
#prod, quantValor = linha.stlip().split("#")
#quantValor = quantValor.replace('[', '')
#quantValor = quantValor.replace(']', '')
#quant, valor = quantValor.strip().split(",")
#estoque[prod] = [int(quant), float(valor)]
#lembrar de fechar o arquivo quando finalizar

###Salvar Estoque no Arquivo
#Após abrir o arquvo em modo de escrita 
#fazer algo como isso para salvar o estoque no arquivo
#for chave, dados in estoque.items():
#   arquivoEstoque.write("%s#%s\n" % (chave,dados))
#lembrar de fechar o arquivo quando finalizar


op = 1
while op != 0:
    estoque = carregarEstoque()
    print("O que deseja fazer?")
    op = int(input("1- venda | 2- ver total | 3- ver estoque | 4- adicionar item ao estoque | 0- sair\n"))
    if op == 1:
        Venda()
    elif op == 2:
        verTotal()
    elif op == 3:
        verEstoque()
    elif op == 4:
        adicionarItem()
    elif op == 0:
        print ("saindo...")
    else:
        print("digite uma opção válida!")