#-*- coding: utf-8 -*-

'''
Este módulo é responsável pela preparação do servidor para operar como parte do sistema de cálculo da SBQInt

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''


def listar():
    
    '''funcao usada apenas para armazenar os diretorios em uma lista'''

    import os
    import sys

    nome = os.getenv('LOGNAME') 
    caminhoraiz = '/opt/qnint'
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
            print "Criando a pasta %s" %(pastas)
            os.mkdir(pastas)
        
        except:
            
            mensagem = 'Possivelmente ja existe a pasta %s e nao ha necessidade de apagar seu conteudo neste momento \n' %(pastas)
            sys.stderr.write(mensagem)
    
def remover():
    '''Remove todas as pastas criadas no cliente.'''
    import commands
    import sys
    
    diretorios = listar()
    comando = 'rm -rf ' + diretorios[0]
    
    try:
        print "Removendo a pasta %s" %(diretorios[0])
        commands.getoutput(comando)
        
    except:
        
        sys.stderr.write('Remova manualmente os seguintes diretorios: \n')
        sys.stderr.write(diretorios)
        

def pegarResultado(nome):
    
    diretorios = listar()
    calculos = diretorios[4]
    
    caminho = calculos + '/' + nome #este nome precisa conter a extensão do arquivo
    
    try:
        arquivo = open(caminho, 'r')        
        
        resultado = arquivo.readlines()
        
        return resultado
    
    except:
        
        return None    