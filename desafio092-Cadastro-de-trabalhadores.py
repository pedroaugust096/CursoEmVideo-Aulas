'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
while True:
    cadastro = dict()
    cadastro['Nome'] = str(input('Nome: '))
    ano_nasc = int(input('Ano de Nascimento: '))
    cadastro['Idade'] = datetime.now().year - ano_nasc
    cadastro['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if cadastro['Ctps'] == 0:
        print('-=' * 30)
        for k, v in cadastro.items():
            print(f' - {k} tem o valor {v}')
        break
    if cadastro['Ctps'] != 0:
        cadastro['Contratação'] = int(input('Ano de Contratação: '))
        cadastro['Salário'] = int(input('Salário: R$'))
        contr = (datetime.now().year - cadastro['Contratação'])
        cadastro['Aposentadoria'] = (35 - contr) + cadastro['Idade']
        print('-=' * 30)
        for k, v in cadastro.items():
            print(f' - {k} tem o valor {v}')
        break
print()
