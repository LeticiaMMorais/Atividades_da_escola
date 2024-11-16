class Cliente():
    nome = ''
    __endereco = ''
    __cpf = ''
    __idade = 0

    def getDados(self):
        print(f'Nome: {self.nome}\nEndereço: {self.__endereco}\nCPF: {self.__cpf}\nIdade: {self.__idade}')

    def setEndereco(self):
        if self.__endereco == '':
            self.__endereco = input(f'{self.nome}, ponha seu endereço: ')
            print('Novo endereço registrado.')
        else:
            print('Já há um endereço registrado...')
    
    def setIdade(self):
        if self.__idade== 0:
            self.__endereco = input(f'{self.nome}, ponha sua idade: ')
            print('Idade registrada.')
        else:
            print('Já há uma idade registrada...')
        
    def setCPF(self):
        if self.__cpf == '' or self.validarCPF() == False:
            self.__endereco = input(f'{self.nome}, ponha seu CPF: ')
            print('CPF registrado.')           
        else:
            print('Já há um CPF válido registrado...')

    def validarCPF(self):
        cpf = self.__cpf
        if len(self.__cpf) == 14:
            d1 = int(cpf[0])
            d2 = int(cpf[1])
            d3 = int(cpf[2]) 
            d4 = int(cpf[4]) #Aqui foi pulado um ponto
            d5 = int(cpf[5])
            d6 = int(cpf[6])
            d7 = int(cpf[8]) #Aqui foi pulado um ponto
            d8 = int(cpf[9])
            d9 = int(cpf[10])
            soma9digitos = d1*1 + d2*2 + d3*3 + d4*4 + d5*5 + d6*6 + d7*7 + d8*8 + d9*9
            print(f'Soma dos 9 dígitos: {soma9digitos}')
            resto = soma9digitos%11
            print(f'Resto 1 = {resto}')
            digitoVerificador1 = str(resto)[-1]
            print('1º Dígito verificador: {}'.format(digitoVerificador1))
            
            soma10digitos = d1*0 + d2*1 + d3*2 + d4*3 + d5*4 + d6*5 + d7*6 + d8*7 + d9*8 + int(digitoVerificador1)*9
            print(f'Soma dos 10 dígitos: {soma10digitos}')
            resto2 = soma10digitos % 11
            print(f'Resto 2 = {resto2}')
            digitoVerificador2 = str(resto2)[-1]
            print('2º Dígito verificador: {}'.format(digitoVerificador2))

            if cpf[-2:] == digitoVerificador1+digitoVerificador2:
                print(f'Esse CPF de {self.nome} é válido.')
                return True
            else:
                print(f'Esse CPF de {self.nome} NÃO é válido.')
                return False

        else:
            print(f'O cpf ({self.__cpf}) não é válido por não possuir 14 caracteres (formato: 000.000.000-00)')
            return False
