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
    
    
    def __init__(self, ident, programa):
        
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
        
        import commands
        import clienteErros
        
        #etapa de otimização        
        if self.programa == 'gaussian':
         
            otimizacao = "gaussian ... "
        else:
            mensagem = "A tarefa %s exigiu o programa %s e este ainda nao e suportado" %(self.ident, self.programa)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            

        try:             
            out = commands.getoutput(otimizacao)
        except:
            
            mensagem = "A Tarefa %s (fase de otimizacao) nao pode ser executada" %(self.ident)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
        
        #etapa de simulacao
    
     
        if self.programa == 'gaussian':
         
            simulacao = "gaussian ... "
        else:
            mensagem = "A tarefa %s exigiu o programa %s e este ainda nao e suportado" %(self.ident, self.programa)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            

        try:             
            out = commands.getoutput(simulacao)
        except:
            
            mensagem = "A Tarefa %s (fase de simulacao) nao pode ser executada" %(self.ident)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
        
    def compactar(self, ident):
        
        du = ' '

