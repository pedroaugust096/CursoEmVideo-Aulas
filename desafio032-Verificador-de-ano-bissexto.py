'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''

ano = int(input('Digite um ano para ver se ele é bissexto: '))
divisao = ano%4
if divisao != 0:
    print('Não é ano bissexto!')
else:
    print('É ano bissexto!')