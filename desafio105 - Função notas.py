'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um 
dicionário com as seguintes informações:

– Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)
'''
def notas(* n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.

    Args:
        n: uma ou mais notas dos alunos (aceita várias).
        sit: valor opcional, indicando se deve ou não adicionar a situação.
        return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit == True:
        if r['média'] < 5:
            r['situação'] = 'RUIM'
        elif r['média'] < 7:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'BOA'
    return r
  

# Programa principal
print()
resp = notas(5.5, 9.5, 6.5, 10, sit=True)
print(resp)
