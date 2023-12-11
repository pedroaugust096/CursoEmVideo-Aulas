'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

tot_H = mui_menor = maior = 0
while True:
    texto = str('CADASTRE UMA PESSOA')
    print('-'*25)
    print(f'{texto:^25}')
    print('-'*25)
    i = int(input('Idade: '))
    if i > 18:
        maior += 1
    s = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if s == 'M':
        tot_H += 1
    elif s == 'F':
        if i < 20:
            mui_menor += 1
    else:
        print('-'*25)
        print('Por favor, digite um sexo válido!')    
    print('-'*25)
    q = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if q == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {maior}
Ao todo temos {tot_H} homens cadastrados
E temos {mui_menor} mulheres com menos de 20 anos''')
