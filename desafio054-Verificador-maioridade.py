'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores'''

from datetime import date

menor = 0
maior = 0
atual = date.today().year
print('')

for c in range(1, 8):
    nasc = float(input('Em que ano a {} pessoa nasceu? '.format(c)))
    dif = atual - nasc

    if (atual - nasc) <= 18:
        menor += 1

    else:
        maior += 1

print('\n{} pessoas ainda não atingiram a maioridade'.format(menor))
print('{} pessoas já atingiram a maioridade'.format(maior))
