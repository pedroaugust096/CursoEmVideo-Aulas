'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site Pudim não está acessível no momento.')
else:
    print('\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m')
    print(site.read())
