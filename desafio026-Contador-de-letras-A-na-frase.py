'''Faça um programa que leia uma frase pelo teclado e mostre:
1) Quantas vezes aparece a letra "A"
2) Em que posição ela aparece a primeira vez
3) Em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ')).strip().lower()
print('Na sua frase a letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))
