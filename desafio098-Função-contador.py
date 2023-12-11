'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    
    if i<=f:
        while i <= f:
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
            i += p
        print('FIM!')
    else:
        while i >= f:
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
            i -= p
        print('FIM!')

    

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
início = int(input(f'{"Início:":<8}'))
fim = int(input(f'{"Fim:":<8}'))
passo = int(input(f'{"Passo:":<8}'))
contador(início, fim, passo)
