'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos'''

somatorio = float()
media = float()
maior = float()
mulheres = str()
imulher = float()
nmaior = str()
for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).upper().split()
    idade = float(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite se seu sexo é H/M: '))
    print('')
    somatorio += idade
    if c == 1 and sexo == 'H':
        maior = idade
        nmaior = nome
    else:
        if sexo == 'H' and idade > maior:
            idade = maior
            nmaior = nome
    if sexo == 'M' and idade < 20:
        imulher += 1
    c += 1
media = somatorio / 4
print('A média da idade do grupo é {:.2f} anos, o homem mais velho se chama {} e {:.0f} mulheres têm menos de 20 anos'.format(media, nmaior, imulher))