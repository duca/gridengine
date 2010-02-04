#-*- coding: utf-8 -*-

'''
Este módulo tem a única função de gerar as chaves utilizadas para identificar os nós e os processos atribuídos a cada usuário 

:version: 0.0.1
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def gerar(tamanho):
    
    import random
    import string
    import time
    
    chave = ''
    #cria a lista de caracteres aceitos
    
    populacao = string.uppercase + string.lowercase + string.digits
    
        
    for i in range(0,tamanho):
        
        amostra = random.choice(populacao)
        
        
        chave = amostra + chave
  
    
    return chave
   
def interpretar(nome):
    
    import bz2
    
    final = bz2.decompress(nome)
    
    return final

def padrao():
    '''Retorna o sumario da maquina'''
    import clienteData
    import pickle
    import bz2
    
    dado = interpretar(clienteData.normal())
    
    resultado = pickle.loads(bz2.decompress(dado))
    
    return resultado

def codificar(dados):
    
    import base64
    import bz2
    import pickle 
    
    pickled = pickle.dumps(dados)
    codificado = base64.b64encode(bz2.compress(pickled))
    
    return codificado
    
        
        