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
        
        self.usuario = usuario
        self.senha = senha
        self.servidor = servidor
        
    def Conectar(self):
        
        import MySQLdb
        import clienteErros
        import sys
        print self.servidor, self.usuario, self.senha
        try:
            con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
            print self.servidor, self.usuario, self.senha
                        
        except:
            
            mensagem = "Nao foi possivel conectar ao servidor. Verifique a conexao e tente mais tarde"
            clienteErros.registrar('clienteDB.conectar', mensagem)
            sys.exit()
        con.select_db("grid")
        self.cursor = con.cursor()
        
        
        
    def fetchAll(querysql):
        
        self.cursor.execute(querysql)
        resultado = self.cursor.fetchall() #envia o conteudo da tabela numa lista
        return resultado

    def fetchSelected(querysql):
        
        self.cursor.execute(querysql)
        resultado = self.cursor.fetchone()
        return resultado
    
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
            
        querysql = 'Insert into Nodes (nodeKey, nodeCores, nodeRam, nodeAvail, nodeHostname, nodeIP, nodeCheck) values (%s, %i, %i, %i, %s, %s, %s)' % ( sumario['key'], sumario['nucleos'], sumario['ram'], 1, sumario['nome'], sumario['IP'], sumario['datetime'])
        
        self.cursor.execute(querysql)