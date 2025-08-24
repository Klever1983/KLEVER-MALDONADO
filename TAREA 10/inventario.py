#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Gestión de Inventarios (versión con archivos y manejo robusto de excepciones)
----------------------------------------------------------------------------------------
Características clave:
- Persiste el inventario en un archivo de texto JSON (inventario.json).
- Carga automática al iniciar; si el archivo no existe se crea.
- Maneja excepciones comunes: FileNotFoundError, PermissionError, JSONDecodeError, OSError.
- Recuperación ante archivo corrupto: realiza un respaldo automático y reinicia un archivo sano.
- Interfaz de consola con mensajes claros de éxito/fallo en operaciones.
- Escritura atómica mediante archivo temporal + os.replace para reducir riesgo de corrupción.

Formato de almacenamiento:
- JSON con una lista de productos, cada producto es un dict con claves: id, nombre, cantidad, precio.

Uso:
- Ejecutar:  python inventario.py
"""

from __future__ import annotations
import json
import os
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, List, Optional, Tuple


ARCHIVO_POR_DEFECTO = "inventario.json"


@dataclass
class Producto:
    id: str
    nombre: str
    cantidad: int
    precio: float

    @staticmethod
    def desde_dict(d: Dict) -> "Producto":
        # Validación y conversión segura de tipos
        return Producto(
            id=str(d.get("id", "")).strip(),
            nombre=str(d.get("nombre", "")).strip(),
            cantidad=int(d.get("cantidad", 0)),
            precio=float(d.get("precio", 0.0)),
        )


class Inventario:
    def __init__(self, ruta_archivo: str = ARCHIVO_POR_DEFECTO) -> None:
        self.ruta_archivo = ruta_archivo
        self.productos: Dict[str, Producto] = {}
        ok, msg = self.cargar_desde_archivo()
        # Notar: no imprimimos aquí para no ensuciar salida en tests, pero la UI reporta estos mensajes.
        self._ultimo_mensaje_inicio = msg

    # ---------------------- Persistencia ----------------------
    def cargar_desde_archivo(self) -> Tuple[bool, str]:
        """
        Carga el inventario desde el archivo JSON. Si el archivo no existe, lo crea vacío.
        Maneja archivo corrupto realizando respaldo y reinicio seguro.
        """
        try:
            if not os.path.exists(self.ruta_archivo):
                # Crear archivo vacío
                self._guardar_lista_productos([])  # crea el archivo sano
                self.productos = {}
                return True, f"Archivo '{self.ruta_archivo}' no encontrado. Se creó uno nuevo."
            # Leer y decodificar JSON
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise json.JSONDecodeError("El contenido no es una lista JSON.", doc=str(data), pos=0)
            self.productos = {}
            for item in data:
                p = Producto.desde_dict(item)
                if p.id:  # ignorar registros sin id
                    self.productos[p.id] = p
            return True, f"Inventario cargado correctamente desde '{self.ruta_archivo}'. Productos: {len(self.productos)}"
        except FileNotFoundError:
            # Raza de condición: fue borrado entre exists() y open()
            try:
                self._guardar_lista_productos([])
                self.productos = {}
                return True, f"Archivo '{self.ruta_archivo}' no encontrado. Se creó uno nuevo."
            except PermissionError:
                return False, f"Permiso denegado al crear '{self.ruta_archivo}'. Verifique permisos de escritura."
        except PermissionError:
            return False, f"Permiso denegado al leer '{self.ruta_archivo}'. Ejecute con permisos adecuados."
        except json.JSONDecodeError:
            # Archivo corrupto: crear respaldo y reiniciar
            backup = self._respaldar_archivo_corrupto()
            try:
                self._guardar_lista_productos([])
                self.productos = {}
                return False, (
                    f"El archivo estaba corrupto. Se creó un respaldo en '{backup}' y se reinició '{self.ruta_archivo}' vacío."
                )
            except PermissionError:
                return False, (
                    f"El archivo estaba corrupto y no se pudo crear uno nuevo por permisos insuficientes. Respaldo en '{backup}'."
                )
        except OSError as e:
            return False, f"Error del sistema al leer '{self.ruta_archivo}': {e}"

    def guardar_en_archivo(self) -> Tuple[bool, str]:
        """Guarda el inventario actual al archivo en modo atómico (temp + replace)."""
        try:
            lista = [asdict(p) for p in self.productos.values()]
            self._guardar_lista_productos(lista)
            return True, f"Inventario guardado en '{self.ruta_archivo}'."
        except PermissionError:
            return False, f"Permiso denegado al escribir en '{self.ruta_archivo}'. Cierre el archivo si está abierto o cambie permisos."
        except OSError as e:
            return False, f"Error del sistema al guardar '{self.ruta_archivo}': {e}"

    def _guardar_lista_productos(self, lista: List[Dict]) -> None:
        """Escritura atómica: escribe en archivo temporal y luego reemplaza."""
        tmp = f"{self.ruta_archivo}.tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, self.ruta_archivo)

    def _respaldar_archivo_corrupto(self) -> str:
        base, ext = os.path.splitext(self.ruta_archivo)
        marca = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup = f"{base}.corrupto-{marca}{ext or '.json'}"
        try:
            if os.path.exists(self.ruta_archivo):
                os.replace(self.ruta_archivo, backup)
        except OSError:
            # Como último recurso, intentar copiar
            try:
                from shutil import copyfile
                copyfile(self.ruta_archivo, backup)
            except Exception:
                backup = "(no se pudo crear respaldo)"
        return backup

    # ---------------------- Operaciones CRUD ----------------------
    def agregar(self, producto: Producto) -> Tuple[bool, str]:
        if producto.id in self.productos:
            return False, f"Ya existe un producto con id '{producto.id}'."
        if producto.cantidad < 0 or producto.precio < 0:
            return False, "Cantidad y precio deben ser no negativos."
        self.productos[producto.id] = producto
        ok, msg = self.guardar_en_archivo()
        if ok:
            return True, f"Producto '{producto.nombre}' agregado y guardado correctamente."
        else:
            # revertir en memoria si guardar falla
            self.productos.pop(producto.id, None)
            return False, f"No se pudo guardar el producto. {msg}"

    def actualizar(self, id_: str, nombre: Optional[str] = None, cantidad: Optional[int] = None, precio: Optional[float] = None) -> Tuple[bool, str]:
        if id_ not in self.productos:
            return False, f"No existe producto con id '{id_}'."
        p = self.productos[id_]
        if nombre is not None:
            p.nombre = nombre.strip()
        if cantidad is not None:
            if cantidad < 0:
                return False, "La cantidad no puede ser negativa."
            p.cantidad = cantidad
        if precio is not None:
            if precio < 0:
                return False, "El precio no puede ser negativo."
            p.precio = precio
        ok, msg = self.guardar_en_archivo()
        if ok:
            return True, f"Producto '{id_}' actualizado y guardado correctamente."
        else:
            return False, f"No se pudo guardar el cambio. {msg}"

    def eliminar(self, id_: str) -> Tuple[bool, str]:
        if id_ not in self.productos:
            return False, f"No existe producto con id '{id_}'."
        p = self.productos.pop(id_)
        ok, msg = self.guardar_en_archivo()
        if ok:
            return True, f"Producto '{p.nombre}' eliminado y cambios guardados."
        else:
            # si falló el guardado, intentar restaurar
            self.productos[id_] = p
            return False, f"No se pudo guardar la eliminación. {msg}"

    def buscar_por_id(self, id_: str) -> Optional[Producto]:
        return self.productos.get(id_)

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        t = texto.lower().strip()
        return [p for p in self.productos.values() if t in p.nombre.lower()]

    def listar(self) -> List[Producto]:
        return list(self.productos.values())

    # ---------------------- Utilidades ----------------------
    def mensaje_inicio(self) -> str:
        """Mensaje informativo de la carga inicial."""
        return self._ultimo_mensaje_inicio


# ---------------------- Interfaz de Usuario (Consola) ----------------------
def input_no_vacio(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("⚠ Entrada vacía. Intente de nuevo.")

def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠ Ingrese un número entero válido.")

def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠ Ingrese un número (puede incluir decimales) válido.")


def mostrar_producto(p: Producto) -> None:
    print(f"- ID: {p.id} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: {p.precio:.2f}")


def menu() -> None:
    inv = Inventario()
    # Reportar estado de carga de archivo
    print(inv.mensaje_inicio())

    opciones = {
        "1": "Listar productos",
        "2": "Agregar producto",
        "3": "Actualizar producto",
        "4": "Eliminar producto",
        "5": "Buscar por ID",
        "6": "Buscar por nombre",
        "7": "Exportar a CSV",
        "0": "Salir"
    }

    def exportar_csv(ruta: str = "inventario.csv") -> Tuple[bool, str]:
        import csv
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as f:
                w = csv.writer(f)
                w.writerow(["id", "nombre", "cantidad", "precio"])
                for p in inv.listar():
                    w.writerow([p.id, p.nombre, p.cantidad, f"{p.precio:.2f}"])
            return True, f"Inventario exportado a '{ruta}'."
        except PermissionError:
            return False, f"Permiso denegado al escribir '{ruta}'. Cierre el archivo si está abierto o cambie permisos."
        except OSError as e:
            return False, f"Error del sistema al exportar CSV: {e}"

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        for k in sorted(opciones):
            print(f"{k}. {opciones[k]}")
        elec = input("Seleccione una opción: ").strip()

        if elec == "1":
            prods = inv.listar()
            if not prods:
                print("ℹ No hay productos registrados.")
            else:
                print(f"Productos en inventario: {len(prods)}")
                for p in prods:
                    mostrar_producto(p)

        elif elec == "2":
            print(">> Agregar producto")
            id_ = input_no_vacio("ID: ")
            nombre = input_no_vacio("Nombre: ")
            cantidad = input_int("Cantidad: ")
            precio = input_float("Precio: ")
            ok, msg = inv.agregar(Producto(id_, nombre, cantidad, precio))
            print(("✅ " if ok else "❌ ") + msg)

        elif elec == "3":
            print(">> Actualizar producto")
            id_ = input_no_vacio("ID del producto a actualizar: ")
            if not inv.buscar_por_id(id_):
                print("❌ No existe ese ID.")
                continue
            print("Deje en blanco para no cambiar un campo.")
            nombre = input("Nuevo nombre: ").strip()
            cantidad_txt = input("Nueva cantidad: ").strip()
            precio_txt = input("Nuevo precio: ").strip()

            nombre_val = nombre if nombre else None
            cantidad_val = None
            precio_val = None
            if cantidad_txt:
                try:
                    cantidad_val = int(cantidad_txt)
                except ValueError:
                    print("❌ Cantidad inválida. Operación cancelada.")
                    continue
            if precio_txt:
                try:
                    precio_val = float(precio_txt)
                except ValueError:
                    print("❌ Precio inválido. Operación cancelada.")
                    continue
            ok, msg = inv.actualizar(id_, nombre_val, cantidad_val, precio_val)
            print(("✅ " if ok else "❌ ") + msg)

        elif elec == "4":
            print(">> Eliminar producto")
            id_ = input_no_vacio("ID del producto a eliminar: ")
            ok, msg = inv.eliminar(id_)
            print(("✅ " if ok else "❌ ") + msg)

        elif elec == "5":
            id_ = input_no_vacio("ID a buscar: ")
            p = inv.buscar_por_id(id_)
            if p:
                print("Resultado de la búsqueda:")
                mostrar_producto(p)
            else:
                print("ℹ No se encontró producto con ese ID.")

        elif elec == "6":
            txt = input_no_vacio("Texto a buscar en el nombre: ")
            res = inv.buscar_por_nombre(txt)
            if not res:
                print("ℹ No se encontraron coincidencias.")
            else:
                print(f"Se encontraron {len(res)} coincidencias:")
                for p in res:
                    mostrar_producto(p)

        elif elec == "7":
            ruta = input("Ruta del CSV (Enter para 'inventario.csv'): ").strip() or "inventario.csv"
            ok, msg = exportar_csv(ruta)
            print(("✅ " if ok else "❌ ") + msg)

        elif elec == "0":
            print("¡Hasta luego!")
            break

        else:
            print("⚠ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nInterrupción por teclado. Saliendo...")
        sys.exit(130)
