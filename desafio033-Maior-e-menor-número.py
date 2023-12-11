'''Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n3<n2<n1:
    print('O maior número é o {} e o menor é {}'.format(n1, n3))
if n3<n1<n2:
    print('O maior número é o {} e o menor é {}'.format(n2, n3))
if n2<n1<n3:
    print('O maior número é o {} e o menor é {}'.format(n3, n2))
if n2<n3<n1:
    print('O maior número é o {} e o menor é {}'.format(n1, n2))
if n1<n2<n3:
    print('O maior número é o {} e o menor é {}'.format(n3, n1))
if n1<n3<n2:
    print('O maior é {} e o menor é {}'.format(n2, n1))

'''Resolução Guanabara:
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é menor
menor = a
if b < a and b < c:
    menor =  b
if c < a and c < b:
    menor = c

# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi: {}'.format(menor))
print( 'O maior valor digitado foi: {}'.format(maior))'''