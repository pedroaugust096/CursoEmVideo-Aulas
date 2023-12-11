# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado

k = float(input('O carro percorreu quantos quilômetros? '))
d = float(input('O carro foi alugado por quantos dias? '))
p = 60*d+0.15*k
print('O valor do preço a ser pago é de R$:{:.2f}'.format(p))
