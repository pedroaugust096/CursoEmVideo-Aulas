'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for valor in num:   
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            valor = maior
        else:
            if valor > maior:
                maior = valor
        cont += 1           
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')    


maior(0, 3, 42, 55, 79, 1, 27, 36)
maior(15, -7, 22, -458, 1000, 2)
maior()
