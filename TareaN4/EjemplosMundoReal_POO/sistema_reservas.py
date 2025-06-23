"""
Finalidad del Ejemplo:
Este programa modela un sistema de reservas de hotel utilizando Programación Orientada a Objetos (POO).
Representa una situación del mundo real donde se gestionan habitaciones, clientes y reservas mediante
clases que simulan su comportamiento e interacción. El objetivo es demostrar cómo la POO permite organizar
y estructurar soluciones eficientes a problemas cotidianos.
"""

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} - Tipo: {self.tipo}, Precio: ${self.precio} - {estado}"


class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} (Cédula: {self.cedula})"


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_disponibles(self):
        print("\nHabitaciones disponibles:")
        disponibles = False
        for hab in self.habitaciones:
            if hab.disponible:
                print(hab)
                disponibles = True
        if not disponibles:
            print("No hay habitaciones disponibles en este momento.")

    def reservar_habitacion(self, numero, cliente):
        for hab in self.habitaciones:
            if hab.numero == numero:
                if hab.disponible:
                    hab.reservar()
                    print(f"\nReserva confirmada para {cliente.nombre} en la habitación {hab.numero}.")
                    return
                else:
                    print("La habitación seleccionada está ocupada.")
                    return
        print("Número de habitación no encontrado.")


# Bloque principal de ejecución interactiva
if __name__ == "__main__":
    hotel = Hotel("Hotel Interactivo")

    # Agregar algunas habitaciones al sistema
    hotel.agregar_habitacion(Habitacion(101, "Simple", 30))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 50))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 80))

    while True:
        print("\n=== Sistema de Reservas ===")
        hotel.mostrar_disponibles()

        opcion = input("\n¿Deseas hacer una reserva? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del sistema.")
            break

        nombre = input("Ingresa el nombre del cliente: ")
        cedula = input("Ingresa la cédula del cliente: ")
        cliente = Cliente(nombre, cedula)

        try:
            numero = int(input("Ingresa el número de habitación a reservar: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        hotel.reservar_habitacion(numero, cliente)
