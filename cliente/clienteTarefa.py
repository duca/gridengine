#-*- coding: utf-8 -*-

'''
Este módulo mantém as funções básicas para efetuar o trabalho.

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

class Tarefa:
    
    ident = None
    programa = None
    nucleos = 0
    
    
    def __init__(self, ident, programa, nucleos):
        
        self.ident = ident
        self.programa = programa
        self.nucleos
        
    def descompactar(self, ident):
        
        import clientePastas
        import zlib
        import commands
        import sys
        from clienteErros import registrar
    
        diretorios = clientePastas.listar()
        resultados = diretorios[4] + '/' + usuario + '/' + self.ident + '.zip'
        
    def executar(self,ident):
        
        import commandos
        
        
        
        
    
        
        

