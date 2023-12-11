'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
            'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

'''num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {contagem[num]}')'''

num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    elif 0 <= num <= 20:
        print(f'Você digitou o número {contagem[num]}. ', end='')
        resp = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
        if resp == 'S':
            num = int(input('Digite um número entre 0 e 20: '))
        elif resp not in 'SN':
            resp = str(input('Tente novamente. Você deseja continuar? [S/N] ')).strip().upper()[0]
        else:
            break
print('Obrigado. Volte sempre!')     