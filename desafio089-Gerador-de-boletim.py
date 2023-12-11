'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.'''

nota = list()
n1n2 = list()
total = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    nota.append(nome)
    n1n2.append(nota1)
    n1n2.append(nota2)
    nota.append(n1n2[:])
    nota.append(media)
    total.append(nota[:])
    nota.clear()
    n1n2.clear()
    perg = str(input('Quer continuar? [S/N] '))
    if perg in 'Nn':
        break
print('-='*30)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(total):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(total) -1:
        print(f'Notas de {total[opc][0]} são {total[opc][1]}')
print('<<<VOLTE SEMPRE>>>')
    