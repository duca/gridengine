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
        
    def Conectar(self, db):
        
        import MySQLdb
        import sys
        try:
            con = MySQLdb.connect(self.servidor, self.usuario, self.senha)
            con.select_db(db)
            self.cursor = con.cursor()
            return self.cursor
                        
        except:
            
            mensagem = "Nao foi possivel conectar ao servidor. Verifique a conexao e tente mais tarde"
            print mensagem
            #clienteErros.registrar('clienteDB.conectar', mensagem)
            #sys.exit()

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
