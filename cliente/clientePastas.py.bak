#-*- coding: utf-8 -*-

'''
Este módulo é responsável pela preparação do cliente para operar como parte do sistema de cálculo da SBQInt

desenvolvido por Eduardo Martins Lopes < edumlopes at gmail dot com >
'''


def listar():
    
    '''funcao usada apenas para armazenar os diretorios em uma lista'''

    import os
    import sys

    nome = os.getenv('LOGNAME') 
    caminhoraiz = '/home/'+nome+'/qnint'
    logs = caminhoraiz+'/logs'
    sistema = caminhoraiz+'/bin'
    calculo = caminhoraiz+'/calculos'
    
    diretorios = [nome, caminhoraiz, logs, sistema, calculo]
    
    return diretorios
    

def criar():
    ''' Gera as pastas padrão que devem haver no cliente. Lembrando que ficam dentro de uma pasta raiz escondida'''
    import os
    import sys

    diretorios = listar()
        
    for pastas in diretorios:
        
        try:
            os.mkdir(pastas)
        except:
            mensagem = 'Possivelmente ja existe a pasta %s e nao ha necessidade de apagar seu conteudo neste momento \n' %(pastas)
            sys.stderr.write(mensagem)
        
        
def remover():
    '''Remove todas as pastas criadas no cliente.'''
    import commands
    import sys
    
    diretorios = listar()
    comando = 'rm -r ' + diretorios[1]
    
    try: 
        commands.getoutput(comando)
        
    except:
        
        sys.stderr.write('Remova manualmente os seguintes diretorios: \n')
        sys.stderr.write(diretorios)    