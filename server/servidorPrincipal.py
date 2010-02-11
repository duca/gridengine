# -*- coding: utf-8 -*-

'''
Este arquivo contém o looping principal

'''

def Principal():
        
    import servidorDB
    import localDB
    import servidorPastas
    
    #PID
    
    pid = open('/var/run/qnint-grid.pid', 'w')
    pid.write(str(1))
    pid.close()
    
    pidStatus = 1
    
    while pidStatus == 1:
        
        qnint = servidorDB.Remoto()
        grid = servidorDB.Local()
        
        
        #Checar para ver se o arquivo ainda existe, caso contrário termina a execução do programa
        try:
            pid = open('/var/run/qnint-grid.pid', 'r')
            pid.close()
        except:
            pidStatus = 0
