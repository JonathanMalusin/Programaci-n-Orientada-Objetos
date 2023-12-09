#EjemploAbstraccion
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_info(self):
        """Devuelve la información del libro."""
        return f'Título: {self.titulo}, Autor: {self.autor}'

# Uso de la abstracción
libro1 = Libro("Sangre de Campeón", "Carlos Cauhtémoc Sánchez")
print(libro1.obtener_info())