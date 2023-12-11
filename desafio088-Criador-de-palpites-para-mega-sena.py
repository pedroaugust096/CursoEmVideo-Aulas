'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from random import randint
jogo = list()
numeros = list()
tot = 0
qjogos = int(input('Quantos jogos você deseja fazer? '))
while tot < qjogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont == 6:
            break
    numeros.sort()
    jogo.append(numeros[:])
    numeros.clear()
    print(f'Jogo {tot+1}: {jogo[0]}')
    jogo.clear()
    tot += 1
