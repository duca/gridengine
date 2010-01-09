#-*- coding:utf-8 -*-

'''
Este modulo contem as funcoes usadas para mapear a carga do cliente, hostname e ip. Nenhuma aceita variaveis de entrada 

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def Carga():
    
    '''funcao usada para levantar a carga media em 5min da cpu '''
    
    import commands
    import os
    import clienteErros
    
    try:
        output = os.getloadavg()
        carga = output[2]
        return carga
    except:
        mensagem = 'impossivel obter a carga de uso em seu equipamento. Ele nao podera ser incluido no Grid-QNInt ate resolvermos esse problema. \n'
        sys.stderr.write(mensagem)
        clienteErros.registrar('clienteData.carga', mensagem) #registra o erro no log do programa

    
def hostname():
    '''Esta funcao detecta o hostname do pc'''
    import os
    
    nome = 'NomePadrao'
    
    try: 
        
        nome = os.getoutput('/bin/uname -a')
        
    except:
        
        try:
            
            nome = os.getoutput('uname -a')
            
        except:
            
            nome = os.getoutput('/sbin/uname -a')
    return nome

def pegarIP():
    
    '''Esta funcao detecta qual e o verdadeiro endereco ip com o qual a maquina acessa a internet atraves do que o site www.qualmeuip.net retorna ao acessa-la atraves do python'''
     
    import urllib #biblioteca padrao para manipular url's
    import sys
    import clienteErros
    
    try:
        conexao = urllib.urlopen("http://www.qualmeuip.net") #acessando a pagina
        conteudo = conexao.readlines() #copiando todo o conteudo da pagina
        linha = conteudo[66] #linha 66
        #entre as marcacoes <strong> e </strong>
        inicio = linha.find('g>') 
        fim = linha.find('</') 
        inicio = inicio + 2 #acerto dos caracteres
        ip = linha[inicio:fim]

        return ip

    
    except:
        #escreve a mensagem de erro na saida de erro padrao
        mensagem = 'sem conexao com a internet. Seu equipamento nao podera ser acessado pelo GRID-QNInt ate resolver esse problema. \n'
        sys.stderr.write(mensagem)
        #registra o erro no log
        clienteErros.registrar('clienteData.pegarIP', mensagem)
        
    
def gerarNodeKey():
    
    import sys    
    import clienteData
    import clienteErros
    import clienteDB
    import chave

    
    tamanho = 10
    try:
        NodeKey = chave.gerar(tamanho)
    except:
        mensagem = 'Nao foi possivel gerar a chave para este Nodo'
        clienteErros.registrar('clienteDB.gerarNodeKey', mensagem)
        sys.stderr.write(mensagem)
        
    
def verificarKey(chave):
    
    import clienteDB
    
    querysql = "select NodeKey from Nodes"
            
    chaves = clienteDB.fetchAll(querysql)
            
             
    for results in chaves: #loop por toda a lista de resultadods
        
        
        if chave == chaves:
            
            confere = 'sim'
            
            break
        
        else:            
          
            confere = 'nao'
                    
    return confere 

        
        
    
    