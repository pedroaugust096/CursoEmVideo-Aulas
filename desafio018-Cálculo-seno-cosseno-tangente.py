'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''

from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f} tem o SENO de {:.2f}\n O ângulo de {:.1f} tem o COSSENO de {:.2f}\n O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))
