#-*- coding: utf-8 -*-

'''
Este módulo contém as funções que registram, no banco de dados, as informações relativas ao nó em que foi instalado

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

class clienteDB:
    
    usuario = None
    senha = None
    servidor = None
    
    def __ini__(self, usuario, senha, servidor):
        
        self.usuario = usuario
        self.senha = senha
        self.servidor = servidor
        
    def conectar(self):
        
        import MySQLdb
        import clienteErros
        import sys
        
        try:
            con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
                        
        except:
            
            mensagem = "Nao foi possivel conectar ao servidor. Verifique a conexao e tente mais tarde"
            clienteErros.registrar('clienteDB.conectar', mensagem)
            sys.exit()
        con.select_db("grid")
        self.cursor = con.cursor()
        
        def verificarKey(self,chave):

            querysql = "select NodeKey from Nodes"
            self.cursor.execute(querysql)
            chaves = self.cursor.fetchall() #envia o conteudo da tabela numa lista
            
            for results in chaves: #loop por toda a lista de resultadods
                
                if chave == chaves:
                    
                    confere = 'sim'
                    break
                
                else:
                    
                    confere = 'nao'
                    
            return confere 
             


def registrarInfo():

    nodeKey = models.CharField('Id do Nodo', max_length = 5)
    nodeCores = models.IntegerField('Num. de Nucleos')
    nodeAvail = models.IntegerField('Ativo (sim:1 ou nao:0)')
    nodeHostname = models.CharField('Hostname', max_length = 20)
    nodeIP = models.CharField('IP do Nodo', max_length = 15)
    nodeCheck = models.DateTimeField('Data de Registro')