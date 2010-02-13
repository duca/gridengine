#-*- coding: utf-8 -*-

'''
Este módulo é o responsável por processar a lista de argumentos
:version: 0.0.1
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def Padrao(argumentos):
  
  print argumentos[0] + "\n"
  print "O uso correto do programa é: \n python main.py --função \n \n Para obter a lista completa de opções use a opção --ajuda "
  
  
def Ajuda(argumentos):
  
  arquivo = open('help.dat', 'r')
  
  texto = arquivo.readlines()
  for linhas in texto:
    print linhas
  arquivo.close()
  
def Processar(argumentos):
  '''Função principal de processamento de argumentos'''
  
  import servidorFuncoes
  
  Check(argumentos)
      
  argumento = argumentos[1][2:]
  if argumento == "iniciar":
    print "Iniciando..."
    return True
  elif argumento == "preparar":
    print "Preparando..."
    servidorFuncoes.preparar()
    return False
  elif argumento == "remover":
    print "Removendo..."
    servidorFuncoes.remover()
    return False
  elif argumento == "ajuda":
    print "Ajudando..."
    Ajuda(argumentos)
    return False
  elif argumento == "versao":
    servidorFuncoes.versao(argumentos)
    return False
      
def Check(argumentos):
  '''Fecha o programa se houver argumento inválido'''
  import sys
  if len(argumentos) != 2 : #checa quantidade de argumentos 
    Padrao(argumentos)
    sys.exit()
 
  if argumentos[1][0:2] != "--":
    print argumentos[1][0:2]  
    Padrao(argumentos)
    sys.exit()
    

      