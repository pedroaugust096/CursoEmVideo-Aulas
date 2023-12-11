'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:

[-] À vista dinheiro/cheque: 10% de desconto
[-] À vista no cartão: 5% de desconto
[-] Em até 2x no cartão: preço normal
[-] 3x ou mais no cartão: 20% de juros'''

preço = float(input('Digite o valor do produto: R$'))
escolha = int(input('''\nSelecione a forma de pagamento:

[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão

Opção selecionada: '''))

if escolha == 1:
    np = preço * 0.9
    print('\nVocê receberá 10% de desconto na sua compra. Seu produto sairá por R${:.2f}'.format(np))

elif escolha == 2:
    np = preço * 0.95
    print('\nVocê receberá 5% de desconto na sua compra. Seu produto sairá por R${:.2f}'.format(np))

elif escolha == 3:
    print('\nSeu produto sairá por R${:.2f}'.format(preço))

elif escolha == 4:
    np = preço * 1.2
    print('\nVocê pagará um juros de 20% por escolher parcelar em 3x ou mais. Seu produto sairá por R${:.2f}'.format(np))

else:
    print('\nDigite um valor válido!!!')
