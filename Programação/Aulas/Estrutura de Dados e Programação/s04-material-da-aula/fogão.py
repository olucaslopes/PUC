class Fogão:

    def __init__(self):
        self.temperatura = 0

    def aumentar(self, val):
        self.temperatura += val

    def diminuir(self, val):
        self.temperatura -= val

fogão = Fogão()
fogão.aumentar(100)
print(fogão.temperatura)
