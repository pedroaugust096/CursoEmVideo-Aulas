'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"'''
c = str(input('Digite o nome de uma cidade: ')).strip()
print(c[:5].capitalize() == 'Santo')
