'''Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

[-] EQUILÁTERO: todos os lados iguais
[-] ISÓSCELES: dois lados iguais, um diferente
[-] ESCALENO: três lados diferentes'''

print('=-' * 14)
print('Analisador de Triângulos')
print('=-' * 14 )

l1 = float(input('\nDigite o comprimento da primeira reta: '))
l2 = float(input('Digite o comprimento da segunda reta: '))
l3 = float(input('Digite o comprimento da terceira reta: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('\nAs retas acima NÃO PODEM formar um triângulo')

else:
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        print('\nAs retas acima PODEM formar um triângulo\n')
        print('=-' * 20)
        print('Classificação do Triângulo')
        print('=-' * 20)

    if l1 == l2 and l1 == l3:
        print('\nO triângulo formado é EQUILÁTERO')

    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('\nO triângulo formado é ISÓSCELES')

    elif l1 != l2 != l3:
        print('\nO triângulo formado é ESCALENO')