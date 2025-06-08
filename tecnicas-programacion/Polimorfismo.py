class Ave:
    def hacer_sonido(self):
        print("Algun sonido")

class Loro(Ave):
    def hacer_sonido(self):
        print("Hola")

class Paloma(Ave):
    def hacer_sonido(self):
        print("Ruuuu")

# Uso
aves = [Loro(), Paloma()]
for ave in aves:
    ave.hacer_sonido()
