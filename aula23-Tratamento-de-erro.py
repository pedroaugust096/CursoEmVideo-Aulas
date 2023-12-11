'''Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a
estrutura try except no Python de uma forma simples.'''

# Exemplo:

# print(x) --> esta função dará erro, pois a variável x não foi declarada. Não se trata de um erro de sintaxe, mas sim,
# de um erro semântico. Quando isso acontece, ou seja, quando o erro não acontece de forma sintática, ele recebe o nome
# de EXCEÇÃO. Esta exceção, neste caso, recebe o nome de NameError.

# Exemplo 2:

# n = int(input('Número: ))
# print(f'Você digitou o número {n}') --> Este programa, a princípio, funciona normalmente para números. Porém, se a
# pessoa escrever o número por extenso, por exemplo, cai num outro tipo de exceção: ValueError

# Exemplo 3:

# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a/b
# print(f'O resultado é {r}') --> O programa funcionará corretamente, a não ser que o usuário digite o denominador 0.
# Isto cai num terceiro tipo de exceção: ZeroDivisionError. Na matemática, não existe resultado para divisão com
# denominador zero.

# Exemplo 4:

# r = 2/'2' --> Será uma exceção do tipo TypeError. A parcela do denominador não é reconhecida como um número!

# Exemplo 5:

# lst = [3, 6, 4]
# print(lst[3]) --> Ocorrerá uma exceção do tipo IndexError (ou KeyError, no caso dos dicionários), pois não há elemento
# de índice 3, uma vez que a lista lst possui somente os índices zero, um e dois.

# Para resolver todos esses e muitos outros problemas com exceções, utilizamos a estrutura try: except:. Dentro da
# estrutura try inserimos o que geralmente dá problema, ou seja, os comandos que normalmente cairiam em algum tipo de
# exceção. Na estrutura except, colocamos o que acontecerá caso eu tente realizar algo que se encaixe nas exceções de
# cima. Se, por acaso, o try der certo, adiciona-se uma terceira parcela chamada else:, que conterá o que acontece
# quando a condição do try é aceita. Além dessas três cláusulas, existe ainda uma quarta, a finally:. Ela acontecerá
# independente se o try der certo ou se der erro.

# OBS.: As duas últimas cláusulas são OPCIONAIS. Seu uso nem sempre é necessário.()

# Exemplos práticos:
'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except:
    print('Infelizmente tivemos um problema :(')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre, obrigado!')'''

# Exemplificando de outra forma:
'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro: # --> Pode existir um except declarado para cada tipo de erro possível no programa!
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre, obrigado!')'''

# Outro exemplo:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um úmero por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre, obrigado!')
