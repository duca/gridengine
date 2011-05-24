#-*- coding: utf-8 -*-



#imports  

import sys
import argParser
import servidorPrincipal
import servidorPastas
import sys
import os

username = os.getenv('LOGNAME')
raiz = servidorPastas.listar()[1]

try:
    arquivo = raiz + '/teste.dat'
    teste = open(arquivo, 'w')
except:
    mensagem = u' \n \n Este programa precisa ser executado com um usuario que possa criar e movimentar a pasta %s. Funcionaria essa pasta fosse criada manualmente e seus privilegios fossem atribuido ao usuario atual (%s) ou outro em cujo ambiente sera executado este programa. \n \n' %(raiz, username)
    sys.stderr.write(mensagem)
    sys.exit()

status = argParser.Processar(sys.argv)

if status == False: #Não iniciar o serviço
    
    sys.exit()
    
elif status == True: #Iniciar o serviço
    #início do loop principal
    
    mensagem = "Para parar o servidor, remova o arquivo /opt/qnint/qnint.pid ou use os métodos mais tradicionais"
    
    print mensagem
    servidorPrincipal.Loop()
    
    print "O servidor foi terminado com sucesso!"
    


