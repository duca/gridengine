#-*- coding: utf-8 -*-

'''
Este módulo contém as funções básicas do programa. Está fora do main por questões de encapsulamento e segurança (os módulos são enviados como arquivos inelegíveis)

:version: 0.0.1
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def preparar():
    
    import clientePastas
    
    servidorPastas.padrao()

def versao(argumentos):
    
    print "Versao 0.0.1"