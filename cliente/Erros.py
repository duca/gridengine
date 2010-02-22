#-*- coding:latin-1 -*-

'''
Este modulo cuida do registro dos logs do programa e está divido em funcoes para criar os arquivos e os preencher
'''
    
def registrar(nomeDaFuncao, mensagem):
    
    from datetime import datetime
    import clientePastas
    import sys
    
    
    diretorios = clientePastas.listar()
    sisLog = diretorios[2]+'/erros.log'
    
    try:
        registro = open(sisLog, 'a')

    except:
        
        clientePastas.criar()

    
    timestamp = datetime.now()
    separadorHora = ":"
    separadorData = "/"
    
    
    horario = str(timestamp.hour) + separadorHora + str(timestamp.minute) + " " + str(timestamp.day) + separadorData + str(timestamp.month) + separadorData + str(timestamp.year)
    
    mensagem = horario + " Funcao: " + nomeDaFuncao + " Mensagem: " + mensagem + "\n"
    
    try:
        registro.write(mensagem)
        
    except:

        clientePastas.criar()
        
        try:
            registro.write(mensagem)
        except:
            erro = horario + "Nao foi possivel registrar o evento de erro " + erro + ", entretanto o programa tentara seguir assim mesmo \n"
            sys.stderr.write(mensagem)            