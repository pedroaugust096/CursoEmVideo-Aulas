'''FUNÇÕES (PARTE 2)
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, 
o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções 
Python, escopo de variáveis e retorno de resultados.'''

# Utilizando o interactive help.
# Supondo que o usuário não saiba para que serve o comando print. Método para aprender com o interactive help:

help(print) # --> isto serve para qualquer comando

# Fazendo o mesmo, agora com o comando input, mas utilizando o .__doc__:

print('\nPara o comando input:')
print(input.__doc__)
help(input)

# DOCSTRINGS: são, literalmente, strings de documentação. Quando o usuário utiliza a função help(input), por exemplo,
# o python retorna a docstring do comando input, ou seja, o manual deste comando.

# Acessando a docstring de uma função criada pelo usuário. Para isso, devemos cadastrar a docstring da função
# criada por nós. Para isso, devemos abrir aspas duplas três vezes logo na linha abaixo do comando def e descrever
# o funcionamento da função, ou seja, escrever seu manual:

def contador(i, f, p):
    """
    
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


print()
help(contador) # --> se somente for utilizado este comando sem descrever o funcionamento do programa, o mesmo 
# não retornará a descrição da função, somente mostrará a quantidade de parâmetros que ela possui.

# PARÂMETROS OPCIOAIS: Trata-se de uma função que funcione, por exemplo, somando 5 parâmetros. Porém, caso 
# o usuário insira apenas 3 parâmetros, ela continue funcionando. Exemplificando:
def somar(a=0, b=0, c=0): # --> Isto significa que, se por acaso a função não receber valor para a, b ou 
# c, ele valerá zero
    """_Sumário:
        --> Faz a soma de três valores e mostra o resultado na tela.

    Args:
        a (int, opcional): O primeiro valor. Defaults to 0.
        b (int, opcional): O segundo valor. Defaults to 0.
        c (int, opcional): O terceiro valor. Defaults to 0.
    """
    s = a + b + c
    print(f'A soma vale {s}')


print('\nParâmetros opcionais:')
help(somar)    
somar(3, 2, 5)
somar(8, 4)
somar(b=4, c=2)
somar()

# ESCOPO DE VARIÁVEIS: Escopo diz respeito ao local onde a variável vai existir, e o local onde ela não vai mais 
# existir. Exemplo:


# Programa Principal
def teste():
    x = 8 # --> Variável Local (declarada dentro da função)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
    
    
n = 2 # --> Variável Global. Mesmo com o n sendo declarado após a função, ele funciona dentro de toda 
# a área do programa. Isto é o Escopo Global
print()
print(f'No programa principal, n vale {n}')
teste()
# print(f'No programa principal, x vale {x}') --> Este print dará erro, porque a variável x existe somente
# dentro da função teste. Ou seja, x tem um Escopo Local (só funciona dentro da função).

print()
def teste(b):
    # OBS.: Se criarmos uma variável a aqui, ela será diferente da a global lá de baixo.
    # Ou seja, existirá uma variável a local (aqui) e uma variável a global (lá em baixo).
    
    # global a --> Se escrevermos isto, nós dizemos ao python para não criar uma variável a local,
    # e sim, para ele utilizar o a global, que passará a ser 8 lá em baixo.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}') # --> Tudo que está até aqui faz parte do Escopo Local
    

# Programa Principal: --> O que está daqui para baixo faz parte do Escopo Global  
a = 5
teste(a)
print(f'\nA fora vale {a}')
# print(f'B fora vale {b}') --> Não funcionará, porque b é uma variável local (só funciona lá no def)
# print(f'C fora vale {c}') --> Não funcionará, porque c é uma variável local (só funciona lá no def)

# OBS.: Existe escopo de chamada de biblioteca (função local e função global). Este conteúdo será explicado 
# nos exercícios (iniciativa via)


# RETORNO DE VALORES: As funções em python podem retornar ou não retornar valores. Para isso, utiliza-se
# o return. Fazendo isso no exemplo da função somar(). Ex.:

print()
def somar(a=0, b=0, c=0):
    s = a + b + c
    # print(f'A soma vale {s}') --> será substituído por:
    return s
    
    
r1 = somar(3, 2, 5)
r2 = somar (2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

# PARTE PRÁTICA: Criar uma função que calcule o fatorial de um número e o retorne ao programa principal para que ele 
# mostre o resultado na tela

print()
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f # --> não serve apenas para números. Pode receber valores literais (uma frase), reais, devolver listas,
# dicionários, tuplas, etc.


# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}.')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')     

print()
def par(n=0):
    if n%2==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
