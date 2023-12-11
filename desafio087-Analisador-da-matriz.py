'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print()
pares = 0
tc = 0
maior = 0

for l in range(0, 3): # --> l = linha
    for c in range(0, 3): # --> c = coluna
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        tc += matriz[l][2]
        if matriz[1][c] == 0:
            maior = 0
        elif matriz[1][c] > maior:
            maior = matriz[1][c]                     
print('')
for l in range(0, 3): # --> for que tem a finalidade de 'arrumar' a conformação dos valores de acordo com a matriz 3x3
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print() # --> para fazer com que, toda vez que uma coluna termine, o for passe para a linha de baixo
print(f'A soma de todos os valores pares digitados é {pares}')
print(f'A soma da terceira coluna é {tc}')
print(f'O maior valor da segunda linha é {maior}')
print('Izi')
