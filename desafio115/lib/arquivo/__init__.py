from desafio115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # --> rt = read text (tenta abrir o arquivc para leitura em modo texto). A função
# open() serve para abrir um arquivo.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # --> wt+ = write text (tenta escrever um arquivo de texto, e o + o cria, caso ele não exista).
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        # print(a.read()) # --> comando para ler todo o arquivo. Mudamos esta parte do programa ao longo da resolução
        for linha in a:
            dado = linha.split(';') # --> separa por ;
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # --> at = append text (salva elementos dentro do arquivo de texto)
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n') # --> escreve o nome e idade no arquivo
        except:
            print('Houve um ERRO ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
