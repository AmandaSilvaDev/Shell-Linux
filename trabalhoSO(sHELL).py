from audioop import reverse
import os
from time import sleep

#funções para visualizar os id de pai e filho;
def Verfilho():
        print("Sou o Filho: PID {}. Meu pai é {}".format(os.getpid(),os.getppid()))
        print("eu sou o filho execultando:1")
        sleep(1)
        print("eu sou o filho execultando:2")
        sleep(1)
        print("eu sou o filho execultando:3")
        sleep(1)
        print("eu sou o filho execultando:4")
        sleep(1)
        print("eu sou o filho execultando:5")
        
def Verpai():
        print("Sou o Pai: PID {}.".format(os.getppid()))

        
def history():
    i = len(histo)+1
    for c in histo[-10:]:
        i -=1
        print("{} - {}".format(i-1,c))

#historico
histo = []

#inicio do shell
while True:
    
    print("osh>")
    entrada = input()
    histo.append(entrada)

    x = entrada.split(" ") #fatiamento para acessar os comandos

    #parte do  & 
    if x[len(x)-1] =="&":
        isConcurrent = True
        #para usar o excvp tem que tirar o & para n dar erro
        x.remove("&")
    else: #caso nao tenha & nao tem concorrentes
        isConcurrent = False
    print("É concorrente?",isConcurrent)
    

    #criando o processo filho
    pid = os.fork()


    if pid ==0: #caso o processo filho der certo
        
        if entrada == "history":
            history()
        else:
            Verfilho()
            Verpai()
            os.execvp(x[0],x) 
  
                
    else:
        if isConcurrent == False:
            os.wait()
        elif isConcurrent == True:
            pass
        print("eu sou o pai execultando:1")
        sleep(1)
        print("eu sou o pai execultando:2")
        sleep(1)
        print("eu sou o pai execultando:3")
        sleep(1)
        print("eu sou o pai execultando:4")
        sleep(1)
        print("eu sou o pai execultando:5")
        