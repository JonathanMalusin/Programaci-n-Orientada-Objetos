import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar  # Instala este paquete si no lo tienes: pip install tkcalendar

class EventManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Eventos")

        # Contenedor para la lista de eventos
        self.event_frame = ttk.Frame(root)
        self.event_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Lista de eventos
        self.event_tree = ttk.Treeview(self.event_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.event_tree.heading("Fecha", text="Fecha")
        self.event_tree.heading("Hora", text="Hora")
        self.event_tree.heading("Descripción", text="Descripción")
        self.event_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar para la lista de eventos
        event_scroll = ttk.Scrollbar(self.event_frame, orient="vertical", command=self.event_tree.yview)
        event_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.event_tree.configure(yscrollcommand=event_scroll.set)

        # Contenedor para los campos de entrada
        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(padx=10, pady=5, fill=tk.BOTH)

        # Etiquetas y campos de entrada
        ttk.Label(self.input_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.date_entry = ttk.Entry(self.input_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.time_entry = ttk.Entry(self.input_frame)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.desc_entry = ttk.Entry(self.input_frame)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones de acción
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(padx=10, pady=5, fill=tk.BOTH)

        ttk.Button(self.button_frame, text="Agregar Evento", command=self.add_event).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Eliminar Evento Seleccionado", command=self.delete_selected_event).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        # Verificar si todos los campos están completos
        if not date or not time or not desc:
            messagebox.showerror("Error", "Por favor completa todos los campos.")
            return

        # Agregar evento a la lista
        self.event_tree.insert("", "end", values=(date, time, desc))

        # Limpiar campos de entrada
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_selected_event(self):
        selected_item = self.event_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor selecciona un evento para eliminar.")
            return

        # Confirmación opcional para eliminar evento
        confirmation = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres eliminar este evento?")
        if confirmation:
            self.event_tree.delete(selected_item)

def main():
    root = tk.Tk()
    app = EventManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
