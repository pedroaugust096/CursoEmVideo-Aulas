# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada:

n = float(input('Digite um número: '))
d = 2*n
t = 3*n
r = n**(1/2)
print('Seu dobro é {:.2f} \nSeu triplo é {:.2f} \nE sua raiz quadrada é {:.2f}'.format(d, t, r))
