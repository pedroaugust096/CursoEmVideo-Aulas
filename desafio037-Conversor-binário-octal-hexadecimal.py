'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conver-
são:

- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

n = int(input('Digite um valor: '))
a = int(input('\nPara converter o valor, digite: \n'
      '\n [1] para converter para binário...'
      '\n [2] para converter para octal...'
      '\n [3] para converter para hexadecimal...\n'
      '\nEntrada: '))

if a == 1:
    b = bin(n)
    print ('\nO número {} convertido para binário é igual a: {}'.format(n, b[2:]))

elif a == 2:
    b = oct(n)
    print('\nO número {} convertido para octal é igual a: {}'.format(n, b[2:]))

elif a == 3:
    b = hex(n)
    print('\nO número {} convertido para hexadecimal é igual a: {}'.format(n, b[2:]))

else:
    print('Opção inválida. Tente novamente!')
