'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já do tempo do alistamento. Seu programa também deverá
mostrar o tempo que falta ou que passou do prazo'''

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = abs(atual - nasc)
dif = abs(18 - idade)

if (atual - nasc) < 18:

    aalist = atual + dif
    print('''\nQuem nasceu em {} tem {} anos em {}.
Ainda faltam {} anos para o alistamento.
Seu alistamento será em {}.'''.format(nasc, idade, atual, dif, aalist))

elif (atual - nasc) == 18:
    print('''\nQuem nasceu em {} tem {} anos em {}.
Você deve se alistar IMEDIATAMENTE!'''.format(nasc, idade, atual))

else:
    aalist = atual - dif
    print('''\nQuem nasceu em {} tem {} anos em {}.
Você já deveria ter se alistado há {} anos!
Seu alistamento foi em {}!'''.format(nasc, idade, atual, dif, aalist))