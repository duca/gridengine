#-*- coding: utf-8 -*-

'''
:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def compactar(usuario):
    
    import tarfile
    import clientePastas
    import sys
    from clienteErros import registrar
    
    diretorios = clientePastas.listar()
    resultados = diretorios[4] + '/' + usuario
    nomedoarquivo = resultados + '.tar'
    
    try:

        arquivo = tarfile.open(nomedoarquivo, 'w')
        arquivo.add(resultados)
        
        
    except:
        
        mensagem = "Nao foi possivel criar o arquivo %s. Seu equipamento nao podera ser mantido no GRID-QNInt ate resolver este problema." &(nomedoarquivo)
        registrar('clienteResultados.compactar', mensagem)
        sys.stderr.write(mensagem)
        

def enviar(usuario):
    
    import 
        
        