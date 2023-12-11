'''Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50
por km para viagens de até 200km e R$0,45 para viagens mais longas'''

dist = float(input('Qual a distância da viagem em km: '))
if dist <= 200:
    preço = dist*0.50
    print('O preço da passagem será de R${:.2f}'.format(preço))
else:
    preço = dist*0.45
    print('O preço da passagem será de R${:.2f}'.format(preço))