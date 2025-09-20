import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x500")

        # Frame Lista de Eventos
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=80)
        self.tree.column("Descripción", width=300)
        self.tree.pack()

        # Frame Entrada de Datos
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=20)

        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(self.frame_entrada, width=50)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Frame Botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento, bg="#4CAF50", fg="white", width=15)
        self.btn_agregar.grid(row=0, column=0, padx=10)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Seleccionado", command=self.eliminar_evento, bg="#f44336", fg="white", width=20)
        self.btn_eliminar.grid(row=0, column=1, padx=10)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit, width=10)
        self.btn_salir.grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
            return

        try:
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Formato Incorrecto", "La hora debe estar en formato HH:MM.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Seleccionar Evento", "Por favor, selecciona un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
        if confirm:
            for item in selected:
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
