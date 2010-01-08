from django.db import models

'''

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''
# Create your models here.

import datetime

class Nodes(models.Model):
    
    nodeKey = models.CharField('Id do Nodo', max_length = 5)
    nodeCores = models.IntegerField('Num. de Nucleos')
    nodeAvail = models.IntegerField('Ativo (sim:1 ou nao:0)')
    nodeHostname = models.CharField('Hostname', max_length = 100)
    nodeIP = models.CharField('IP do Nodo', max_length = 15)
    nodeCheck = models.DateTimeField('Data de Registro')
    
class NodeLoad(models.Model):
    nodeKey = models.CharField('Id do Nodo', max_length = 5)
    nodeCores = models.IntegerField('Num. de Cores')
    nodeLoad = models.IntegerField('Carga do No')

class Queue(models.Model):
    
    QueueJobKey = models.CharField('Id do Trabalho', max_length = 10)
    QueueDataPath = models.CharField('Caminho para o arquivo', max_length = 100)
    QueueNodeAssigned = models.CharField('Nodo Alocado', max_length = 5)
    QueueDate = models.DateTimeField('Registro da Atividade')
    QueueStatus = models.IntegerField('Status da atividade')
    
class Job(models.Model):
    
    JobKey = models.CharField('Id do Trabalho', max_length = 10)
    JobUser = models.CharField('Usuario associado', max_length = 10)
    JobDate = models.DateTimeField('Data de Inicio')
    JobDuration = models.IntegerField('Duracao da Tarefa')
    JobDataPath = models.CharField('Caminho do arquivo', max_length = 100)
    
    
