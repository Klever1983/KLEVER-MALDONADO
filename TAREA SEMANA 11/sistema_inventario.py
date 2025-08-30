import pickle

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = str(id_producto)  # ahora siempre será texto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def establecer_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {ID: Producto}

    def agregar_producto(self, producto):
        if producto.obtener_id() not in self.productos:
            self.productos[producto.obtener_id()] = producto
        else:
            print(f"⚠️ Producto con ID '{producto.obtener_id()}' ya existe.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"✅ Producto '{id_producto}' eliminado.")
        else:
            print(f"⚠️ Producto con ID '{id_producto}' no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.establecer_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.establecer_precio(nuevo_precio)
            print(f"✅ Producto '{id_producto}' actualizado.")
        else:
            print(f"⚠️ Producto con ID '{id_producto}' no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.obtener_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("⚠️ No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("📦 El inventario está vacío.")

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)
        print(f"💾 Inventario guardado en '{archivo}'.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
            print(f"📂 Inventario cargado desde '{archivo}'.")
        except FileNotFoundError:
            print(f"⚠️ El archivo '{archivo}' no existe.")


def mostrar_menu():
    print("\n---- Menú de Gestión de Inventario ----")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")


def menu():
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto (puede ser texto): ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")

            if nueva_cantidad:
                nueva_cantidad = int(nueva_cantidad)
            else:
                nueva_cantidad = None

            if nuevo_precio:
                nuevo_precio = float(nuevo_precio)
            else:
                nuevo_precio = None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            archivo = input("Nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(archivo)

        elif opcion == "7":
            archivo = input("Nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(archivo)

        elif opcion == "8":
            print("👋 Saliendo...")
            break

        else:
            print("⚠️ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
