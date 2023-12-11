'''Variáveis compostas: podem ser de 3 tipos:

A) TUPLAS: Ex.: lanche = ()
B) LISTAS: Ex.: lanche []
C) DICIONÁRIOS: Ex.: lanche {}

OBS.: AS TUPLAS SÃO VARIÁVEIS COMPOSTAS IMUTÁVEIS'''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Pode ser feito da seguinte forma: lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim' (sem o uso dos parênteses)
print(lanche)
print(lanche[1])
print(lanche[-1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print('')

# lanche[1] = 'Refrigerante' --> se mandar dar print em lanche[1], aparecerá uma mensagem de erro, pois tuplas são imu-
# táveis!

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('')

# Outra forma de utilizar tuplas no for:
for cont in range(0, len(lanche)):
    #print(cont) --> vai mostrar a contagem numérica de 0 a 4
    '''print(lanche[cont]) --> vai mostrar os lanches (ou seja, o lanche na posição em que o contador estiver, indo de
zero a 3)'''
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print('')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print('')
print(len(lanche))

print('')
print(sorted(lanche)) # --> organiza o conteúdo da tupla em ordem alfabética
print('')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # --> o comando + em tuplas serve para juntar as tuplas 'a' e 'b'
d = b + a

print(a)
print(b)
print(c)
print(d)
print('')
print(len(c))
print(c.count(5)) # --> conta quantas vezes o número 5 apareceu na tupla c
print(c)
print(c.index(8)) # --> mostra em que posição está o número 8. Se o número estiver repetido, mostra só a primeira
# ocorrência
print(c.index(2, 5)) # --> mostra em que posição está o número 2, começando a contagem da posição 5

print('')
pessoa = ('Pedro', 27, 'M', 90) # --> aceita tanto números quanto letras numa mesma tupla (somente em python)
# del(pessoa) --> deleta da memória a tupla. Serve para apagar qualquer coisa no python
print(pessoa)