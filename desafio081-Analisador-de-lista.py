'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valor = list()
print('')
while True:
    n = int(input('Digite um valor: '))
    valor.append(n)
    perg = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if perg != 'S':
        break
print('')
print(f'A lista possui {len(valor)} números.')
valor.sort(reverse=True)
print(f'Lista de valores: {valor}')
if 5 in valor:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')
