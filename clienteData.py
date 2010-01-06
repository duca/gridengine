#-*- coding:utf-8 -*-

'''
Este modulo contem as funcoes usadas para mapear a carga do cliente, hostname e ip. Nenhuma aceita variaveis de entrada 

desenvolvido por Eduardo Martins Lopes < edumlopes at gmail dot com >
'''

def carga():
    
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
    #a
    

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
        
    
    

    
        
        
    
    