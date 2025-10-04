import tkinter as tk
from tkinter import ttk, messagebox
from inventario import Inventario
from producto import Producto

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventario - UEA")
        self.root.geometry("700x500")
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.inventario = Inventario()
        self.crear_interfaz()

    def crear_interfaz(self):
        info = tk.Label(self.root, text="Estudiante: Jofre Castro\nCarrera: Ingeniería en TI\nParalelo: A", font=("Arial", 12))
        info.pack(pady=10)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Producto", command=self.agregar_producto).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Modificar Producto", command=self.modificar_producto).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar Producto", command=self.eliminar_producto).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Salir", command=self.root.quit).grid(row=0, column=3, padx=5)

        columnas = ("ID", "Nombre", "Cantidad", "Precio")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings")
        for col in columnas:
            self.tabla.heading(col, text=col)
        self.tabla.pack(pady=20, fill="both", expand=True)
        self.root.bind("<Delete>", lambda e: self.eliminar_producto())

        self.cargar_tabla()

    def cargar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for p in self.inventario.mostrar_productos():
            self.tabla.insert("", tk.END, values=(p.id_producto, p.nombre, p.cantidad, p.precio))

    def agregar_producto(self):
        self.mostrar_formulario("Agregar Producto")

    def modificar_producto(self):
        item = self.tabla.focus()
        if not item:
            messagebox.showwarning("Atención", "Seleccione un producto para modificar.")
            return
        valores = self.tabla.item(item, "values")
        self.mostrar_formulario("Modificar Producto", valores)

    def eliminar_producto(self):
        item = self.tabla.focus()
        if not item:
            messagebox.showwarning("Atención", "Seleccione un producto para eliminar.")
            return
        valores = self.tabla.item(item, "values")
        self.inventario.eliminar_producto(valores[0])
        self.cargar_tabla()
        messagebox.showinfo("Eliminado", "Producto eliminado correctamente.")

    def mostrar_formulario(self, titulo, valores=None):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)

        tk.Label(ventana, text="ID:").grid(row=0, column=0)
        id_entry = tk.Entry(ventana)
        id_entry.grid(row=0, column=1)

        tk.Label(ventana, text="Nombre:").grid(row=1, column=0)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=1, column=1)

        tk.Label(ventana, text="Cantidad:").grid(row=2, column=0)
        cantidad_entry = tk.Entry(ventana)
        cantidad_entry.grid(row=2, column=1)

        tk.Label(ventana, text="Precio:").grid(row=3, column=0)
        precio_entry = tk.Entry(ventana)
        precio_entry.grid(row=3, column=1)

        if valores:
            id_entry.insert(0, valores[0])
            nombre_entry.insert(0, valores[1])
            cantidad_entry.insert(0, valores[2])
            precio_entry.insert(0, valores[3])

        def guardar():
            idp = id_entry.get()
            nombre = nombre_entry.get()
            cantidad = int(cantidad_entry.get())
            precio = float(precio_entry.get())

            if valores:
                self.inventario.modificar_producto(idp, nombre, cantidad, precio)
            else:
                self.inventario.agregar_producto(Producto(idp, nombre, cantidad, precio))

            self.cargar_tabla()
            ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
