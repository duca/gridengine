#-*- coding: utf-8 -*-

'''
Este módulo é responsável pela preparação do cliente para operar como parte do sistema de cálculo da SBQInt

desenvolvido por Eduardo Martins Lopes < edumlopes at gmail dot com >
'''


def listar():
    
    '''funcao usada apenas para armazenar os diretorios em uma lista'''

    import os
    import sys

    nome = os.getlogin() 
    caminhoraiz = '/home/'+nome+'/.qnint'
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

        
def criar(usuario):
    '''Essa função cria a pasta que conterá os dados da simulação e seu resultado.'''
    import os
    import clienteErros
    
    diretorios = listar()
    calculos = diretorios[4]    
    
    resultados = calculos + '/' + usuario
    
    try:
        os.mkdir(resultados)
    except: 
        mensagem = 'nao foi possivel criar a pasta para o usuario %s' %(usuario)
        clienteErros.registrar('clientePastas.criar', mensagem)
        
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
        


        
        
        
    