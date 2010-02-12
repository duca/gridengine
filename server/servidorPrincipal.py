# -*- coding: utf-8 -*-

'''
Este arquivo contém o looping principal

'''

def Loop():
        
    import servidorDB
    import servidorPastas
    import time
    
    #PID
    
    pid = open('/var/run/qnint-grid.pid', 'w')
    pid.write(str(1))
    pid.close()
    
    pidStatus = 1
    
    qnint = servidorDB.Remoto()
    grid = servidorDB.Local()
    
    while pidStatus == 1:
        
        
        
        
        #checar por novas tarefas
        
        qnint.pegarTarefas()
        
        
        
        #Checar para ver se o arquivo ainda existe, caso contrário termina a execução do programa
        try:
            pid = open('/var/run/qnint-grid.pid', 'r')
            pid.close()
        except:
            pidStatus = 0
            
        
        time.sleep(10)
        
        
    

            
            