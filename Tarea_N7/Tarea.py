class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        print(f"📚 Libro creado: '{self.titulo}' de {self.autor}")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"🔐 El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"⚠️ El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"🔓 El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"⚠️ El libro '{self.titulo}' no estaba prestado.")

    def __del__(self):
        print(f"🗑️ Destructor: Eliminando el objeto Libro '{self.titulo}'.")


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []
        print(f"👤 Usuario creado: {self.nombre}")

    def tomar_libro(self, libro):
        if not libro.prestado:
            libro.prestar()
            self.libros_prestados.append(libro)
            print(f"📖 {self.nombre} ha tomado el libro '{libro.titulo}'.")
        else:
            print(f"❌ {self.nombre} no puede tomar el libro '{libro.titulo}' porque ya está prestado.")

    def devolver_libros(self):
        print(f"🔁 {self.nombre} va a devolver todos los libros.")
        for libro in self.libros_prestados:
            libro.devolver()
        self.libros_prestados.clear()

    def __del__(self):
        print(f"🗑️ Destructor: Eliminando el objeto Usuario '{self.nombre}'.")


# Uso del programa
if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("1984", "George Orwell")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")

    # Crear un usuario
    usuario1 = Usuario("Ana")

    # Simular préstamo de libros
    usuario1.tomar_libro(libro1)
    usuario1.tomar_libro(libro2)

    # Devolver libros
    usuario1.devolver_libros()
