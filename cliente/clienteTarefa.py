#-*- coding: utf-8 -*-

'''
Este módulo mantém as funções básicas para efetuar o trabalho.

:version: 0.01
:author: por Eduardo Martins Lopes < edumlopes at gmail.com dot com > 
'''

class Tarefa:
    
    JobKey = None
    programa = None
    nucleos = 0
    
    
    def __init__(self, JobKey, programa):
        import clientePastas
        
        self.JobKey = JobKey
        nome = JobKey

        self.programa = programa
        self.nucleos
        print 'Tarefa %s cadastrada com sucesso.' % (JobKey)
        
        #Definindo os caminhos padrao
        diretorio= clientePastas.listar()[4]
        self.program = clientePastas.listar()[3] + '/pcgamess'
        self.inpIn= diretorio + '/' + nome + '.inp'
        self.logOut = diretorio + '/' + nome + '.log'
        self.punch = diretorio + '/' + 'PUNCH'
    #def descompactar(self, JobKey):
        
        #import clientePastas
        #import zlib
        #import commands
        #import sys
        #from clienteErros import registrar
    
        #diretorios = clientePastas.listar()
        #resultados = diretorios[4] + '/' + usuario + '/' + self.JobKey + '.zip
    def babelPCGamess(self):
        
        import commands
        
        
        
        job = self.JobKey
    def executar(self):
        
        import commands
        import clienteErros
        
        #etapa de otimização        
        print self.programa
        #if self.programa == 'pcgamess':
         
        otimizacao = ' %s -i %s -o %s' %(self.program, self.inpIn, self.logOut)
  
        print otimizacao
        #else:
           # mensagem = u"A tarefa %s exigiu o programa %s e este ainda nao e suportado" %(self.JobKey, self.programa)
            #clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
 
        try:
            rmPunch = 'rm -f %s' &(self.punch)
            outRm = commands.getoutput('rm -f PUNCH') 
            
            out = commands.getoutput(otimizacao)
            
            parseLog(self.logOut)
            
            outRm = commands.getoutput('rm -f PUNCH') 
            
            return 1
        except:
            
            mensagem = u"A Tarefa %s  nao pode ser executada.Verifique a instalacao do programa %s. Mensagem de erro %s" %(self.JobKey, self.programa, out)
            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
            return 0
        
        #etapa de simulacao
    
     
#        if self.== 'pcgamess':
#         
#            simulacao = "gaussian ... "
#        else:
#            mensagem = u"A tarefa %s exigiu o programa %s e este ainda não é suportado" %(self.JobKey, self.programa)
#            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
#
#        try:             
#            out = commands.getoutput(simulacao)
#        except:
#            
#            mensagem = u"A Tarefa %s (fase de simulacao) não pode ser executada. Verifique a instalação do programa %s" %(self.JobKey, self.programa)
#            clienteErros.registrar("Tarefa.executar.otimizacao", mensagem)            
        
    #def otimizar(self, 
    #def compactar(self, JobKey):
        
        #du = ' '

def sumario():
    '''Esta função carrega os dados básicos do Workstation'''
    
    import Chave
    
    tudo = Chave.padrao()
    
    return tudo

def parseLog(nome):
    import clienteErros
    
    logf = open(nome, 'r')
    conteudo = logf.readlines()
   
    #parsing...
    i = 0
    for linha in conteudo:
        #removendo a primeira linha do warning de desatualizado
        if conteudo[i].find('OUTDATED') != -1:
            dummy = conteudo.pop(i)
        i = i + 1
    i = 0
    for linha in conteudo:
        #removendo a segunda linha do warning de desatualizado
        if conteudo[i].find('UPDATES') != -1:            
            dummy = conteudo.pop(i)
        i = i + 1
    #fechando o arquivo
    logf.close()
    
    try:
        logf = open(nome,'w')
        logf.writelines(conteudo)
    except:
        clienteErros.registrar('clienteTarefas.parseLog', 'Nao foi possivel gravar o arquivo de log finalizado, o sistema utilizara o original. ERRO: 0135L')    
    
def Iniciar():
    
    import clienteDB
    import clienteData
    import clienteErros
    import clienteFuncoes
    import clientePastas
    import time
    import Chave
    # ####################################################
    # Main loop
    
    # ####################################################
    #PID stuff
    pidStatus = 1
    pidPath = clientePastas.listar()[1] + '/grid-nodo.pid'
    
    pidf = open(pidPath, 'w')
    pidf.write(str(1))
    pidf.close()
    
    # ####################################################    
    sumario = Chave.padrao()
    try:
        chave = sumario['key']
    except:
        clienteFuncoes.cadastrar()
        sumario = Chave.padrao()
        chave = sumario['key']
        
    # ####################################################    
    grid = clienteDB.banco()
    # ####################################################    
    while pidStatus == 1:
    # ####################################################           
        try:
            grid.HeartBeat()
        except:
            
            grid.Reconectar()
            
            try:
                grid.HeartBeat()
            except:
                clienteErros.registrar("clienteTarefa.iniciar (sessao HearBeat)", "Provavelmente seu workstation nao foi cadastrado ou esta sem acesso a internet")
     
    # ####################################################
        print "chave: ", chave
        tudo = grid.pegarTarefas(chave)
        extensao = tudo.pop()
        aprovadas = tudo.pop()
        
    # ###############################################################
    # Loop principal de execucao das tarefas
        
        for aprovado in aprovadas:

            time.sleep(3)
            grid = clienteDB.banco()
            
            job = Tarefa(aprovado, 'pcgamess')
            
            print "Executando..."
            sucesso = job.executar()
            
            if sucesso == 1:
                grid.registrarConclusao(aprovado)
            if sucesso == 0:
                mensagem = "Houve um insucesso ao executar a tarefa %s" %(aprovado)
                clienteErros.registrar('clienteTarefa.executar', mensagem)
            
            print "atividade realizada"
            
            # ####################################################    
            # Desconexao para garantir que nao caiu a conexao com o banco de dados
            grid.Desconectar()            

        # ####################################################
        #Checar para ver se o arquivo ainda existe, caso contrário termina a execução do programa
        try:
            pid = open(pidPath, 'r')
            pid.close()
        except:
            pidStatus = 0
            print "O programa sera parado, pois nao foi possivel localizar o arquivo %s" %(pidPath)
        # ####################################################       
        mensagem = "Para parar o servidor, remova o arquivo %s ou use os metodos mais tradicionais" %(pidPath)
        print mensagem
        time.sleep(5)