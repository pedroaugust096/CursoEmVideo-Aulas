'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print()

for l in range(0, 3): # --> l = linha
    for c in range(0, 3): # --> c = coluna
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))
print('')
for l in range(0, 3): # --> for que tem a finalidade de 'arrumar' a conformação dos valores de acordo com a matriz 3x3
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print() # --> para fazer com que, toda vez que uma coluna termine, o for passe para a linha de baixo
