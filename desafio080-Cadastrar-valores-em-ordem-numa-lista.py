'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

valores = list()
print('')
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}° número: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'O valor foi adicionado na {pos+1}ª posição')
                break
            pos += 1
print('')
print(valores)
        