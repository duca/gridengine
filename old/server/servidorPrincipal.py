# -*- coding: utf-8 -*-

'''
Este arquivo contém o looping principal

'''

def Loop():
        
    import servidorDB
    import servidorPastas
    import servidorErros
    import time
    import commands
    
    #PID
    pidPath = servidorPastas.listar()[1] + '/qnint-grid.pid'
    pid = open(pidPath, 'w')
    pid.write(str(1))
    pid.close()
    
    pidStatus = 1
    
    qnint = servidorDB.Remoto()
    grid = servidorDB.Local()
    
    while pidStatus == 1:   
               
        #checar por novas tarefas
        try:
            qnint = servidorDB.Remoto()
            grid = servidorDB.Local()
        except:
            mensagem = u'Nao foi possivel pegar as tarefas, pode ser um erro do banco ou de conexao. Erro 0035L'
            servidorErros.registrar('servidorPrincipal.Loop(pegarTarefas)', mensagem)
        qnint.pegarTarefas()    
        time.sleep(10)
        
        #Colocar como dono dos arquivos, o usuário qnint
        comando = "chgrp -R users " + servidorPastas.listar()[1]
        try:
            commands.getoutput(comando)
        
        except:
            mensagem = u'Nao foi possivel trocar o grupo detentor do diretorio %s, pode ser que os nodos nao consigam mover os dados. Erro 0042L'
            servidorErros.registrar('servidorPrincipal.Loop(chown)', mensagem)
            
        
        #Checar tarefas concluídas
        try:
            qnint.cadastrarResultado()
        except:
            mensagem = u'Nao foi possivel cadastrar os Resultados. Erro 0052L'
            servidorErros.registrar('servidorPrincipal.Loop(cadastrarResultados)', mensagem)
        
        
        #Checar para ver se o arquivo ainda existe, caso contrário termina a execução do programa
        try:
            pid = open(pidPath, 'r')
            pid.close()
        except:
            pidStatus = 0
            
        qnint.Desconectar()
        grid.Desconectar()
        time.sleep(30)
        print "Fim do loop"