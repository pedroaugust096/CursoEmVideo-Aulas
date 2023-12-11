'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

lista = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 
        'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba','Avaí',
        'Ponte Preta', 'Atlético-GO')
print('-='*15)
print(f'Lista de times do Brasileirão: {lista}')
print('-='*15)
print(f'Os 5 primeiros times são {lista[0:5]}')
print('-='*15)
print(f'Os 4 últimos times são {lista[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('-='*15)
print(f'O Chapecoense está na {lista.index("Chapecoense")+1}ª posição')
