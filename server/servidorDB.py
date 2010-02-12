#-*- coding: utf-8 -*-

'''
Este script faz as interligações básicas com os servidores local e remoto e retém as operações básicas.

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''
import DB
class Remoto(DB.banco):
    
    def __init__(self):
        
        import DB
        self.servidor = "qnint.sbq.org.br"
        self.usuario = "qnint"
        self.senha = "_qn09pw"
        self.sql = "qnint"
        
        self.srv = DB.banco(self.usuario, self.senha, self.servidor)
        
        self.qnint = self.srv.Conectar(self.sql)
        
    def Reconectar(self):
        
        self.srv.Desconectar()
        
        self.srv.Conectar(self.sql)
        
    def Desconectar(self):
        
        self.qnint.close()
        
    def pegarTarefas(self):
        
        import servidorPastas
        #Pastas
        
        pastas = servidorPastas.listar()
        dirPdb = pastas[4]
        
        
        #Queries e acesso ao banco       
        nomeSql = "SELECT nome FROM moleculas2 WHERE log = '' ORDER BY tamanho, tempo"
        arquivoSql = "SELECT arquivo FROM moleculas2 WHERE log = '' ORDER BY tamanho, tempo"
        
        
        self.qnint.execute(nomeSql)
        n = self.qnint.fetchall()
        nomes = interpretar(n)
        
        #print nomes
        
        self.qnint.execute(arquivoSql)
        arquivos = self.qnint.fetchall()
#        a = self.qnint.fetchall()
#        arquivos = interpretar(a)
        
        #remapeando a tupla para algo mais legível
        n= reduce(lambda x, y:x + ',' + y, map(lambda x: x[0],nomes))
        nomes = n.split(',')
        print len(arquivos), nomes, type(nomes)
        #Criação dos arquivos
        pdb = {}
        for i in range (0, len(nomes)):
            
            #escreve os arquivos pdb na pasta /var/qnint
            #print str(nomes[i])
            caminho = dirPdb+'/'+nomes[i]+'.pdb'
            arquivo = open(caminho,'w')            
            arquivo.writelines(arquivos[i])
            
            #cria um dicionário com os nomes + arquivo para reserva
            pdbs = {nomes[i] : arquivos[i]}
 
        #Cadastra os trabalhos localmente e já os designa    
        
        grid = Local()        
        grid.cadastrarTarefas(nomes)        
        grid.Desconectar()
    
    
    def cadastrarResultado(self):
        
        import servidorPastas
        
        #checagem dos concluidos
        
        grid = Local()
        concluidos = grid.checarConcluido()
        grid.Desconectar()
        
        for nome in concluidos:
            
            #pegar arquivo correspondente
            resultado = servidorPastas.pegarResultados(nome)
            if resultado != None:
                cadastroSQL = "UPDATE moleculas2 SET log=%s WHERE nome=%s" %(resultado,nome)
                Reconectar() #reconecta (ficará em loop caso não consiga de primeira
                self.qnint.execute(cadastroSQL)
        
class Local(DB.banco):
    
    def __init__(self):
        
        import DB
        self.servidor = "200.136.224.70"
        self.usuario = "qnint"
        self.senha = "5471102aa"
        
        self.srv = DB.banco(self.usuario, self.senha, self.servidor)
        
        self.grid = self.srv.Conectar("grid")
        
       
    def Reconectar(self):
        
        self.srv.Desconectar()
        
        self.srv.Conectar("grid")
        
    def Desconectar(self):
        
        self.srv.Desconectar()
        
    def limparBanco(self):
        
        #limpando nodeload
        
        self.grid.execute("DELETE FROM grid_nodeload WHERE id >= 1")
        
        #limpando nodes
        
        self.grid.execute("DELETE FROM grid_nodes WHERE id >= 1")
        
        #limpando grid queue
        
        self.grid.execute("DELETE FROM grid_queue WHERE id >= 1")
        
    
    def checarConcluidos(self):
        
        checkSQL = "SELECT queuejob FROM grid_queue WHERE queuestatus='1' "
        
        try:
            self.grid.execute(checkSQL)
            
        except:
            self.Reconectar()
            self.grid.execute(checkSQL)
        concluidos = self.grid.fetchall()
        
        return concluidos      
    
    def cadastrarTarefas(self,nomes): 
        ''' Um rotina bem braçal para checar por novas tarefas. Ainda preciso instalar as rotinas de checagem e registro de erros'''
        
        
        listarNodos = "SELECT nodeKey from grid_nodeload ORDER BY nodeload"
        listarCargas = "SELECT nodeload from grid_nodeload ORDER BY nodeload"
        listarTarefas = "SELECT queuejob from grid_queue WHERE queuenodeassigned=''"
        
        #executa uma reconecção para garantir o sucesso da operação
        #self.Reconectar()
        self.grid.execute(listarNodos)
        n = self.grid.fetchall()
        nodos = interpretar(n)

        self.grid.execute(listarCargas)
        cargas = self.grid.fetchall()
#        #cargas = interpretar(c)
        print cargas

        
        self.grid.execute(listarTarefas)
        tarefas = self.grid.fetchall()
#        #tarefas = interpretar(t)

        print tarefas
        
        #checa quais tarefas ainda não foram designadas
        aprovados = []
        for i in range(0, len(nomes)):
            #este serve contador é zerado antes de checar se uma dada tarefa já está na fila
            contador = 0
            for j in range(0,len(tarefas)):
                
                if nomes[i] == tarefas[j]:
                    #se estiver na fila, adiciona 1 ao contador
                    contador = contador + 1
                    print contador , " \t contador"
            #se contador = 0, então a tarefa em questão é nova        
            if contador == 0:
                
                aprovados.append(nomes[i])
                print nomes[i] , " \t aprovados"
        
        for i in range(0, len(cargas)):
            
            if cargas[i] <= 2:
          
                Reconectar()
                
                self.grid.execute("INSERT into grid_queue(QueueJob, QueueNodeAssigned, QueueDuration, QueueStatus) values (%s, %s, '0', '0')",(aprovados[i], nodos[i]))
                
def interpretar(dado):
    n= reduce(lambda x, y:x + ',' + y, map(lambda x: x[0],dado))
    resultado = n.split(',')
    
    return resultado