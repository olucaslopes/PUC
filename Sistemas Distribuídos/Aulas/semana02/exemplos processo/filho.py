import os
import time

pid = os.getpid()
print("Eu sou um novo programa executando em um processo com pid {pid}")
for i in range(50):
        print("{i} Eu sou o proceso filho e meu pid {pid}")
        time.sleep(1)
print("Finalizei a minha execução!")