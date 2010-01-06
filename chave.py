#-*- coding: utf-8 -*-

'''
Este módulo tem a única função de gerar as chaves utilizadas para identificar os nós e os processos atribuídos a cada usuário 

desenvolvido por Eduardo Martins Lopes < edumlopes at gmail dot com >
'''

def gerar(tamanho):
    
    import random
    import string
    import time
    
    chave = ''
    #cria a lista de caracteres aceitos
    
    populacao = string.uppercase + string.lowercase + string.digits
    
        
    for i in range(1,tamanho):
        
        amostra = random.choice(populacao)
        
        
        chave = amostra + chave
  
    
    return chave
   
        
    
        
        