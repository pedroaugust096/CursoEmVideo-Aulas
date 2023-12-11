'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa'''

from math import hypot
c1 = float(input('Digite o valor do comprimento do cateto oposto: '))
c2 = float(input('Digite o valor do comprimento do cateto adjacente: '))
h = hypot(c1, c2)
print('O comprimento da hipotenusa deste triângulo retângulo é de {:.2f}'.format(h))
