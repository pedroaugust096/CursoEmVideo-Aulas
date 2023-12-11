# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Digite o preço do produto: '))
pn = p*0.95
print('O valor do produto com desconto é de R${:.2f}'.format(pn))
