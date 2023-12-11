'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
jog = dict()
gols = list()
lista = list()
while True:
    jog.clear()
    jog['nome'] = str(input('Nome do Jogador: '))
    part = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    gols.clear()
    for c in range(0, part):
        gols.append(int(input(f'   Quantos gols na partida {c+1}? ')))
        c += 1
    jog['gols'] = gols[:]
    jog['total'] = sum(gols)
    lista.append(jog.copy())
    while True:
        perg = str(input('Quer continuar? [S/N] ')).upper()[0]
        if perg in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if perg == 'N':
        break
print('-=' * 40)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
print('_' * 40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    elif dados >= len(lista):
        print(f'ERRO! Não existe jogador com código {dados}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[dados]["nome"].upper()}: ')
        for i, g in enumerate(lista[dados]["gols"]):
            print(f'   No jogo {i+1}, fez {g} gols.')
print('<< VOLTE SEMPRE >>')
        