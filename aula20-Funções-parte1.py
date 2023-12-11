'''FUNÇÕES (PARTE 1)
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. 
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.'''

def lin():
    print('-' * 30)
    

# Programa principal --> É o programa propriamente dito. Devemos sempre deixar, ao menos, 2 linhas de distância entre
# a sintaxe de criação da função (trecho de cima) e o programa principal.
# Exemplos básicos de criação de funções:
lin()
print(f'{"CURSO EM VÍDEO":^30}')
print(f'{"APRENDA PYTHON":^30}')
lin()

# Ex2:
def mensagem(msg):
    print('-' * 30)
    print(msg) # --> msg é um parâmetro da função mensagem
    print('-' * 30)


print()
mensagem(f'{"SISTEMA DE ALUNOS":^30}') # --> Só utilizamos {} para fazer a mensagem 'sistema de alunos'
# aparecer centralizada

# Ex3:

'''a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

Fazendo em funções:'''

#def soma(a, b):
#    s = a + b
#    print(s)


# Programa principal
# print()
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)

# também pode ser executado da seguinte forma:
# soma(a=4, b=5) # --> Retornará o mesmo resultado que a primeira chamada da função soma

# Fazendo de outra maneira:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# Programa principal
print()
soma(4, 5)
print()
soma(a=4, b=5)
print()
soma(b=4, a=5)
# Se colocarmos: soma(b=5, 4) --> Vai dar erro. Se chamou uma letrinha (especificou argumento), tem que chamar
# todas (especificar todos os argumentos).

# Empacotamento de parâmetros: def contador(*núm): --> este asterisco é o desempacotador, ou seja, quando 
# inserimos ele no argumento da função, estamos dizendo pro python para ele pegar diversos argumentos e salvá-los
# no argumento núm. Ex.:
def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')



print()
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def cont2(* n):
    tam = len(n)
    print(f'Recebi os valores {n} e são ao todo {tam} números.')


print()
cont2(2, 1, 7)
cont2(8, 0)
cont2(4, 4, 7, 6, 2)

# Ex.: (Este exemplo não é de desempacotamento):
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


print()
valores = [7,2,5,0,4]
dobra(valores)
print(valores)
