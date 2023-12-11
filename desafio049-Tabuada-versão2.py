'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for'''

n = int(input('\nDigite um número qualquer: '))
print('{:=^40}'.format(' TABUADA DO NÚMERO {} '.format(n)))
print('')

for c in range(0, 11):
    tab = int(n*c)
    print('{} x {:2} = {}'.format(n, c, tab))
print('\nFIM!')