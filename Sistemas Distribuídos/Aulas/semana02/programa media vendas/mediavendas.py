import sys

def somar_vendas(filename,qtd):
   file = open(filename, 'r')
   total = 0;
   for linha in file:
       total = total + float(linha)
       qtd[0] = qtd[0] + 1
   return total
   
if __name__ == '__main__':
    filenames = sys.argv[1:]
    for filename in filenames:
        qtd_vendas = [0]
        total_vendas = somar_vendas(filename,qtd_vendas)
        media = total_vendas/qtd_vendas[0]
        print(f"{filename}: Média das vendas R$ {media}")
        print("quantidade de vendas ",qtd_vendas)

