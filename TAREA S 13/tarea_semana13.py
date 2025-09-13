# -------------------------------------------------------
# TAREA SEMANA 13 - Creación de una Aplicación GUI Básica
# Autor: [Tu Nombre o Usuario]
# Descripción:
#   Esta aplicación permite al usuario agregar datos a través
#   de un campo de texto y mostrarlos en una lista. Además,
#   incluye un botón para limpiar la lista o eliminar la
#   información seleccionada.
#
# Librería utilizada: Tkinter (Python)
# -------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_texto.get()  # Obtener el texto ingresado
    if dato.strip() != "":  # Validar que no esté vacío
        lista_datos.insert(tk.END, dato)  # Insertar al final de la lista
        entrada_texto.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un texto válido.")

# Función para limpiar la lista completa
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Función para eliminar el ítem seleccionado
def eliminar_seleccionado():
    seleccion = lista_datos.curselection()  # Obtener índice seleccionado
    if seleccion:
        lista_datos.delete(seleccion)
    else:
        messagebox.showinfo("Información", "Seleccione un elemento para eliminar.")

# ----------------- INTERFAZ GRÁFICA -------------------

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica - Semana 13")
ventana.geometry("400x350")  # Ancho x Alto
ventana.resizable(False, False)  # No redimensionable

# Etiqueta de título
label_titulo = tk.Label(ventana, text="Gestor de Datos", font=("Arial", 14, "bold"))
label_titulo.pack(pady=10)

# Campo de texto con etiqueta
label_entrada = tk.Label(ventana, text="Ingrese un dato:")
label_entrada.pack()
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar", width=10, command=agregar_dato)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=10, command=eliminar_seleccionado)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", width=10, command=limpiar_lista)
btn_limpiar.grid(row=0, column=2, padx=5)

# Lista para mostrar los datos
label_lista = tk.Label(ventana, text="Datos ingresados:")
label_lista.pack()
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
