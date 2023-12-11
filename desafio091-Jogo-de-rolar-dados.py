'''Crie um programa onde 4 jogadores jogue um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter # --> Função que serve para ordenar um dicionário baseado em algum valor dentro deste
c = 0
dado = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6)}
ranking = dict() # --> Criamos um dicionário vazio, pois precisamos jogar o dicionário 'dados' dentro deste aqui para sortear os vencedores. Também pode ser usado como lista
print('\nValores sorteados:')
for k, v in dado.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print()
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True) # --> Ordena o dicionário ranking usando os valores de
# dado.item(), ou seja, suas keys e seus values, utilizando como chave o itemgetter na parte 1 (os valores das jogadas,
# os randints).
for i, v in enumerate(ranking):
    print(f'   {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
