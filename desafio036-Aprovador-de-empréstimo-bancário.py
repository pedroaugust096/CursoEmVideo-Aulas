'''Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
tem = float(input('Em quantos anos você quer pagar esta casa? '))

prestação = (valor / (tem * 12))

if prestação > 0.3*sal:
    print('\nEMPRÉSTIMO NEGADO! \nPara ter margem suficiente para o financiamento, sua prestação deverá ser menor que R${:.2f}!'
          ' Sua prestação está valendo R${:.2f}'.format(0.3*sal, prestação))

else:
    print('\nEMPRÉSTIMO APROVADO! Para pagar uma casa de R${:.2f} em {:.0f} anos, a prestação será de R${:.2f}!'
          .format(valor, tem, prestação))