#EjemploEncapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulamos el nombre
        self.__edad = edad      # Encapsulamos la edad

    def obtener_nombre(self):
        """Devuelve el nombre de la persona."""
        return self.__nombre

    def establecer_edad(self, nueva_edad):
        """Establece la edad de la persona, con validación."""
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")

    def obtener_edad(self):
        """Devuelve la edad de la persona."""
        return self.__edad

# Uso del encapsulamiento
persona = Persona("Juan", 25)
print(f"Nombre: {persona.obtener_nombre()}, Edad: {persona.obtener_edad()}")

# Intentamos establecer una edad negativa (lo cual no se permitirá)
persona.establecer_edad(-5)

# Establecemos una nueva edad
persona.establecer_edad(30)

# Mostramos la información actualizada
print(f"Nombre: {persona.obtener_nombre()}, Edad: {persona.obtener_edad()}")