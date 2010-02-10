#-*- coding: utf-8 -*-

'''
Este script faz as interligações básicas com os servidores local e remoto e retém as operações básicas.

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

class Remoto(banco):
    
    def __init__(self):
        
        import DB
        servidor = "qnint.sbq.org.br"
        usuario = "qnint"
        senha = "_qn09pw"
        
        srv = DB.banco(servidor, usuario, senha)
        
        self.qnint = srv.Conectar("qnint")
        
        
        
    def pegarTarefas(self):
        
        import servidorPastas
        import localDB
        #Pastas
        
        pastas = servidorPastas.listar()
        dirPdb = pastas[4]
        
        
        #Queries e acesso ao banco       
        nomeSql = "SELECT nome FROM moleculas2 WHERE log = '' ORDER BY tamanho, tempo"
        arquivoSql = "SELECT arquivo FROM moleculas2 WHERE log = ' ' ORDER BY tamanho, tempo"
        
        
        self.qnint.execute(nomeSql)
        nomes = self.qnint.fetchall()
        
        self.qnint.execute(arquivoSql)
        arquivos = self.qnint.fetchall()
        
        #Criação dos arquivos
        pdb = {}
        for i in range (0, len(nomes)):
            
            #escreve os arquivos pdb na pasta /var/qnint
            caminho = dirPdb+'/'+nomes[i]+'.pdb'
            arquivo = open(caminho,'w')            
            arquivo.writelines(arquivos[i])
            
            #cria um dicionário com os nomes + arquivo para reserva
            pdbs = {nomes[i] : arquivos[i]}
 
        #Cadastra os trabalhos localmente e já os designa    
        grid = localDB.Local()        
        grid.cadastrarTarefas(nomes)        
        grid.Desconectar()
    
    
    def cadastrarResultado(self):
        
        import servidorPastas
        import localDB
        
        #checagem dos concluidos
        
        grid = localDB.Locao()
        concluidos = grid.checarConcluido()
        grid.Desconectar()
        
        for nome in concluidos:
            
            #pegar arquivo correspondente
            resultado = servidorPastas.pegarResultados(nome)
            if resultado != None:
                cadastroSQL = "UPDATE moleculas2 SET log=%s WHERE nome=%s" %(resultado,nome)
                Reconectar() #reconecta (ficará em loop caso não consiga de primeira
                self.qnint.execute(cadastroSQL)
        
        
    

    
        
        
    
        
        
        
        


