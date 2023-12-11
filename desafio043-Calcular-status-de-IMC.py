'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:

[-] Abaixo de 18.5: Abaixo do Peso
[-] Entre 18.5 e 25: Peso Ideal
[-] Entre 25 e 30: Sobrepeso
[-] Entre 30 e 40: Obesidade
[-] Acima de 40: Obesidade Mórbida'''

peso = float(input('\nDigite seu peso em kg: '))
h = float(input('Digite sua altura em m: '))
imc = peso / (h * h)

if peso <= 0 or h <= 0:
    print('\nDigite um valor válido!')

else:
    if imc < 18.5:
        print('\nSeu imc é de {:.2f} \nSeu status: ABAIXO DO PESO'.format(imc))

    elif 18.5 <= imc <= 25:
        print('\nSeu imc é de {:.2f} \nSeu status: PESO IDEAL'.format(imc))

    elif 25 <= imc <= 30:
        print('\nSeu imc é de {:.2f} \nSeu status: SOBREPESO'.format(imc))

    elif 30 <= imc <= 40:
        print('\nSeu imc é de {:.2f} \nSeu status: OBESIDADE'.format(imc))

    else:
        print('\nSeu imc é de {:.2f} \nSeu status: OBESIDADE MÓRBIDA'.format(imc))