#-*- coding: utf-8 -*-

'''
Este script faz as interligações básicas com os servidores local e remoto e retém as operações básicas.

'''
import DB

class Local(DB.banco):
    
    def __init__(self):
        
        import DB
        self.servidor = "200.136.224.70"
        self.usuario = "qnint"
        self.senha = "5471102aa"
        
        self.srv = DB.banco(servidor, usuario, senha)
        
        self.grid = self.srv.Conectar("grid")
        
        return self.grid
        
    def Reconectar(self):
        
        self.srv.Desconectar()
        
        self.srv.Conectar("grid")
        
    
    def checarConcluidos(self):
        
        checkSQL = "SELECT queuejob FROM grid_queue WHERE queuestatus='1' "
        
        try:
            self.grid.execute(checkSQL)
            
        except:
            Reconectar()
            self.grid.execute(checkSQL)
        concluidos = self.grid.fetchall()
        
        return concluidos      
    
    def cadastrarTarefas(self,nomes): 
        ''' Um rotina bem braçal para checar por novas tarefas. Ainda preciso instalar as rotinas de checagem e registro de erros'''
        
        
        listarNodos = "SELECT nodeKey from grid_nodes ORDER BY nodeLoad"
        listarCargas = "SELECT nodeLoad from grid_nodes ORDER BY nodeLoad"
        listarTarefas = "SELECT queuejob from grid_queue WHERE nodeassigned=''"
        
        #executa uma reconecção para garantir o sucesso da operação
        Reconectar()
        self.grid.execute(listarNodos)
        nodos = self.grid.fetchall()

        self.grid.execute(listaCargas)
        cargas = self.grid.fetchall()
        
        self.grid.execute(listarTarefas)
        tarefas = self.grid.fetchall()
        
        #checa quais tarefas ainda não foram designadas
        aprovados = []
        for i in range(0, len(nomes)):
            #este serve contador é zerado antes de checar se uma dada tarefa já está na fila
            contador = 0
            for j in range(0,len(tarefas)):
                
                if nomes[i] == tarefas[j]:
                    #se estiver na fila, adiciona 1 ao contador
                    contador = contador + 1
            #se contador = 0, então a tarefa em questão é nova        
            if contador == 0:
                
                aprovados.append(nomes[i])
        
        for i in range(0, len(cargas)):
            
            if cargas[i] <= 2:
                
                designarSQL = "INSERT into grid_queue(QueueJob, QueueNodeAssigned, QueueDuration, QueueStatus) values (%s, %s, '0', '0')  " %(aprovados[i], nodos[i])
                
                Reconectar()
                
                self.grid.execute(designarSQL)

                

                    

                
                
        
        
        

    
        
        
    
        
        
        
        


