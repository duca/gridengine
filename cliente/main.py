#-*- coding: utf-8 -*-



#imports

import sys
import argParser
  
status = argParser.Processar(sys.argv)

if status == False: #Não iniciar o serviço
    
    sys.exit()
    
else if status == True: #Iniciar o serviço
    #início do loop principal
      


