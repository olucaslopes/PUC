from threading import Thread 
from time import sleep 
import sys
import time

def somar_vendas(filename):
   file = open(filename, 'r')
   total = 0
   i = 0
   for linha in file:
       total = total + float(linha)
       time.sleep(0.001)
       i = i+1
   media = total/i
   print(filename," - Média das vendas: ",media)

if __name__ == "__main__": 
    filenames = sys.argv[1:]
    threads = []
    i = 0
    for filename in filenames:
        qtd_vendas = [0]
        thread = Thread(target = somar_vendas, args = (filename,))
        threads.append(thread)
        thread.start();
        i = i + 1
    
    for j in range(i):
        threads[j].join() 
    print("threads finalizaram com sucesso...") 