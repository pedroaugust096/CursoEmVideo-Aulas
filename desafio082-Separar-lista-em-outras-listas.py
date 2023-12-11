'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

valor = list()
par = list()
impar = list()
print('')
while True:
    n = int(input('Digite algum valor: '))
    valor.append(n)
    perg = str(input('Deseja continuar? [S/N] ')).upper()
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if perg != 'S':
        break
print(f'A primeira lista é: {valor}')
print(f'A lista de números pares é: {par}')
print(f'A lista de valores ímpares é: {impar}')
print('')
        