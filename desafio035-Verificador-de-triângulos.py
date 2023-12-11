'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo'''

import cmath

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('As retas acima PODEM formar triângulo!')
else:
    print('As retas acima NÃO PODEM formar triângulo!')