def metade(v = 0, format = True):
    """-> Calcula a metade de um valor monetário informado pelo usuário. 

    Args:
        v (int, optional): Parâmetro valor. Defaults to 0.
        format (bool, optional): Indica se o resultado será formatado como moeda ou não. Defaults to True.

    Returns:
        Retorna a metade do valor informado pelo usuário.
    """
    res = v / 2
    return res if format is False else moeda(res)

def dobro(v = 0, format = True):
    """-> Calcula o dobro de um valor monetário informado pelo usuário. 

    Args:
        v (int, optional): Parâmetro valor. Defaults to 0.
        format (bool, optional): Indica se o resultado será formatado como moeda ou não. Defaults to True.

    Returns:
        Retorna o dobro do valor informado pelo usuário.
    """
    res = v * 2
    return res if format is False else moeda(res)

def aumentar(v = 0, p = 0, format = True):
    """-> Aumenta o valor informado a um percentual qualquer também informado pelo usuário.

    Args:
        v (int, optional): Parâmetro valor. Defaults to 0.
        p (int, optional): Parâmetro percentual, escrito de forma inteira e sem o símbolo %. Defaults to 0.
        format (bool, optional): Indica se o resultado será formatado como moeda ou não. Defaults to True.

    Returns:
        Retorna o resultado do valor informado acrescido do percentual informado pelo usuário.
    """
    valor = v
    perc = p
    result = v + v * p/100
    return result if format is False else moeda(result)

def diminuir(v = 0, p = 0, format = True):
    """-> Diminui o valor informado a um percentual qualquer também informado pelo usuário.

    Args:
        v (int, optional): Parâmetro valor. Defaults to 0.
        p (int, optional): Parâmetro percentual, escrito de forma inteira e sem o símbolo %. Defaults to 0.
        format (bool, optional): Indica se o resultado será formatado como moeda ou não. Defaults to True.

    Returns:
        Retorna o resultado do valor informado decrescido do percentual informado pelo usuário.
    """
    valor =  v
    perc = p
    result = v - v * p/100
    return result if format is False else moeda(result)
def moeda(v=0, moeda='R$'):
    """-> Formata como moeda o valor inserido pelo usuário.

    Args:
        v (int, optional): Parâmetro valor. Defaults to 0.
        moeda (str, optional): Parâmetro moeda. Indica a simbologia de qual unidade monetária a função retornará. Defaults to 'R$'.

    Returns:
        Returna o valor inserido pelo usuário formatado conforme a unidade monetária definida por ele.
    """
    return f'{moeda}{v:.2f}'.replace('.',',')

def resumo(p, aum, dim):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(p):>12}')
    print(f'Dobro do preço: {dobro(p, True):>13}')
    print(f'Metade do preço: {metade(p, True):>12}')
    print(f'{aum:>2}% de aumento: {aumentar(p, aum, True):>13}')
    print(f'{dim:>2}% de redução: {diminuir(p, dim, True):>13}')
    print('-' * 30)
