'''LISTAS COMPOSTAS: são váriaveis compostas, assim como as listas, que agrupam uma lista dentro da outra. Ou seja,
é uma composta por outras listas.'''

print()
teste = list()
teste.append('Pedro')
teste.append(27)
galera = list()
'''galera.append(teste)
print(f'Lista teste: {teste}')
print(f'Lista galera: {galera}')
print()
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(f'Lista galera modificada: {galera}') # --> ficou deste jeito pois, ao fazer galera.append(teste), estamos
# realizando uma ligação entre as duas estruturas (teste e galera). Então, toda modificação feita em uma das lis-
# tas é refletida na outra.'''

# Para que apenas uma lista seja mudada, devemos fazer o seguinte:
galera.append(teste[:])
print(f'Lista teste: {teste}')
print(f'Lista galera: {galera}')
print()
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(f'Lista galera modificada: {galera}')

# Outra forma de declarar a lista composta:

print()
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(f'Lista galera declarada no segundo exemplo: {galera}')
print(f'Declaração galera[0]: {galera[0]}')
print(f'Declaração galera[0][0]: {galera[0][0]}')
print(f'Declaração galera[2][1]: {galera[2][1]}')

# Utilizando o for para printar o conteúdo da lista composta:

print()
print('Para printar o conteúdo da lista composta galera utilizando o for: ')
for p in galera:
    print(p)
print()

# Para printar somente os nomes:

for p in galera:
    print(p[0])
print()

# Para printar somente a idade:

for p in galera:
    print(p[1])    
print()

# Mostrar os elementos discriminados:

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print()

# Mostrando os elementos 'inputados' em uma lista:

galera = list()
dado = list()
totmai = totmen = 0 # --> só é possível fazer esta atribuição simplificada para VARIÁVEIS SIMPLES!
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    print()
    galera.append(dado[:]) # --> copia os dados para a lista galera sem atrelar uma a outra
    dado.clear() # --> limpa os dados da lista para receber os dados de uma nova pessoa
print(f'A lista galera do terceiro exemplo é: {galera}')

# Para mostrar somente os que têm mais de 21 anos:
print()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print()
print(f'Temos {totmai} maiores e {totmen} menores de idade.')      
