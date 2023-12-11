# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

tc = float(input('Digite a temperatura em ºC: '))
tf = 9*tc/5+32
print('A temperatura em ºF é igual a: {:.2f}'.format(tf))
