'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressao
usando a estrutura while'''

print('Gerador de PA')
print('-='*8)
c = 0
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
ac = 0
while c < 10:
    ac = a1+r*c
    print('{}'.format(ac), end ='')
    print(' ➔ ', end='')
    c += 1
print('FIM')

