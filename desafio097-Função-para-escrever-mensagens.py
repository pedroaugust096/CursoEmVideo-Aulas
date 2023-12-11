'''Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) Saída: 
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~'''
def escreva(msg):
    tam = len(msg)
    print(f'~' * (tam+4))
    print(f'  {msg}')
    print(f'~' * (tam +4))


escreva('Pedro Augusto')
escreva('Teste')
escreva('Escrevendo mensagens')
