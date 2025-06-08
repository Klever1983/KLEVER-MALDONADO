class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def conducir(self):
        print("Conduciendo...")

class Coche(Vehiculo):
    def tocar_bocina(self):
        print("Beep beep!")

# Uso
c = Coche("Toyota")
c.conducir()
c.tocar_bocina()
