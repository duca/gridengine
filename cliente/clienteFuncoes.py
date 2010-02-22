#-*- coding: utf-8 -*-

'''
Este módulo contém as funções básicas do programa. Está fora do main por questões de encapsulamento e segurança (os módulos são enviados como arquivos inelegíveis)

:version: 0.0.1
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def cadastrar():
    '''
    Efetiva o cadastro da workstation caso ja nao esteja cadastrada
    '''

    import clienteData
    import clienteDB
    import clienteErros
    import clientePastas
    import sys

    message = 'Seu workstation ja esta cadastrado'
    try:
        caminho = clientePastas.listar()[1] + '/cliente.dll'
        arquivo = open(caminho, 'rb')
        clienteErros('clienteFuncoes.cadastrar', message)
        sys.exit()
        
    except:
        sumario = clienteData.sumario()        
        
        status = clienteData.verificarKey(sumario['key'])
        
        if status == 1:
            sys.stderr.write(message)
            clienteErros('clienteFuncoes.cadastrar', message)
            sys.exit()
        elif status == 0:

            clienteData.persistencia(sumario)
            

            try: 
                servidor = clienteDB.banco()
                servidor.registrarWorkstation(sumario)
                servidor.HeartBeat()
            except: 
                mensagem = u"Nao foi possivel conectar ao servidor. Verifique a conexao e tente mais tarde"
                clienteErros.registrar('clienteDB.reconectar', mensagem)
                sys.exit()
            

    
def remover():
    
    import clientePastas
      
    clientePastas.remover()

def preparar():
    
    import clientePastas
    
    clientePastas.criar()
    
def offline():
    
    import clienteDB
    

def versao(argumentos):
    
    print "Versao 0.0.1"
    
def iniciar():
    
    import clienteIniciar
    
    clienteIniciar.loopPrincipal()    