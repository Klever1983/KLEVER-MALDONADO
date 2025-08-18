# inventario.py
from dataclasses import dataclass
from typing import List, Optional

# ===========================
# Clase Producto
# ===========================
@dataclass
class Producto:
    id: str          # único
    nombre: str
    cantidad: int
    precio: float

    def __str__(self) -> str:
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio:.2f}"


# ===========================
# Clase Inventario
# ===========================
class Inventario:
    def __init__(self) -> None:
        self._productos: List[Producto] = []

    # Asegura ID único
    def agregar_producto(self, p: Producto) -> bool:
        if self._buscar_por_id(p.id) is not None:
            return False
        self._productos.append(p)
        return True

    def eliminar_por_id(self, id_: str) -> bool:
        p = self._buscar_por_id(id_)
        if p is None:
            return False
        self._productos.remove(p)
        return True

    def actualizar_cantidad(self, id_: str, nueva_cantidad: int) -> bool:
        p = self._buscar_por_id(id_)
        if p is None:
            return False
        p.cantidad = nueva_cantidad
        return True

    def actualizar_precio(self, id_: str, nuevo_precio: float) -> bool:
        p = self._buscar_por_id(id_)
        if p is None:
            return False
        p.precio = nuevo_precio
        return True

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        needle = texto.strip().lower()
        return [p for p in self._productos if needle in p.nombre.lower()]

    def listar_todos(self) -> List[Producto]:
        return list(self._productos)

    # --- helper privado ---
    def _buscar_por_id(self, id_: str) -> Optional[Producto]:
        for p in self._productos:
            if p.id.lower() == id_.lower():
                return p
        return None


# ===========================
# Interfaz de Usuario (Consola)
# ===========================
def leer_texto(prompt: str) -> str:
    s = input(prompt).strip()
    while not s:
        s = input("No puede estar vacío. Intenta de nuevo: ").strip()
    return s

def leer_entero(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Ingresa un número entero válido.")

def leer_float(prompt: str) -> float:
    while True:
        try:
            # Usa punto decimal (ej: 12.5)
            return float(input(prompt).strip())
        except ValueError:
            print("Ingresa un número decimal válido (usa punto).")

def mostrar_menu() -> None:
    print("======= SISTEMA DE INVENTARIOS =======")
    print("1) Añadir nuevo producto")
    print("2) Eliminar producto por ID")
    print("3) Actualizar CANTIDAD por ID")
    print("4) Actualizar PRECIO por ID")
    print("5) Buscar producto(s) por NOMBRE")
    print("6) Mostrar todos los productos")
    print("0) Salir")

def opcion_agregar(inv: Inventario) -> None:
    print("-- Añadir producto --")
    id_ = leer_texto("ID (único): ")
    nombre = leer_texto("Nombre: ")
    cantidad = leer_entero("Cantidad: ")
    precio = leer_float("Precio: ")
    ok = inv.agregar_producto(Producto(id=id_, nombre=nombre, cantidad=cantidad, precio=precio))
    print("Producto agregado." if ok else "ERROR: ya existe un producto con ese ID.")

def opcion_eliminar(inv: Inventario) -> None:
    print("-- Eliminar producto --")
    id_ = leer_texto("ID a eliminar: ")
    print("Eliminado." if inv.eliminar_por_id(id_) else "No se encontró ese ID.")

def opcion_actualizar_cantidad(inv: Inventario) -> None:
    print("-- Actualizar CANTIDAD --")
    id_ = leer_texto("ID: ")
    nueva = leer_entero("Nueva cantidad: ")
    print("Cantidad actualizada." if inv.actualizar_cantidad(id_, nueva) else "No se encontró ese ID.")

def opcion_actualizar_precio(inv: Inventario) -> None:
    print("-- Actualizar PRECIO --")
    id_ = leer_texto("ID: ")
    nuevo = leer_float("Nuevo precio: ")
    print("Precio actualizado." if inv.actualizar_precio(id_, nuevo) else "No se encontró ese ID.")

def opcion_buscar_nombre(inv: Inventario) -> None:
    print("-- Buscar por nombre --")
    q = leer_texto("Texto a buscar: ")
    resultados = inv.buscar_por_nombre(q)
    if not resultados:
        print("Sin coincidencias.")
    else:
        print("Coincidencias:")
        for p in resultados:
            print(p)

def opcion_listar_todos(inv: Inventario) -> None:
    print("-- Listado de productos --")
    lista = inv.listar_todos()
    if not lista:
        print("Inventario vacío.")
    else:
        for p in lista:
            print(p)

def main() -> None:
    inv = Inventario()
    while True:
        mostrar_menu()
        op = leer_entero("Elige una opción: ")
        if op == 1:
            opcion_agregar(inv)
        elif op == 2:
            opcion_eliminar(inv)
        elif op == 3:
            opcion_actualizar_cantidad(inv)
        elif op == 4:
            opcion_actualizar_precio(inv)
        elif op == 5:
            opcion_buscar_nombre(inv)
        elif op == 6:
            opcion_listar_todos(inv)
        elif op == 0:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
        print()  # línea en blanco

if __name__ == "__main__":
    main()
