#-*- coding: utf-8 -*-



#imports

import sys
import argParser
import clienteTarefa
  
status = argParser.Processar(sys.argv)

if status == False: #Não iniciar o serviço
    
    sys.exit()
    
else if status == True: #Iniciar o serviço
    #início do loop principal
    
    
    clienteTarefa.Iniciar()
    


