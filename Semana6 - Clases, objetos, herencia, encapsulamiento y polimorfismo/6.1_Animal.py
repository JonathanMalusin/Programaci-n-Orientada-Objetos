class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación

    def get_nombre(self):
        return self.__nombre

    def hacer_sonido(self):
        pass  # Método que será sobrescrito en las clases derivadas


# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza  # Encapsulación

    def get_raza(self):
        return self.__raza

    def hacer_sonido(self):  # Polimorfismo: método sobrescrito
        return "Wou!"

# Otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.__color = color  # Encapsulación

    def get_color(self):
        return self.__color

    def hacer_sonido(self):  # Polimorfismo: método sobrescrito
        return "Miau!"

# Crear instancias
if __name__ == "__main__":
    perro1 = Perro("Firulais", "Labrador")
    gato1 = Gato("Pepinillo", "Amarillo")

    print(f"{perro1.get_nombre()} es un {perro1.get_raza()} que dice: {perro1.hacer_sonido()}")
    print(f"{gato1.get_nombre()} es de color {gato1.get_color()} y dice: {gato1.hacer_sonido()}")