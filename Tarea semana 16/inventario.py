import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="datos.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()

    def modificar_producto(self, id_producto, nombre, cantidad, precio):
        for p in self.productos:
            if p.id_producto == id_producto:
                p.set_nombre(nombre)
                p.set_cantidad(cantidad)
                p.set_precio(precio)
        self.guardar_en_archivo()

    def mostrar_productos(self):
        return self.productos

    def guardar_en_archivo(self):
        with open(self.archivo, "w") as f:
            for p in self.productos:
                f.write(f"{p.id_producto},{p.nombre},{p.cantidad},{p.precio}\n")

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                for linea in f:
                    idp, nombre, cantidad, precio = linea.strip().split(",")
                    self.productos.append(Producto(idp, nombre, int(cantidad), float(precio)))
