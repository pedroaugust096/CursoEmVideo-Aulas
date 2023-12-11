'''Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segudo valor: '))
fim = False
while not fim:
    opção = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
>>>>> Qual é a sua opção? '''))
    if opção == 5:
        fim = True
    else:
        if opção <= 0 or opção > 5:
            print('Opção inválida, tente novamente')
            print('=-='*10)
            sleep(1.5)
        elif opção == 1:
            print('A soma entre {} + {} é {}'.format(n1, n2, n1+n2))
            print('=-='*10)
            sleep(1.5)
        elif opção == 2:
            print('O resultado de {} x {} é {}'.format(n1, n2, n1*n2))
            print('=-='*10)
            sleep(1.5)
        elif opção == 3:
            if n1 > n2:
                print('Entre {} e {}, o maior valor é {}'.format(n1, n2, n1))
                print('=-='*10)
                sleep(1.5)
            elif n1 < n2:
                print('Entre {} e {}, o maior valor é {}'.format(n1, n2, n2))
                print('=-='*10)
                sleep(1.5)
            else:
                print('Os valores {} e {} são os mesmos'.format(n1, n2))
                print('=-='*10)
                sleep(1.5)
        elif opção == 4:
            print('Informe os números novamente: ')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
print('Finalizando...')
print('=-='*10)
sleep(1.5)
print('Fim do programa! Volte sempre!')
