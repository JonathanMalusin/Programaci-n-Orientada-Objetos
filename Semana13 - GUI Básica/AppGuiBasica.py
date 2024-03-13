import tkinter as tk
from tkinter import messagebox

class Aplicacion:
    def __init__(self, master):
        self.master = master
        master.title("Aplicación de Ejemplo")

        self.etiqueta = tk.Label(master, text="Ingrese información:")
        self.etiqueta.pack()

        self.campo_texto = tk.Entry(master)
        self.campo_texto.pack()
        # Asociar el evento <Return> (Enter) con la función agregar_info
        self.campo_texto.bind("<Return>", lambda event: self.agregar_info())

        self.agregar_boton = tk.Button(master, text="Agregar", command=self.agregar_info)
        self.agregar_boton.pack()

        self.limpiar_boton = tk.Button(master, text="Limpiar", command=self.limpiar_info)
        self.limpiar_boton.pack()

        self.lista = tk.Listbox(master)
        self.lista.pack()

        # Obtener el tamaño de la pantalla
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (screen_width - master.winfo_reqwidth()) / 2
        y = (screen_height - master.winfo_reqheight()) / 4

        # Definir la geometría de la ventana para centrarla en la pantalla
        master.geometry("+%d+%d" % (x, y))

    def agregar_info(self):
        info = self.campo_texto.get()
        if info:  # Verificar si la caja de texto no está vacía
            self.lista.insert(tk.END, info)
            self.campo_texto.delete(0, tk.END)  # Limpiar el campo de texto después de agregar la información
        else:
            # Mostrar un mensaje de error si la caja de texto está vacía
            messagebox.showerror("Error", "Debe llenar la caja de texto")

    def limpiar_info(self):
        if self.lista.size() > 0:  # Verificar si hay elementos en la lista
            self.lista.delete(0, tk.END)
        else:
            # Mostrar un mensaje si no hay elementos para limpiar
            messagebox.showinfo("Información", "No es necesario limpiar")

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()

