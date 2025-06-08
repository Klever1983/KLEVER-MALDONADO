class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # atributo privado

    def obtener_nombre(self):
        return self.__nombre

# Uso
p = Persona("Ana")
print(p.obtener_nombre())
