'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

'''preço = ('',
         '-'*40,
         '{:^40}'.format('LISTAGEM DE PREÇO'),
         '-'*40,
         '{:>}{:^}{:<}'.format('Lápis', '.'*25, 'R$   1.75 '),
         '{:>}{:^}{:<}'.format('Borracha', '.'*22, 'R$   2.00 '),
         '{:>}{:^}{:<}'.format('Caderno', '.'*23, 'R$  15.90 '),
         '{:>}{:^}{:<}'.format('Estojo', '.'*24, 'R$  25.00 '),
         '{:>}{:^}{:<}'.format('Transferidor', '.'*18, 'R$   4.20 '),
         '{:>}{:^}{:<}'.format('Compasso', '.'*22, 'R$   9.99 '),
         '{:>}{:^}{:<}'.format('Mochila', '.'*23, 'R$ 120.32 '),
         '{:>}{:^}{:<}'.format('Canetas', '.'*23, 'R$  22.30 '),
         '{:>}{:^}{:<}'.format('Livro', '.'*25, 'R$  34.90 '),
         '-'*40,
         '')

for n in preço:
    print(n)'''
    
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('')
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
