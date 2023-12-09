#EjemploPolimorfismo
class Forma:
    def area(self):
        """Método para calcular el área (debe ser implementado por las subclases)."""
        pass

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        """Calcula el área del cuadrado."""
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        """Calcula el área del círculo."""
        return 3.14 * self.radio ** 2

# Uso del polimorfismo
formas = [Cuadrado(5), Circulo(3)]
for forma in formas:
    print(f'Área: {forma.area()}')