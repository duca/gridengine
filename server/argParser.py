#-*- coding: utf-8 -*-

'''
Este módulo é o responsável por processar a lista de argumentos
:version: 0.0.1
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def Padrao(argumentos):
  
  print argumentos[0] "\n"
  print "O uso correto do programa é: \n python main.py --função \n \n Para obter a lista completa de opções use a opção --ajuda "
  
  
def Ajuda(argumentos):
  
  arquivo = open('help.dat', 'r')
  
  texto = arquivo.readlines()
  print argumentos[0]
  for linhas in texto:
    print linhas
  arquivo.close()
  
def Processar(argumentos):
  '''Função principal de processamento de argumentos'''
  
  import clienteFuncoes

  Check(argumentos)
      
  argumento = argumentos[1][3:]
  if arumento == "iniciar":
    return True
  else if argumento == "cadastrar":
    clienteFuncoes.cadastrar()
    return False
  else if argumento == "descadastrar":
    clienteFuncoes.descadastrar()
    return False
  else if argumento == "preparar":
    clienteFuncoes.preparar()
    return False
  else if argumento == "remover":
    clienteFuncoes.remover()
    return False
  else if argumento == "ajuda":
    Ajuda(argumentos)
    return False
  else if argumento == "versao":
    clienteFuncoes.versao(argumentos)
    return False
      
def Check(argumentos):
  '''Fecha o programa se houver argumento inválido'''
  import sys
  
  if len(argumentos) != 2 : #checa quantidade de argumentos 
    Padrao(argumentos)
    sys.exit()
    
  for i in range (len(argumentos)):
    
    if argumentos[i][0:2] != "--":
      
      Padrao(argumentos)
      sys.exit()
    

      