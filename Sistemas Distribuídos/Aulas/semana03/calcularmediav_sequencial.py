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
   
if __name__ == '__main__':
    filenames = sys.argv[1:]
    for filename in filenames:
        somar_vendas(filename)
        
