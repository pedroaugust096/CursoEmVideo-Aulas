'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua ca-
tegoria, de acordo com a idade:

[-] Até 9 anos: MIRIM
[-] Até 14 anos: INFANTIL
[-] Até 19 anos: JÚNIOR
[-] Até 25 anos: SÊNIOR 
[-] Acima de 25 anos: MASTER'''

from datetime import date

atual = date.today().year
nasc = int(input('Digite em que ano você nasceu: '))
ano = atual - nasc

if ano >= 0 and ano <= 9:
    print('\nSua categoria é: MIRIM')

elif ano > 9 and ano <=14:
    print('\nSua categoria é: INFANTIL')

elif ano > 12 and ano <=19:
    print('\nSua categoria é: JÚNIOR')

elif ano > 19 and ano <= 25:
    print('\nSua categoria é: SÊNIOR')

elif ano >= 25:
    print('\nSua categoria é: MASTER')

else:
    print('\nERRO! Digite uma data válida!')