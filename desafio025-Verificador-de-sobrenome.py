'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome'''
nome = str(input('Digite seu nome: '))
if 'Silva' in nome:
    print('Tem Silva')
elif 'Santos' in nome:
    print('Tem Santos')
elif 'Souza' in nome:
    print('Tem Souza')
else:
    print('Não possui os sobrenomes Silva, Santos ou Souza')
