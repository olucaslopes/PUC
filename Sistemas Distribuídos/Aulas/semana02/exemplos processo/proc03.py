import sys
import os
import time

pid = os.fork()
if pid == 0:
     fpid = os.getpid()
     print("Eu sou o proceso filho e meu pid",fpid)
     time.sleep(3)
     print("Vou trocar a minha imagem e executar outro programa...")
     os.execlp('python3', 'python3', 'filho.py')
else:
     ppid = os.getpid()
     print("Processo pai (",ppid,") aguardando o processo filho",pid)
     os.wait()
     print("Processo filho ",fpid," finalizou!")
     