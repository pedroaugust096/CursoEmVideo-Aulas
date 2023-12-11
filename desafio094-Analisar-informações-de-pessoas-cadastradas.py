'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
mulher = list()
acmedia = list()
dic = dict()
lista = list()
soma = 0
while True:
    dic['nome'] = str(input('Nome: '))
    while True:
        dic['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if dic['sexo'] not in 'MmFf':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            break
    if dic['sexo'] in 'Ff':
        mulher.append(dic['nome'])
    dic['idade'] = float(input('Idade: '))
    while True:
        cont = str(input('Quer continuar? [S/N] '))
        if cont not in 'SsNn':
            print('ERRO! Digite apenas S ou N.')
        else:
            break
    soma += dic['idade']
    lista.append(dic.copy())
    if cont in "Nn":
        break
media = soma/len(lista)
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for e in mulher:
    print(f'{e}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f' {k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
    