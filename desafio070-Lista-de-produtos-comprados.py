'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

tot_compra = maiormil = menor = c = 0
nome_menor = ''
texto = str('LOJA SUPER BARATÃO')
fim = str('FIM DO PROGRAMA')
print('-'*35)
print(f'{texto:^35}')
print('-'*35)
while True:
    prod = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$ '))
    tot_compra += preço
    c += 1
    if preço > 1000:
        maiormil += 1
    if c == 1:
        menor = preço
        nome_menor = prod
    elif menor > preço:
        menor = preço
        nome_menor = prod  
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        print(f'{fim:-^35}')
        break      
print(f'''O total da compra foi R${tot_compra:.2f}
Temos {maiormil} produtos custando mais de R$1000.00
O produto mais barato foi {nome_menor} que custa R${menor:.2f}''')