# Programa para calcular el área de un rectángulo

def calcular_area_rectangulo(base, altura):

    area = base * altura
    return area

def main():
    # Solicitamos al usuario que ingrese la base y la altura.
    base_str = input("Ingrese la longitud de la base del rectángulo: ")
    altura_str = input("Ingrese la altura del rectángulo: ")

    # Convertir las entradas a tipos de datos adecuados (float)
    base = float(base_str)
    altura = float(altura_str)

    # Calculamos el área utilizando la función definida anteriormente
    area_rectangulo = calcular_area_rectangulo(base, altura)

    # Mostramos el resultado al usuario
    print(f"El área del rectángulo con base {base} y altura {altura} es: {area_rectangulo}")

    # Uso de un tipo de dato booleano
    es_cuadrado = base == altura
    print(f"¿Es un cuadrado? {es_cuadrado}")

if __name__ == "__main__":
    # Llamamos a la función principal
    main()