'''Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep
num = randint(0, 10)
print('')
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 19)
print('')
acertou = False
cont = 0
while not acertou:
    escolha = int(input('Em que número eu pensei? '))
    cont += 1
    print('\nPROCESSANDO...')
    sleep(1.5)
    if escolha == num:
        acertou = True
    else:
        if escolha < 0 or escolha > 10:
            print('\nDIGITE UM NÚMERO ENTRE 0 E 10. ESCOLHA INVÁLIDA!\n')
        elif escolha < num:
            print('\nMais... Tente mais uma vez\n')
        elif escolha > num:
            print('\nMenos... Tente mais uma vez\n')
print('''\nPARABÉNS,VOCÊ ACERTOU!
Você precisou de {} palpites para acertar!'''.format(cont))
