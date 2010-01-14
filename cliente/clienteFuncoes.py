#-*- coding: utf-8 -*-

'''
Este módulo contém as funções básicas do programa. Está fora do main por questões de encapsulamento e segurança (os módulos são enviados como arquivos inelegíveis)

:version: 0.01
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

    
    try:
        caminho = clientePastas.listar()[1] + '/cliente.dll'
        arquivo = open(caminho, 'rb')
        message = 'Seu workstation ja esta cadastrado'
        sys.stderr.write(message)
        clienteErros('clienteFuncoes.cadastrar', message)
        sys.exit()
        
    except:
        
        sumario = clienteData.sumario()
        clienteData.persistencia(sumario)
      
    
    disponibilidade = 1
    dados = clienteData.sbp()
    servidor = clienteDB.banco(dados[0], dados[1], dados[2])
    
    querysql = 
    {'key' : key, 'nome' : nome, 'IP': IP, 'nucleos' : cpus, 'ram' : sisram}

def iniciar():
    du = ' '

def descadastrar():
    
    du = ' '

def preparar():
    
    du = ' '




def versao(argumentos):
    
    du = ' '