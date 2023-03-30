class Lâmpada:

    def __init__(self, estado):
        # Atributos de cada objeto criado a partir desta classe.
        # O self indica que estes são atributos dos objetos
        self.estado = estado

    def troca(self):
        self.estado = not self.estado

lamp = Lâmpada(True)
print(lamp.estado)

lamp.troca()
print(lamp.estado)

lamp.troca()
print(lamp.estado)
