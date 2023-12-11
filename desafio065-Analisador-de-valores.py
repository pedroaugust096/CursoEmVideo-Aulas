'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores.'''

c = 0
m = float()
s = int()
n = int()
maior = 0
menor = 0
s == 0
while True:
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    p = str(input('Quer continuar? [S/N] ')).upper()
    if p != 'S':
        m = s/c
        break
print('Você digitou {} valores e a média foi {:.2f}'.format(c, m))
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
