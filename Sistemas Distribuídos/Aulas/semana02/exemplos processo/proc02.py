import sys
import os
import time

pid = os.fork()
if pid == 0:
     fpid = os.getpid()
     for i in range(30):
        print("#",i,"Eu sou o proceso filho e meu pid",fpid)
        time.sleep(1)
else:
     ppid = os.getpid()
     print("Processo pai",ppid,"aguardando o processo filho",pid)
     os.wait()
     print("Processo filho",pid,"finalizou!")
     