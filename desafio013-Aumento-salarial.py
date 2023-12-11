# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

s = float(input('Digite seu salário: '))
a = float(input('Digite o valor do aumento: '))
s2 = s*a
print('O valor do salário com o aumento é de R${:.2f}'.format(s2))
