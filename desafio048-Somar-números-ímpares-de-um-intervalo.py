'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500'''

s = 0
cont = 0
print('')
for c in range(3, 501, 3):
    if c % 2 != 0:
        print(c)
        cont += 1
        s += c
print('\nO somatório dos {} números ímpares entre 0 e 500 que são múltiplos de 3 é: {}'.format(cont, s))
