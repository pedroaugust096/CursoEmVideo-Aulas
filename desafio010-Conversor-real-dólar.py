# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27

n = float(input('Digite o quanto você tem na sua carteira em reais: '))
d = n/3.27
di = n//3.27
res = (n%3.27)
print('Você pode comprar {:.2f} dólares \nVocê terá {:.2f} dólares inteiros \nE te sobrarão {:.2f} reais'.format(d,di,res))
