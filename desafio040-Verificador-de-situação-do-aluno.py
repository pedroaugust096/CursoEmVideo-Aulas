'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:

[-] Média abaixo de 5.0: REPROVADO
[-] Média entre 5.0 e 6.9: RECUPERAÇÃO
[-] Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('''\nSua média é {:.2f}.
Resultado: REPROVADO!'''.format(media))

elif media >= 5.0 and media <= 6.9:
    print('''\nSua média é {:.2f}
Resultado: RECUPERAÇÃO!'''.format(media))

elif media > 6.9:
    print('''\nSua média é {:.2f}
Resultado: APROVADO! PARABÉNS!'''.format(media))