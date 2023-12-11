# int() - função para números inteiros
# float() - função para números reais (números flutuantes, ou decimais etc)
# bool() - função para valores booleanos (Verdadeiro ou Falso). Sempre deve aparecer o True ou False com letra maiúscula
# str() - função para string: recebe dígitos, texto etc, desde que estejam entre aspas


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
# print('A soma entre {}'.format(n1),'e {}'.format(n2), 'vale',s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
