"""
Elabore uma maneira de gerenciar os nomes dos alunos de uma turma usando arquivo:
• Como ver os alunos que já estão no arquivo?
• Como inserir um novo aluno?
"""
#Podemos ler os alunos que estão no arquivo com a seguinte função:
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    rArquivo = arquivo.readlines()
    arquivo.close()
    return rArquivo

#Podemos adicionar um novo aluno no arquivo com a seguinte função:
def adicionar_ao_arquivo(nome_arquivo, novo_aluno):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(novo_aluno+'\n') #Tem que colocar \n para ele entender que a linha terminou.
    arquivo.close()


#Primeiro vamos criar o arquivo para não dar problema:
nome_arquivo = 'alunos.txt'
arquivoAlunos = open(nome_arquivo, 'a') #se colocasse 'w' as informações já presentes no arquivo seriam apagadas.
arquivoAlunos.close()

#Agora, vamos deixar essas funções usáveis:
continuar = 's'
while continuar.lower() in ['s', 'sim', 'ss']:
    funcao = input('\nEscolha um número:\n1- Ver os alunos que estão na turma\n2- Adicionar um novo aluno\n > ').strip()
    if funcao=='1':
        arquivo = ler_arquivo(nome_arquivo)
        print('\nA turma tem os seguintes alunos: ')
        for linha in arquivo:
            print(linha, end='') #Se não colocar end, os nomes serão impressos pulando as linhas.
        print('\n Fim do arquivo')
    
    elif funcao=='2':
        novo_aluno = input('\nDigite o nome do novo aluno:\n > ').strip().title()
        adicionar_ao_arquivo(nome_arquivo, novo_aluno)
        print('\n O nome foi adicionado.')

    else:
        print('   Só aceito 1 ou 2.')
    continuar = input('\nDeseja realizar mais alguma operação?\n > ').strip()


