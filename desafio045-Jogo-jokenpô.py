'''Crie um programa que faça o computador jogar Jokenpô com você'''

from random import choice
from time import sleep

print('{:=^40}'.format(' JOGO JOKENPÔ '))
Pedra = str('Pedra')
Papel = str('Papel')
Tesoura = str('Tesoura')

escolha = str(input('''Escolha entre pedra, papel ou tesoura:

Sua escolha: '''))

lista = [Pedra, Papel, Tesoura]
computador = choice(lista)

print('''\nAgora eu farei minha escolha

Eu escolho: ''', end='')
sleep(3)

if escolha == computador:
    print('{}! EMPATE!'.format(computador))

elif escolha == Pedra and computador == Papel or escolha == Tesoura and computador == Pedra or escolha == Papel and computador == Tesoura:
    print('{}! VOCÊ PERDEU!'.format(computador))

elif escolha == Pedra and computador == Tesoura or escolha == Tesoura and computador == Papel or escolha == Papel and computador == Pedra:
    print('''{}!

Meus parabéns! VOCÊ VENCEU'''.format(computador))

else:
    print('Por favor, digite uma entrada válida!')
