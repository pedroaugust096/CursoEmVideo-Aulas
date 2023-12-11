# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
import math

l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
a = l*h
q = float(math.ceil(a/2))
print('A área da parede é de {}m² \nSerão necessários {} baldes de tinta para pintar esta parede'.format(a, q))
