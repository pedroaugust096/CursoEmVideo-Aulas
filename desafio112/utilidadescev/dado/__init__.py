from desafio112.utilidadescev import moeda


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)


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
