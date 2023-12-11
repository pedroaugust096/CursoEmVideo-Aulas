'''DICIONÁRIOS: variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais. Ex.:'''
pessoas = {'nome' : 'Pedro', 'sexo' : 'M', 'idade' : 27}
print()
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()

# Para acessar as chaves, valores ou itens utilizando laços:
for k in pessoas.keys():
    print(k)

print()   
for v in pessoas.values():
    print(v)

print()
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
del pessoas['sexo'] # --> deleta a key sexo e o value associado a ela
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
pessoas['nome'] = 'Leandro' # --> modifica o value atrelado à key nome
for k, v in pessoas.items():
    print(f'{k} = {v}')
    
print()
pessoas['peso'] = 91 # --> para adicionar um elemento ao dicionário
for k, v in pessoas.items():
    print(f'{k} = {v}')

# Criando um dicionário dentro de uma lista:
print()
brasil = list()
estado1 = {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf' : 'São Paulo', 'sigla' : 'SP'}

# OBS.: Neste caso, para adicionarmos os dicionários estado1 e estado2 à lista brasil, devemos usar o append(),
# pois é a lista quem receberá os 2 dicionários, então usamos o método de adição de elementos referente às listas
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

# Mais exemplos. Como fazer uma cópia de um elemento de um dicionário
# OBS.: Os dicionários não aceitam a utilização do [:] para fazer cópia de elementos, pois esta variável
# composta não aceita fatiamento, como é o caso das listas. Para dicionários, utiliza-se o método copy()
print()
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # -> Traduzindo: adiciona à lista brasil uma cópia dos elementos do dicionário estado
print(brasil)

print()
for e in brasil: # --> for utilizado para "varrer" a lista
    for k, v in e.items(): # --> for utilizado para mostrar os itens dos dicionários
        print(f'O campo {k} tem valor {v}')
