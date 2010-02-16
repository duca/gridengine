#-*- coding: utf-8 -*-

'''
Este módulo contém as funções que registram, no banco de dados, as informações relativas ao nó em que foi instalado

:version: 0.0.1
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

class banco:
    
 
    def __init__(self):
        import MySQLdb
        import clienteErros
        import time
        
        self.usuario = 'qnint'
        self.senha = '5471102aa'
        self.servidor = '200.136.224.70'
        
        try:
            con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
            print "Sucesso em conectar ao banco do GRID"
            con.select_db("grid")
            self.cursor = con.cursor()
                        
        except:
            
            mensagem = u"Nao foi possível conectar ao servidor. O programa esperará 60 segundos e tentará novamente"
            clienteErros.registrar('clienteDB.__init__', mensagem)
            time.sleep(60)
            #tentativa de conectar novamente
            Reconectar()
        
        
        
    def Reconectar(self):
        
        import MySQLdb
        import clienteErros
        import sys
        print self.servidor, self.usuario, self.senha
        try:
            con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
            print 'Sucesso em reconectar'
                        
        except:
            
            mensagem = u"Não foi possível conectar ao servidor. Verifique a conexão e tente mais tarde. Erro 0050L"
            clienteErros.registrar('clienteDB.reconectar', mensagem)
            sys.exit()
        con.select_db("grid")
        self.cursor = con.cursor()

    def Desconectar(self):
        
        self.cursor.close()
        


    def registrarWorkstation(self, sumario ):
        
        import clienteData
        import clienteErros
        import sys
                
        one = 1

        carga = clienteData.Carga()
        try:
            self.cursor.execute ("""INSERT INTO grid_nodes (nodeKey, nodeCores, nodeRam, nodeAvail, nodeHostname, nodeIP) VALUES ( %s, %s, %s, %s, %s, %s)""", ( sumario['key'], sumario['nucleos'], sumario['ram'], one, sumario['nome'], sumario['IP']))
            self.cursor.execute ("""INSERT INTO grid_nodeload (nodeKey, nodeCores, nodeLoad) VALUES ( %s, %s, %s)""", ( sumario['key'], sumario['nucleos'], carga))
            print "Sucesso em cadastrar seu workstation com a chave: ", sumario['key'], "Anote pois precisaremos desse valor em caso de necessidade de descadastro do workstation ou resoluções de erros."
            
        except:
            mensagem = u"Não foi possível executar as query's sql. Verifique a conexão e tente mais tarde. Erro 0077L"
            clienteErros.registrar('clienteDB.registrarWorkstation', mensagem)
            sys.exit()
        
    def pegarTarefas(self,nodeKey):
        
        import clienteErros
        print "Pegando as designações..."
        designadosSQL = "SELECT QueueNodeAssigned FROM grid_queue WHERE QueueStatus = '0'"
        tarefasSQL = "SELECT QueueJob FROM grid_queue WHERE QueueStatus = '0'"
        
        #pega a lista das designações
        self.cursor.execute(designadosSQL)
        d = self.cursor.fetchall()
        designados = interpretar(d)
        
        #pega a lista das tarefas
        self.cursor.execute(tarefasSQL)
        t = self.cursor.fetchall()
        tarefas = interpretar(t)
    
        self.aprovados = []

        for i in range (0, len(tarefas)):

            if designados[i] == nodeKey:
            
                self.aprovados.append(tarefas[i])
            
        print "Pegando os arquivos:"
        for i in self.aprovados:
        
            try:
                print i
                getPdb(i)
        #self.gridSSH = ssh.Connection('200.136.224.70', username='grid', password='grid**00')
        
            except:
                mensagem = u"Nao foi possivel conectar ao servidor."
                clienteErros.registrar('clienteDB.pegarTarefas(sessao ssh)', mensagem)
        return self.aprovados
    
#    def registrarDesignacao(self, nodeKey, JobKey): #funcao desabilitada pois a designação é feita pelo servidor
#        
#        querysql = "UPDATE grid_queue SET NodeAssigned= %s WHERE QueueJobQueue= %s" %(nodeKey, JobKey)
#        
#        self.cursor.execute(querysql)
        
    
    def registrarConclusao(self, Job):
        
               
        querysql = "UPDATE grid_queue SET QueueStatus='1' WHERE QueueJob= %s" %(Job)
        putLog(Job)
        self.cursor.execute(querysql)
        
    def HeartBeat(self):
        
        import clienteData
          
        pulso = clienteData.HeartBeat()
        try:
            self.cursor.execute( "UPDATE grid_nodeload SET nodeLoad= %s WHERE nodeKey=%s",(pulso['load'], pulso['key']))
        except:
            Reconectar()
            self.cursor.execute( "UPDATE grid_nodeload SET nodeLoad= %s WHERE nodeKey=%s",(pulso['load'], pulso['key']))
            
   
        
    def pegarChaves(self):
        
        querysql = "select nodeKey from grid_nodes"
        
        self.cursor.execute(querysql)
        
        chaves = self.cursor.fetchall()
        
        return interpretar(chaves)
   
    def getPdb(self, nome):
        
        import ssh
        import clientePastas
        import clienteErros
        
        pastas = clientePastas.listar()
        pdbLocal = pastas(4) + "/" + nome  
        pdbRemoto = "/opt/qnint/calculos/" + nome
   
        try:
            #'200.136.224.70'
            self.gridSSH = ssh.Connection('127.0.0.1', username='qnint', password='grid**00')
            print "Conectado via ssh"
            self.gridSSH.get(pdbRemoto, pdbLocal)
        except:
            
            mensagem = u"Nao foi possível conectar ao servidor. O programa esperará 60 segundos e tentará novamente. Erro 0186L"
            clienteErros.registrar('clienteDB.sftp', mensagem)
        
    def putLog(self, nome):
        import ssh
        import clientePastas
        import clienteErros
        
        logLocal = pastas(4) + "/" + nome
        logRemoto = "/opt/qnint/logs/"  + nome

        
        try:
            self.gridSSH = ssh.Connection('127.0.0.1', username='qnint', password='grid**00')
            print "Conectado via ssh"

            self.gridSSH.put(logLocal, logRemoto)
                
            gridSSH.close()        
                           
        except:
            
            mensagem = u"Nao foi possível conectar ao servidor. O programa esperará 60 segundos e tentará novamente. Erro 0186L"
            clienteErros.registrar('clienteDB.sftp', mensagem)


def interpretar(dado):
    n= reduce(lambda x, y:x + ',' + y, map(lambda x: x[0],dado))
    resultado = n.split(',')
    return resultado
