#-*- coding: utf-8 -*-

'''
Este módulo contém as funções que registram, no banco de dados, as informações relativas ao nó em que foi instalado

:version: 0.0.1
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

class banco:
    
    usuario = None
    senha = None
    servidor = None
    
    def __init__(self, usuario, senha, servidor):
        import MySQLdb
        import clienteErros
        import time
        import sys
        
        self.usuario = 'qnint'
        self.senha = '5471102aa'
        self.servidor = '192.168.56.101'
        
        print self.servidor, self.usuario, self.senha
        try:
            con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
            print self.servidor, self.usuario, self.senha
                        
        except:
            
            mensagem = u"Nao foi possível conectar ao servidor. O programa esperará 60 segundos e tentará novamente"
            clienteErros.registrar('clienteDB.conectar', mensagem)
            time.sleep(60)
            #tentativa de conectar novamente
            Reconectar()
            sys.exit()
        con.select_db("grid")
        self.cursor = con.cursor()
        
    def Reconectar(self):
        
        import MySQLdb
        import clienteErros
        import sys
        print self.servidor, self.usuario, self.senha
        try:
            con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
            print self.servidor, self.usuario, self.senha
                        
        except:
            
            mensagem = u"Não foi possível conectar ao servidor. Verifique a conexão e tente mais tarde"
            clienteErros.registrar('clienteDB.conectar', mensagem)
            sys.exit()
        con.select_db("grid")
        self.cursor = con.cursor()

    def Desconectar(self):
        
        self.cursor.close()
        


    def registrarWorkstation(self, sumario ):
        
        import clienteData
        import clienteErros
        import sys
        
        dados = clienteData.sbp()
       
        status = verificarKey(sumario['key'])
        
        if status == 1:
            message = 'Seu workstation ja esta cadastrado'
            sys.stderr.write(message)
            clienteErros('clienteFuncoes.cadastrar', message)
            sys.exit()            
            
        querysql = 'Insert into grid_nodes (nodeKey, nodeCores, nodeRam, nodeAvail, nodeHostname, nodeIP, nodeCheck) values (%s, %i, %i, %i, %s, %s, %s)' % ( sumario['key'], sumario['nucleos'], sumario['ram'], 1, sumario['nome'], sumario['IP'], sumario['datetime'])
        
        self.cursor.execute(querysql)
        
    def pegarTarefas(self,nodeKey):
        
        
        designadosSQL = "SELECT queuenodeassigned FROM grid_queue WHERE status = '0'"
        tarefasSQL = "SELECT queuejob FROM grid_queue WHERE status = '0'"
        
        #pega a lista das designações
        self.cursor.execute(designadosSQL)
        designados = self.cursor.fetchall()
        
        #pega a lista das tarefas
        self.cursor.execute(tarefasSQL)
        tarefas = self.cursor.fetchall()
    
        aprovados = []
        
        for i in range (0, len(tarefas)):
            
            if tarefas[i] == nodeKey:
                
                aprovados.append(tarefas[i])
        
        
        return aprovados
    
#    def registrarDesignacao(self, nodeKey, JobKey): #funcao desabilitada pois a designação é feita pelo servidor
#        
#        querysql = "UPDATE grid_queue SET NodeAssigned= %s WHERE QueueJobQueue= %s" %(nodeKey, JobKey)
#        
#        self.cursor.execute(querysql)
        
    
    def registrarConclusao(self, Job):
        
               
        querysql = "UPDATE grid_queue SET queuestatus='1' WHERE queuejob= %s" %(Job)
        
        self.cursor.execute(querysql)
        
    def HeartBeat(self, NodeKey):
        
        from clienteData import HeartBeat
          
        pulso = HeartBeat()
        
        querysql = "UPDATE grid_nodeLoad SET nodeLoad= %d WHERE nodeKey=%s" %(pulso['load'], pulso['key'])
        self.cursor.execute(querysql)
        
    def pegarChaves(self):
        
        querysql = "select NodeKey from grid_nodes"
        
        self.cursor.execute(querysql)
        
        chaves = self.cursor.fetchall()
        
        return chaves
    
