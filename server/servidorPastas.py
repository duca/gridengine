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

    nome = os.getlogin() 
    caminhoraiz = '/var/qnint'
    logs = caminhoraiz+'/logs'
    sistema = caminhoraiz+'/bin'
    calculo = caminhoraiz+'/calculos'
    
    diretorios = [nome, caminhoraiz, logs, sistema, calculo]
    
    return diretorios
    

def padrao():
    ''' Gera as pastas padrão que devem haver no cliente. Lembrando que ficam dentro de uma pasta raiz escondida'''
    import os
    import sys

    diretorios = listar()
    caminhoraiz = diretorios[1]
    logs = diretorios[2]
    sistema = diretorios[3]
    calculos = diretorios[4]

    try:
        os.mkdir(caminhoraiz)
    except:
        mensagem = 'Possivelmente ja existe a pasta %s e nao ha necessidade de apagar seu conteudo neste momento \n' %(caminhoraiz)
        sys.stderr.write(mensagem)
    
    try:        
        os.mkdir(logs)
        os.mkdir(sistema)
        os.mkdir(calculos)
        
        print u' \n Seu sistema já contém as pastas necessárias, agora pode cadastrá-lo no grid e começar a contribuir \n'
        
    except:
        mensagem = 'Nao foi possivel criar as sub-pastas necessarias, por favor remova as pasts %s e %s \n' %(logs, sistema)
        sys.stderr.write(mensagem)

        
def criar():
    '''Essa função cria a pasta que conterá os dados da simulação e seu resultado.'''
    import os
    import clienteErros
    
    diretorios = listar()
    calculos = diretorios[4]    
    
        
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
        
    
        
        
    