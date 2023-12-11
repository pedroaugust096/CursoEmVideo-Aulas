'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''

n = int(input('\nDigite um número inteiro: '))
tot = 0
print('')
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end ='')
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{} '.format(c), end = '')
print('')
print('\n\33[mO número {} foi divisível {} vezes!'.format(n, tot), end = ' ')

if tot == 2:
    print('O número {} É PRIMO!'.format(n))
else:
    print('O número {} NÃO É PRIMO!'.format(n))
