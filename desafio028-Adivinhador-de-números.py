'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
perdeu'''

import random

num = [0, 1, 2, 3, 4, 5]
esc = random.choice(num)
tentativa = int(input('Tente adivinhar o número escolhido pelo computador. Digite um número entre 0 e 5: '))
if tentativa == esc:
    print('Meus parabéns, você venceu. O número escolhido foi {}'.format(esc))
else:
    print('Você perdeu. O número escolhido foi {}'.format(esc))

''' RESOLUÇÃO GUANABARA
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(5)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))'''
