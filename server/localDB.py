#-*- coding: utf-8 -*-

'''
Este script faz as interligações básicas com os servidores local e remoto e retém as operações básicas.

'''

class Local(banco):
    
    def __init__(self):
        
        import DB
        servidor = "200.136.224.70"
        usuario = "qnint"
        senha = "5471102aa"
        
        srv = DB.banco(servidor, usuario, senha)
        
        self.qnint = srv.Conectar("qnint")
        
        
        
    def instalarTarefas(self):
        
        nomeSql = "SELECT nome FROM moleculas2 WHERE log = '' ORDER BY tamanho, tempo"
        arquivoSql = "SELECT arquivo FROM moleculas2 WHERE log = ' ' ORDER BY tamanho, tempo"
        
        
        self.qnint.execute(nomeSql)
        nomes = self.qnint.fetchall()
        
        self.qnint.execute(arquivoSql)
        arquivos = self.qnint.fetchall()
        
        pdb = {}
        for i in range (0, len(nomes)):
            
            pdb = {nomes : arquivos}
              
        return pdb
    

    
        
        
    
        
        
        
        


