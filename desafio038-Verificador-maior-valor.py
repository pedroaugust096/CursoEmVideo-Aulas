'''Escreva um programa que leia dois números inteiros e compare-os, mostrando-os na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = int(input('\nDigite o primeiro número inteiro: '))
n2 = int(input('\nDigite o segundo: '))

if n1 > n2:
    print('\nO PRIMEIRO VALOR É O MAIOR!')

elif n1 < n2:
    print('\nO SEGUNDO VALOR É O MAIOR!')

else:
    print('\nNÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS!')
