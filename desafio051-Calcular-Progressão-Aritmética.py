'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão'''

print('')
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
print('')

for c in range(1, 11):
    an = a1 + (c-1)*r
    print('O {}° termo da PA é: {:2}'.format(c, an))
print('\nFIM!')