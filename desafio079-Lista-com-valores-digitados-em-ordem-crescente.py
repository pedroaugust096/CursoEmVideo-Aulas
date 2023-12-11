'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.'''

valores = list()
print('')
while True:
    num = int(input(f'Digite um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('O valor já consta na listagem!')
    perg = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if perg != 'S':
        break
print(valores)
     