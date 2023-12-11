'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma 
entre todos os valores pares sorteados pela função anterior.'''
from time import sleep
from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for num in range(0, 5):
        num = randint(0, 10)
        print(f'{num}', end=' ', flush=True)
        números.append(num)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    par = 0
    for valor in lista:
        if valor % 2 == 0:
            par += valor
    print(f'Somando os valores pares de {números}, temos {par}')


números = list()
sorteia(números)
somaPar(números)
   