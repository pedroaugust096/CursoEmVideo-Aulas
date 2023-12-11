# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input('Digite um valor em metros: '))
cm = n*100
mm = n*1000
print('Este valor, em centímetros, é igual a {}cm\nE, em milímetros, é igual a {}mm'.format(cm, mm))
