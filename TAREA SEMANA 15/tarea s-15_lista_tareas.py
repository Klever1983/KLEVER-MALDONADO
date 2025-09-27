import tkinter as tk
from tkinter import messagebox


class ListaDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Lista de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # --- Marco principal ---
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.entrada_tarea = tk.Entry(frame, width=30, font=("Arial", 12))
        self.entrada_tarea.grid(row=0, column=0, padx=5)

        # Botón para añadir tarea
        btn_añadir = tk.Button(frame, text="Añadir Tarea", command=self.añadir_tarea)
        btn_añadir.grid(row=0, column=1)

        # Lista donde se mostrarán las tareas
        self.lista_tareas = tk.Listbox(
            self.root,
            width=50,
            height=15,
            selectmode=tk.SINGLE,
            font=("Arial", 10)
        )
        self.lista_tareas.pack(pady=10)

        # Botones de acción
        btn_completar = tk.Button(self.root, text="Marcar como Completada", command=self.marcar_completada)
        btn_completar.pack(pady=5)

        btn_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.pack(pady=5)

        # --- Manejo de eventos ---
        self.root.bind("<Return>", lambda event: self.añadir_tarea())  # Añadir tarea con Enter
        self.lista_tareas.bind("<Double-1>", lambda event: self.marcar_completada())  # Doble clic = completar tarea

    def añadir_tarea(self):
        """Añade una nueva tarea desde el campo de entrada a la lista"""
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def marcar_completada(self):
        """Marca una tarea como completada cambiando su estado visual"""
        try:
            indice = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(indice)

            # Si ya está completada, no volver a marcar
            if tarea.startswith("[✔] "):
                messagebox.showinfo("Información", "Esta tarea ya está completada.")
            else:
                self.lista_tareas.delete(indice)
                self.lista_tareas.insert(indice, "[✔] " + tarea)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista"""
        try:
            indice = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(indice)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareas(root)
    root.mainloop()
