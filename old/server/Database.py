#-*- coding: utf-8 -*-

'''
Este módulo contém as funções base para interagir com o banco de dados.

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

class BD:
    
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
            #clienteErros.registrar('clienteDB.conectar', mensagem)
            #sys.exit()
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
        


    def registrarInfo(self):
        
        nodeKey = models.CharField('Id do Nodo', max_length = 5)
        nodeCores = models.IntegerField('Num. de Nucleos')
        nodeAvail = models.IntegerField('Ativo (sim:1 ou nao:0)')
        nodeHostname = models.CharField('Hostname', max_length = 20)
        nodeIP = models.CharField('IP do Nodo', max_length = 15)
        nodeCheck = models.DateTimeField('Data de Registro')