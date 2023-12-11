'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
c = 0
jog = str()
jogpc = 0
pc = str()
result = str()
soma = int()
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    v = int(input('Diga um valor: '))
    jog = input('Par ou Ímpar? [P/I] ').upper()
    jogpc = randint(0, 10)
    soma = jogpc + v
    if soma % 2 == 0:
        result = 'P'
    else:
        result = 'I'
    if jog != result:
        print('-'*30)
        print(f'Você jogou {v} e o computador {jogpc}. Total de {soma} ', end='')
        if result == 'P':
            print('DEU PAR')
        elif result == 'I':
            print('DEU ÍMPAR')
        print('-'*30)
        print('Você PERDEU!')
        break
    else:
        c += 1
    if jog == result == 'P':
        print('-'*30)
        print(f'Você jogou {v} e o computador {jogpc}. Total de {soma} DEU PAR')
        print('-'*30)
    elif jog == result == 'I':
        print('-'*30)
        print(f'Você jogou {v} e o computador {jogpc}. Total de {soma} DEU ÍMPAR')
        print('-'*30)
    print('''Você VENCEU!
Vamos jogar novamente...''')
    print('=-'*15)   
print('=-'*15)
print(f'GAME OVER! Você venceu {c} vezes.')       
