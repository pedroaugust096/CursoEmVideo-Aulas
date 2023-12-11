'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
ce50 = ce20 = ce10 = ce1 = valor = 0
valor = int(input('Que valor você quer sacar? R$ '))
while valor != 0:
    if valor // 50 != 0:
        ce50 = valor // 50
        valor = valor % 50
        print(f'Total de {ce50} cédulas de R$50')
    elif valor // 20 != 0:
        ce20 = valor // 20
        valor = valor % 20
        print(f'Total de {ce20} cédulas de R$20')
    elif valor // 10 != 0:
        ce10 = valor // 10
        valor = valor % 10
        print(f'Total de {ce10} notas de R$10')
    elif valor < 10:
        ce1 = valor
        print(f'Total de {ce1} notas de R$1')
        valor = 0
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
        