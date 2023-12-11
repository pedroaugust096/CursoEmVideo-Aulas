def metade(v = 0):
    return v / 2

def dobro(v = 0):
    return v * 2

def aumentar(v = 0, p = 0):
    valor = v
    perc = p
    result = v + v * p/100
    return result

def diminuir(v = 0, p = 0):
    valor =  v
    perc = p
    result = v - v * p/100
    return result

def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.',',')
