#EjemploHerencia
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_info(self):
        """Devuelve la información del vehículo."""
        return f'{self.marca} {self.modelo}'

# Clase que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

# Uso de la herencia
coche = Coche("Hyundai", "Tucson", "Gris")
print(coche.obtener_info() + f', Color: {coche.color}')