class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados al usuario

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios únicos

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.id_usuario)

    def dar_de_baja_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario.id_usuario)

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[isbn]

    def devolver_libro(self, usuario, isbn):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                self.libros_disponibles[isbn] = libro
                usuario.libros_prestados.remove(libro)
                break

    def buscar_libros_por_titulo(self, titulo):
        return [libro for libro in self.libros_disponibles.values() if libro.titulo.lower() == titulo.lower()]

    def buscar_libros_por_autor(self, autor):
        return [libro for libro in self.libros_disponibles.values() if libro.autor.lower() == autor.lower()]

    def buscar_libros_por_categoria(self, categoria):
        return [libro for libro in self.libros_disponibles.values() if libro.categoria.lower() == categoria.lower()]

    def listar_libros_prestados(self, usuario):
        return usuario.libros_prestados

# Ejemplo de uso:
if __name__ == "__main__":
    mi_biblioteca = Biblioteca()

    libro1 = Libro("Sangre de Campeon", ("Carlos Cautemoc Sanchez"), "Motivación", "1780307474728")
    libro2 = Libro("El principito", ("Antoine", "de Saint-Exupéry"), "Infantil", "9780156012195")

    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)

    usuario1 = Usuario("Julio", "001")
    mi_biblioteca.registrar_usuario(usuario1)

    mi_biblioteca.prestar_libro(usuario1, "1780307474728")

    print("Libros prestados a", usuario1.nombre + ":")
    for libro in mi_biblioteca.listar_libros_prestados(usuario1):
        print(f"- {libro.titulo} ({libro.autor[0]})")
        #
