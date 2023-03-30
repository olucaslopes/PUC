import sys
import os

if __name__ == '__main__':
    filenames = sys.argv[1:]
    for filename in filenames:
        filho = os.fork()
        if filho == 0:
          os.execlp('python3', 'python3', 'calcularmediav.py', filename)
        else:
           print("processo filho ",filho," criado")
    print("Processo pai aguardando o(s) processo(s) filho(s)")
    os.wait();
    print("Processos filhos terminaram com sucesso!")
          

