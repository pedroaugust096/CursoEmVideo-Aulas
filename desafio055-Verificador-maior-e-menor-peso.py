'''Faça o programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

maior = float()
menor = float()
print('')
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('''\nO menor peso foi {:.2f}kg.
O maior peso foi {:.2f}kg'''.format(menor, maior))