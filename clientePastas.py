#-*- coding: utf-8 -*-

'''Este módulo é responsável pela preparação do cliente para operar como parte do sistema de cálculo da SBQInt'''


def listar():
    
    '''funcao usada apenas para armazenar os diretorios em uma lista'''

    import os
    import sys

    nome = os.getlogin() 
    caminhoraiz = '/home/'+nome+'/.qnint'
    logs = caminhoraiz+'/logs'
    sistema = caminhoraiz+'/bin'
    
    diretorios = [nome, caminhoraiz, logs, sistema]
    
    return diretorios
    

def criar():
    
    import os
    import sys

    diretorios = listar()
    caminhoraiz = diretorios[1]
    logs = diretorios[2]
    sistema = diretorios[3]

    try:
        os.mkdir(caminhoraiz)
    except:
        mensagem = 'Possivelmente ja existe a pasta %s e nao ha necessidade de apagar seu conteudo neste momento \n' %(caminhoraiz)
        sys.stderr.write(mensagem)
    
    try:        
        os.mkdir(logs)
        os.mkdir(sistema)
        
    except:
        mensagem = 'Nao foi possivel criar as sub-pastas necessarias, por favor remova as pasts %s e %s \n' %(logs, systema)
        sys.stderr.write(mensagem)

def remover():
    
    import commands
    import sys
    
    diretorios = listar()
    comando = 'rm -r ' + diretorios[1]
    
    try: 
        commands.getoutput(comando)
        
    except:
        
        sys.stderr.write('Remova manualmente os seguintes diretorios: \n')
        sys.stderr.write(diretorios)
        
        
    