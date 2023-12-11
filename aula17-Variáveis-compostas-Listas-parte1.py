'''LISTAS: Variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves
individuais. Ex.:'''

print('')
print('Primeiro Exemplo:')
print('')
num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 --> não funciona. Para adicionar valores à lista usamos .append()
num.append(7)
# num.sort() # --> ordena a lista, em ordem crescente
num.sort(reverse=True) # --> ordena a lista, em ordem decrescente
# num.insert(2, 0) # --> na posição 2 será inserido o valor 0
# num.pop() # --> remove o último valor da lista
# num.pop(2) # --> retira o item número 2 da lista
num.insert(2, 2)
num.remove(2) # procura, do início da lista, a primeira ocorrência do valor que você mandou eliminar (no caso,
# o valor 2) e o retira da lista
num.remove(5)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print('')
print(f'Essa lista tem {len(num)} elementos.')
print('\n')

'''Para começar uma lista vazia:
1ª opção --> valores = list()
2ª opção --> valores = []'''

print('Segundo Exemplo:')
print('')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

'''for v in valores:
    print(f'{v}... ', end='')'''
    
# Se quisermos mostrar o valor e o índice:
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('\n')

# Outra forma de fazer:
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('\n')

print('Terceiro exemplo:')
print('')
a = [2, 3, 4, 7]
# b = a
# b[2] = 8 # --> mexe nas duas listas, por conta da linha de cima. O comando de cima criauma ligação entre
# as duas listas

# Para que seja feita a alteração somente na lista b, devemos criar uma cópia dos valores da lista a na
# lista b, seguindo a seguinte lógica:

b = a[:] # --> joga todos os valores de A na lista B, sem fazer uma ligação entre elas
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
    