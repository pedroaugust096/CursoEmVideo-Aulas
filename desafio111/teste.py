'''Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado. Transfira todas as
funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.'''
from desafio111.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 30)
