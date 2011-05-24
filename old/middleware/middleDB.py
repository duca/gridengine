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
        
        #Queries e acesso ao banco 
        idUserSql = "SELECT idUsuario FROM moleculas2 WHERE log='' "
        nomeSql = "SELECT nome FROM moleculas2 WHERE log = '' "
        arquivoSql = "SELECT arquivo FROM moleculas2 WHERE log = ''"
        
        #pegando os nomes dos arquivos
        self.qnint.execute(nomeSql)
        n = self.qnint.fetchall()
        nomes = interpretar(n)

        #pegando o ID dos usuarios
        self.qnint.execute(idUserSql)
        i = self.qnint.fetchall()
        usuarios = interpretarNum(i)

        #pegando os PDB's
        self.qnint.execute(arquivoSql)
        arquivos = self.qnint.fetchall()
        
        #comparando com a listagem do banco do grid
        grid = Local()
        gridCursor = grid.Conectar()
        gridCursor.execute("SELECT nome FROM moleculas2")
        gridCursor.close()
        lista = gridCursor.fetchall()
        if len(lista) == 0:
            emGrid = []
            emGrid.append("nada")
        else:
            emGrid = interpretar(lista)
        
        nomeOK = []
        arquivoOK = []
        idOK = []

        for i in range(len(nomes)):
            contador = 0            
            for j in range(len(emGrid)):
                
                if emGrid[j] == nomes[i]:
                    contador = contador + 1
            if contador == 0:
                nomeOK.append(nomes[i])
                arquivoOK.append(arquivos[i])
                idOK.append(usuarios[i])
                
        #conexão novamente ao banco do grid      
        grid = Local()
        for i in range(0,len(nomeOK)):
            #transformando a string arquivo em uma estrutura estilo arquivo para inserir no db
            f = arq(arquivoOK[i])
            ii = str(idOK[i])
            n = str(nomeOK[i])
            grid.cadastrarTarefas(ii,n, f)
   
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
        
    def Conectar(self): 
        self.srv = DB.banco(self.usuario, self.senha, self.servidor)
        self.grid = self.srv.Conectar("grid")
        return self.grid
       
    def Reconectar(self):
        
        self.srv.Desconectar()
        
        self.srv.Conectar()
        
    def Desconectar(self):
        
        self.srv.Desconectar()
        
    def criarTabela(self):
        
        self.grid.execute('''CREATE TABLE `grid`.`moleculas2` (
`id` INT( 12 ) NOT NULL DEFAULT NULL AUTO_INCREMENT PRIMARY KEY ,
`idUsuario` INT( 12 ) NOT NULL ,
`nome` VARCHAR( 250 ) NOT NULL ,
`arquivo` LONGBLOB NOT NULL ,
`extensao` VARCHAR( 30 ) NOT NULL ,
`tamanho` VARCHAR( 30 ) NOT NULL ,
`log` LONGBLOB NOT NULL ,
`status` VARCHAR( 30 ) NOT NULL ,
`idioma` VARCHAR( 30 ) NOT NULL ,
`tempo` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB CHARACTER SET utf8 COLLATE utf8_unicode_ci;''' )
        
    def limparBanco(self):
        
        #limpando nodeload
        
        self.grid.execute("DELETE FROM moleculas2 WHERE id >= 1")
        self.grid.execute('commit')
 
        
    
    def checarConcluidos(self):
        
        checkSQL = "SELECT queuejob FROM grid_queue WHERE QueueStatus='1' "
        
        try:
            self.grid.execute(checkSQL)
            
        except:
            self.Reconectar()
            self.grid.execute(checkSQL)
        concluidos = self.grid.fetchall()
        
        return concluidos      
    
    def cadastrarTarefas(self,campo1, campo2,campo3): 
        ''' Um rotina bem braçal para checar por novas tarefas. Ainda preciso instalar as rotinas de checagem e registro de erros'''
        
        #self.grid.execute("INSERT INTO moleculas(idUsuario, nome) VALUES (%s, %s)", (campo1, campo2))
        self.grid.execute("INSERT INTO moleculas2(idUsuario, nome, arquivo, extensao, log) VALUES (%s, %s, %s, 'pdb', %s)", (campo1, campo2, campo3, ''))
        self.grid.execute('commit')
                
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
    
    import middlePastas
        
    temp = middlePastas.listar()[2] + '/temp.file'
    st = dado
    fi = open(temp, 'w')
    fi.writelines(st)
    fi.close()
    
    fi = open(temp, 'r')
    result = fi.read()
    
    return result
    