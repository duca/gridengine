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

    message = u'Seu workstation já está cadastrado'
    try:
        caminho = clientePastas.listar()[1] + '/cliente.dll'
        arquivo = open(caminho, 'rb')
        sys.stderr.write(message)
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
            dados = sbp()
            servidor = clienteDB.banco(dados[0], dados[1], dados[2])
            try: 
                servidor.conectar()
                servidor.registrarWorstation(sumario)
            except: 
                mensagem = u"Não foi possível conectar ao servidor. Verifique a conexão e tente mais tarde"
                clienteErros.registrar('clienteDB.conectar', mensagem)
                sys.exit()
            

    
def descadastrar():
    
    du = ' '

def preparar():
    
    import clientePastas
    
    clientePastas.padrao()

def versao(argumentos):
    
    print "Versao 0.0.1"
    
def iniciar():
    
    import clienteIniciar
    
    clienteIniciar.loopPrincipal()

    