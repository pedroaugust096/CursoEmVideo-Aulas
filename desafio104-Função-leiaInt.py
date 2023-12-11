'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''
def leiaInt(msg):
    valor = 0
    print('-' * 30)
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            return valor
            break
        else:
            print('\033[0;31mERRO! Digite um valor numérico válido.\033[m')
                

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número \033[0;32m{n}\033[m')
