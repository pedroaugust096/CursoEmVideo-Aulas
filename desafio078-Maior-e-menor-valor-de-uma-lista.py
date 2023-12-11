'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista.'''

'''Minha resolução:

valores = list()
for c in range(0, 5):
    num = int(input(f'Digite o {c+1}° valor: '))
    valores.append(num)
print('')
print(valores)
print(f'''#O valor máximo da lista é: {max(valores)}
# Ele está na posição {valores.index(max(valores))+1}''')
# print(f'''O valor mínimo da lista é: {min(valores)}
# Ele está na posição {valores.index(min(valores))+1}''')
# print('')


listanum = []
mai = men = 0
print()
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
