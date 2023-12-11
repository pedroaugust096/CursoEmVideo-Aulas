'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial.'''
def fatorial(num=1, show=False):
    """ --> Função que calcula o fatorial de um número.

    Args:
        num (int, opcional): Número do qual se deseja calcular o fatorial. Defaults to 1.
        show (bool, opcional): Se declarado, mostra a memória de cálculo da função. Defaults to False.

    Returns:
        O valor do Fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
  
        
# Programa principal:
print(fatorial(4, show=True))
# help(fatorial)
