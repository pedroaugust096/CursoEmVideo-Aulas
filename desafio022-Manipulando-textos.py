'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1)  O nome com todas as letras maiúsculas
2)  O nome com todas as letras minúsculas
3)  Quantas letras ao todo (sem considerar espaços)
4)  Quantas letras tem o primeiro nome'''

nome = str(input('Digite o nome completo da pessoa: '))
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print(len(''.join(dividido)))
print(len(dividido[0]))
