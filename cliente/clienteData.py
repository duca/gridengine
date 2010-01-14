#-*- coding:utf-8 -*-

'''
Este modulo contem as funcoes usadas para mapear a carga do cliente, hostname e ip. Nenhuma aceita variaveis de entrada 

:version: 0.0.1
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def Datetime():
    
    import commands
    import clienteErros
    import sys
    
    try:
        string = commands.getoutput('date')
    except:
        message = 'Nao foi possivel levantar a data e a hora atuais.'
        sys.stderr.write(message)
        clienteErros.registrar('clienteData.Datetime', message)
    return string
        
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
    import commands
    
    nome = 'NomePadrao'
    
    try: 
        
        nome = commands.getoutput('/bin/uname -a')
        
    except:
        
        try:
            
            nome = commands.getoutput('uname -a')
            
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
        
def nucleos():
    import multiprocessing
    import os
    import sys
    import clienteErros
    
    try:
        cores = os.sysconf("SC_NPROCESSORS_ONLN")
        cores_alt = multiprocessing.cpu_count()
        if cores_alt == cores:
            core = cores_alt
        return core
    except:
        message = "Nao foi possivel estabelecer o numero de nucleos no computador. Favor definir a variavel de ambiente SC_NPROCESSORS_ONLN = (numero de nucleos no sistema) e tente novamente"
        os.stderr.write(message)
        clienteErros.registrar("clienteData.nucleos", message)
        sys.exit()
        
def ram():
    
    import os
    import sys
    import clienteErros
    
    try:
        memoria = os.popen("free -m").readlines()[1].split()[1]
        return int(memoria)
    except:
        message = "Nao foi possivel obter informacao de quanta ram ha no sistema, essa informacao é importante para o Grid e portanto seu workstation nao foi adicionado ainda. Tente novamente mais tarde"
        sys.stderr.write(message)
        clientesErros.registrar('clienteData.ram', message)
        sys.exit()
    
    
def sumario():
    import Chave
    
    key = Chave.gerar(5)
    nome = hostname()
    datahora = Datetime()
    IP = pegarIP()
    cpus = nucleos()
    sisram = ram()    
    tudo = {'key' : key, 'nome' : nome, 'IP': IP, 'nucleos' : cpus, 'ram' : sisram, 'datetime' : datahora}
    
    return tudo

def normal():
    
    import clientePastas
    import clienteErros
    import base64
    import sys
    
    try:
        caminho = clientePastas.listar()[1] + '/servidor.dll'
        arquivo = open('servidor.dll', 'rb')
    except:
        mensagem = 'Nao foi possivel encontrar o arquivo %s ou o mesmo esta corrompido' %(caminho)
        sys.stderr.write(mensagem)
        clienteErros.registrar('clienteData.normal', mensagem)
        sys.exit()   
        
    
    conteudo = base64.b64decode(arquivo.read())
    
    return conteudo

def sbp():
    
    import Chave
    
    dado = Chave.padrao()
    
    return dado
    

def verificarKey(chave):
    
    import clienteDB
    
    querysql = "select NodeKey from Nodes"
            
    dados = sbp()
    servidor = clienteDB.banco(dados[0], dados[1], dados[2])
    servidor.conectar()

    chaves = servidor.fetchAll(querysql)
    servidor.Desconectar()
    
    for results in chaves: #loop por toda a lista de resultadods
        
        
        if chave == chaves:
            
            confere = 'sim'
            
            break
        
        else:            
          
            confere = 'nao'
                    
    return confere 

def persistencia(dados):
    
    import clientePastas
    import clienteErros
    import Chave
    
    try:
        caminho = clientePastas.listar()[1] + '/cliente.dll'
        arquivo = open(caminho, 'wb')
        
        arquivo.write(Chave.codificar(dados))
        
        arquivo.close()
        
    except:
        
        mensagem = 'Nao foi possivel encontrar o arquivo %s ou o mesmo esta corrompido' %(caminho)
        sys.stderr.write(mensagem)
        clienteErros.registrar('clienteData.persistencia', mensagem)
        sys.exit()  
        
    
    