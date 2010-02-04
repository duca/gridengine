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
            mensagem = u"A tarefa %s exigiu o programa %s e este ainda não é suportado" %(self.JobKey, self.programa)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            

        try:             
            out = commands.getoutput(otimizacao)
        except:
            
            mensagem = u"A Tarefa %s (fase de otimizacao) não pode ser executada.Verifique a instalação do programa %s" %(self.JobKey, self.programa)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
        
        #etapa de simulacao
    
     
        if self.programa == 'gaussian':
         
            simulacao = "gaussian ... "
        else:
            mensagem = u"A tarefa %s exigiu o programa %s e este ainda não é suportado" %(self.JobKey, self.programa)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            

        try:             
            out = commands.getoutput(simulacao)
        except:
            
            mensagem = u"A Tarefa %s (fase de simulacao) não pode ser executada. Verifique a instalação do programa %s" %(self.JobKey, self.programa)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
        
    #def otimizar(self, 
    #def compactar(self, JobKey):
        
        #du = ' '

def sumario():
    '''Esta função carrega os dados básicos do Workstation'''
    
    import Chave
    
    tudo = Chave.padrao()
    
    return tudo

def pegarKey():
    
    tudo = sumario()
    
    chave = sumario['key']
    
    return chave

       
