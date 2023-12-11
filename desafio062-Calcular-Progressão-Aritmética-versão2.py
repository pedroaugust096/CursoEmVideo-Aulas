'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
ele disse que quer mostrar 0 termos'''

print('Gerador de PA')
print('-='*8)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
termo = a1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} ➔ '.format(termo), end ='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrador.'.format(total))
