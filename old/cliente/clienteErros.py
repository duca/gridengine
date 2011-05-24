#-*- coding:utf-8 -*-

'''
Este modulo cuida do registro dos logs do programa e está divido em funcoes para criar os arquivos e os preencher

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''
   
def registrar(nomeDaFuncao, mensagem):
    
    from datetime import datetime
    import clientePastas
    import sys
    
    
    diretorios = clientePastas.listar()
    sisLog = diretorios[2]+'/erros.log'
    
    try:
        registro = open(sisLog, 'a')

    except:
        
        clientePastas.criar()

    
    timestamp = datetime.now()
    separadorHora = ":"
    separadorData = "/"
    
    
    horario = str(timestamp.hour) + separadorHora + str(timestamp.minute) + " " + str(timestamp.day) + separadorData + str(timestamp.month) + separadorData + str(timestamp.year)
    
    mensagem = horario + " Funcao: " + nomeDaFuncao + " Mensagem: " + mensagem + "\n"
    
    try:
        registro.write(mensagem)
        sys.stderr.write(mensagem)
        
    except:
        clientePastas.criar()
        
        try:
            registro.write(mensagem)
        except:
            erro = horario + u"Nao foi possivel registrar o evento de erro " 
            sys.stderr.write(erro)
            erro = mensagem 
            sys.stderr.write(erro)
            erro = u", entretanto o programa tentara seguir assim mesmo."
            sys.stderr.write(erro)      