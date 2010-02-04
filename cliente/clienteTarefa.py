#-*- coding: utf-8 -*-

'''
Este módulo mantém as funções básicas para efetuar o trabalho.

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

class Tarefa:
    
    JobKey = None
    programa = None
    nucleos = 0
    
    
    def __init__(self, JobKey, programa):
        
        self.JobKey = JobKey
        self.programa = programa
        self.nucleos
        
    #def descompactar(self, JobKey):
        
        #import clientePastas
        #import zlib
        #import commands
        #import sys
        #from clienteErros import registrar
    
        #diretorios = clientePastas.listar()
        #resultados = diretorios[4] + '/' + usuario + '/' + self.JobKey + '.zip'
    
    
    def executar(self,JobKey):
        
        import commands
        import clienteErros
        
        #etapa de otimização        
        if self.programa == 'pcgamess':
         
            otimizacao = "gaussian ... "
        else:
            mensagem = "A tarefa %s exigiu o programa %s e este ainda nao e suportado" %(self.JobKey, self.programa)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            

        try:             
            out = commands.getoutput(otimizacao)
        except:
            
            mensagem = "A Tarefa %s (fase de otimizacao) nao pode ser executada" %(self.JobKey)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
        
        #etapa de simulacao
    
     
        if self.programa == 'gaussian':
         
            simulacao = "gaussian ... "
        else:
            mensagem = "A tarefa %s exigiu o programa %s e este ainda nao e suportado" %(self.JobKey, self.programa)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            

        try:             
            out = commands.getoutput(simulacao)
        except:
            
            mensagem = "A Tarefa %s (fase de simulacao) nao pode ser executada" %(self.JobKey)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
        
    #def otimizar(self, 
    #def compactar(self, JobKey):
        
        #du = ' '
    
    

       
