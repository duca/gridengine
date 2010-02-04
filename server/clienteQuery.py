#-*-coding: utf-8 -*-
'''
Este módulo é usado para encapsular as montagens de Query, formando um midware entre o Database.py e a função propriamente dita. Foi pensado assim para evitar problemas numa eventual migração para outro modelo de banco de dados

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

def heartBeat(nodeKey, nodeCores, nodeLoad):
    
    querysql = "insert into NodeLoad (nodeKey, nodeCores, nodeLoad) values (%s, %i, %i) %(nodeKey, nodeCores, nodeLoad)"
    
    return querysql

def nodeData(nodeKey, nodeCores, nodeAvail, nodeHostname, nodeIP):
    
    querysql = "insert into Nodes (nodeKey, nodeCores, nodeAvail, nodeHostname, nodeIP) values (%s, %i, %i, %s, %s) %(nodeKey, nodeCores, nodeAvail, nodeHostname, nodeIP)"
    
    return querysql

def nodeQueue(nodeKey):
    
    QueueJobKey = models.CharField('Id do Trabalho', max_length = 10)
    QueueDataPath = models.CharField('Caminho para o arquivo', max_length = 100)
    QueueNodeAssigned = models.CharField('Nodo Alocado', max_length = 5)
    QueueDate = models.DateTimeField('Registro da Atividade')
    QueueStatus = models.IntegerField('Status da atividade')
    
def checkKey(chave):
    
    querysql = "select NodeKey, nodeKey from Nodes"
    
    return querysql
