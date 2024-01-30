import os
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        #Archivos Semana 1
        '1': 'Semana1 - Fundamentos de la Programación orientada a objetos - POO/1.1_EjemploTecnicasProgramacion.py',
        #Archivos Semana 2
        '2': 'Semana2 - Desarrollo de Ejemplos de Técnicas de Programación/2_EjemplosPracticos_Abstracción.py',
        '2.1': 'Semana2 - Desarrollo de Ejemplos de Técnicas de Programación/2.1_EjemplosPracticos_Encapsulamiento.py',
        '2.2': 'Semana2 - Desarrollo de Ejemplos de Técnicas de Programación/2.2_EjemplosPracticos_Herencia.py',
        '2.3': 'Semana2 - Desarrollo de Ejemplos de Técnicas de Programación/2.3_EjemplosPracticos_Polimorfismo.py',
        #Archivos Semana 3
        '3': 'Semana3 - Programación Tradicional y POO/3_Programación Orientada a Objetos (POO).py',
        '3.1': 'Semana3 - Programación Tradicional y POO/3.1_Programación Tradicional.py',
        #Archivos Semana 4
        '4': 'Semana4 - Carasterísticas de la Programación Orientada a Objetos/4.1_Tienda.py',
        #Archivos Semana 5
        '5': 'Semana5 - Tipos de datos, Identificadores/5.1_AreaRectangulo.py',
        #Archivos Semana 6
        '6': 'Semana6 - Clases, objetos, herencia, encapsulamiento y polimorfismo/6.1_Animal.py',
        #Archivos Semana 7
        '7': 'Semana7 - Constructores y Destructores/7.1_Televisor.py',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
