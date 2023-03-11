import sys

def somar_vendas(filename):
   file = open(filename, 'r')
   total = 0;
   for linha in file:
       total = total + float(linha)
   return total
   
if __name__ == '__main__':
    filenames = sys.argv[1:]
    for filename in filenames:
        total_vendas = somar_vendas(filename)
        print(f"{filename}: R$ {total_vendas}")
