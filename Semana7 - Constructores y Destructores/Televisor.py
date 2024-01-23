class Televisor:
    def __init__(self, marca, color, pulgadas, os):
        # Constructor: Se ejecuta al crear una instancia de la clase.
        self.marca = marca
        self.color = color
        self.pulgadas = pulgadas
        self.os = os
        print(f"Se ha creado un objeto Televisor de marca {self.marca}, color {self.color}, de {self.pulgadas} pulgadas, Sistema: {self.os}")

    def operacion(self):
        # Método de ejemplo
        print(f"Ejecutando una operación en el objeto {self.marca}, {self.color}, {self.pulgadas}, {self.os}")

    def __del__(self):
        # Destructor: Se ejecuta al eliminar una instancia de la clase.
        print(f"Se está destruyendo el objeto {self.marca}, {self.color}, {self.pulgadas}, {self.os}")

# instancias de la clase utilizando los constructores y destructores
objeto1 = Televisor("TCL", "Negro", 55, "Google TV")
objeto1.operacion()
del objeto1  # Al eliminar la referencia, se activa el destructor

# otra instancia de la clase
objeto2 = Televisor("Samsung", "Blanco", 42, "WebOS")
objeto2.operacion()
# No es necesario llamar a del objeto2, ya que el destructor se ejecutará automáticamente al finalizar el programa
