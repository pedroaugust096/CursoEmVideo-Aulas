'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa custará R$7,00 por cada km acima do limite'''

vel = int(input('Digite a que velocidade o carro está, em km/h: '))
if vel <= 80:
    print(str('\nO carro está dentro do limite de velocidade!'))
else:
    multa = float((vel-80)*7)
    acima = int(vel - 80)
    print('Seu carro foi multado por estar {}km/h acima da velocidade \nO valor da multa é de R${:.2f}'.format(acima, multa))
