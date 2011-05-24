#-*- coding:utf-8 -*-

'''
Este modulo cuida do registro dos logs do programa e está divido em funcoes para criar os arquivos e os preencher

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''
   
def registrar(nomeDaFuncao, mensagem):
    
    from datetime import datetime
    import servidorPastas
    import sys
    
    
    diretorios = servidorPastas.listar()
    sisLog = diretorios[1]+'/erros.log'
    
    try:
        registro = open(sisLog, 'a')

    except:
        
        servidorPastas.criar()

    
    timestamp = datetime.now()
    separadorHora = ":"
    separadorData = "/"
    
    
    horario = str(timestamp.hour) + separadorHora + str(timestamp.minute) + " " + str(timestamp.day) + separadorData + str(timestamp.month) + separadorData + str(timestamp.year)
    
    mensagem = horario + " Funcao: " + nomeDaFuncao + " Mensagem: " + mensagem + "\n"
    
    try:
        registro.write(mensagem)
        
    except:
        
        servidorPastas.remover()
        servidorPastas.criar()
        
        try:
            registro.write(mensagem)
        except:
            erro = horario + "Nao foi possivel registrar o evento de erro " + erro + ", entretanto o programa tentara seguir assim mesmo \n"
            sys.stderr.write(mensagem)

        
    
    
    
    