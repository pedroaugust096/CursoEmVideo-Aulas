'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade'''


def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar este número.\033[m')
            return 0
        else:
            return i


def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m\nUsuário preferiu não digitar este número.\033[m')
            return 0
        else:
            return r



i = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
