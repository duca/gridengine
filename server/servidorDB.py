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

#        self.servidor = "200.136.224.70"
#        self.usuario = "qnint"
#        self.senha= "5471102aa"
#        self.porta = 3306
#        self.sql = "grid"        
        
        self.srv = DB.banco(self.usuario, self.senha, self.servidor)
        
        self.qnint = self.srv.Conectar(self.sql)
        
    def Reconectar(self):
        
        self.srv.Desconectar()
        
        self.srv.Conectar(self.sql)
        
    def Desconectar(self):
        
        self.qnint.close()
    def limparBanco(self):
        
        #limpando moleculas2        
        self.qnint.execute("DELETE FROM moleculas2 WHERE id >= 1")
        self.qnint.execute("commit")

    def pegarTarefas(self):        
        #Queries e acesso ao banco       
        nomeSql = "SELECT nome FROM moleculas2 WHERE log = '' ORDER BY tempo"
        arquivoSql = "SELECT arquivo FROM moleculas2 WHERE log = '' ORDER BY tempo" 
        extSql = "SELECT extensao FROM moleculas2 WHERE log='' ORDER by tempo"
        
        nomes = ''
        self.qnint.execute(nomeSql)
        n = self.qnint.fetchall()
        if len(n) > 0: nomes = interpretar(n)

        extensao = ''
        self.qnint.execute(extSql)
        e = self.qnint.fetchall()
        if len(e) > 0: extensao = interpretar(e)
        
        self.qnint.execute(arquivoSql)
        arquivos = self.qnint.fetchall()
#        a = self.qnint.fetchall()
#        arquivos = interpretar(a)
    
        #Criação dos arquivos
        #pdb = {}
        #for i in range (0, len(nomes)):
            
            #escreve os arquivos pdb na pasta /var/qnint
            #print str(nomes[i])
            #caminho = dirPdb+'/'+nomes[i]+'.pdb'
            #arquivo = open(caminho,'w')            
            #arquivo.writelines(arquivos[i])
            
            # #################################

            ##cria um dicionário com os nomes + arquivo para reserva
            #pdbs = {nomes[i] : arquivos[i]}

        #Cadastra os trabalhos localmente e já os designa    
        
        grid = Local()        
        grid.cadastrarTarefas(nomes,arquivos, extensao)        
        grid.Desconectar()
    
    
    def cadastrarResultado(self):
        
        import servidorPastas
        
        #checagem dos concluidos
        
        grid = Local()
        concluidos = grid.checarConcluidos()

        grid.Desconectar()
        
        arquivos = concluidos.pop()
        nomes = concluidos.pop()
        for i in range(0,len(nomes)):
            self.qnint.execute( "UPDATE moleculas2 SET log= %s WHERE nome= %s" ,(arquivos[i],nomes[i]))
            self.qnint.execute("commit")
        
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
        
        checkSQL = "SELECT QueueJob FROM grid_queue WHERE QueueStatus='1' "
        logSQL = "SELECT log FROM grid_queue WHERE QueueStatus='1' "
        
        #Pegando os nomes, primeiro
        try:
            self.grid.execute(checkSQL)
            c = self.grid.fetchall()
            nomes = interpretar(c)
       
        except:
            self.Reconectar()
            self.grid.execute(checkSQL)
            c = self.grid.fetchall()
            nomes = interpretar(c)

        
        #pegando os arquivos
        self.grid.execute(logSQL)
        logs = self.grid.fetchall() 

        
        concluidos = []
        concluidos.append(nomes)
        arquivos = []
        for i in range(0, len(nomes)):            
            a = arq(logs[i]) #convertendo a stream para algo mais leg�vel
            #montando o dictionary
            arquivos.append(a)
        concluidos.append(nomes)
        concluidos.append(arquivos)
        return concluidos      
    
    def cadastrarTarefas(self,nomes, arquivos, extensao): 
        ''' Um rotina bem braçal para checar por novas tarefas. Ainda preciso instalar as rotinas de checagem e registro de erros'''
        
        listarNodos = "SELECT nodeKey from grid_nodeload"
        listarCargas = "SELECT nodeLoad from grid_nodeload"
        listarTarefas = "SELECT QueueJob from grid_queue"
        
        #executa uma reconecção para garantir o sucesso da operação
        #self.Reconectar()
        self.grid.execute(listarNodos)
        nodos = self.grid.fetchall()
        if len(nodos) > 0:
            n = nodos
            nodos = interpretar(n)

        self.grid.execute(listarCargas)
        c = self.grid.fetchall()
        
        cargas = interpretarNum(c)
     
        self.grid.execute(listarTarefas)
        tarefas = self.grid.fetchall()

        if len(tarefas) > 0:
            t = tarefas
            tarefas = interpretar(t)
        else:
            tarefas = []
        #checa quais tarefas ainda não foram designadas
        aprovados = []
        pdbsAprovados = []
        extAprovados = []
        if len(tarefas) == 0:
            aprovados = nomes
            pdbsAprovados = arquivos
            extAprovados = extensao

        else:
            
            for i in range(0, len(nomes)):
                #este serve contador é zerado antes de checar se uma dada tarefa já está na fila
                contador = 0
                for j in range(0,len(tarefas)):
                    
                    if nomes[i] == tarefas[j]:
                        #se estiver na fila, adiciona 1 ao contador
                        contador = contador + 1
                #se contador = 0, então a tarefa em questão é nova  

                if contador == 0:

                    extAprovados.append(extensao[i])
                    aprovados.append(nomes[i])
                    pdbsAprovados.append(arquivos[i])

        for i in range(0, len(cargas)):
            if cargas[i] <= 2:
                
                if i < len(aprovados):
                    #rápida preparação dos pdb's para inserção no banco
                    f = arq(pdbsAprovados[i])
                    self.grid.execute("INSERT into grid_queue(QueueJob, QueueNodeAssigned, arquivo, extensao) values (%s, %s, %s, %s)",(str(aprovados[i]), str(nodos[i]), f, extAprovados[i]))
             
                
def interpretar(dado):
    n= reduce(lambda x, y:x + ',' + y, map(lambda x: x[0],dado))
    resultado = n.split(',')
    return resultado

def interpretarNum(dado):
    
    tmp = []    
    for i in dado:
        
        tmp.append(int(i[0]))
        
    return tmp    
def arq(dado):    

    tempfile = "/opt/qnint/calculos/temp.file"
    archive = open(tempfile, 'w')
        
    archive.writelines(dado)
    archive.close()
    
    archive = open(tempfile, 'r')
    result = archive.read()
    archive.close()

    return result