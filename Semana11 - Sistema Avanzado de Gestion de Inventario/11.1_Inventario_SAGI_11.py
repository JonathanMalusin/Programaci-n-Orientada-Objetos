import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def obtener_datos(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def agregar_producto(self, producto):
        if not any(p.get_id() == producto.get_id() for p in self.productos):
            self.productos.append(producto)
            print("Producto agregado correctamente.")
        else:
            print("Error: ID duplicado. El producto no fue agregado.")

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id, nuevo_nombre=None, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if nuevo_nombre is not None:
                    p.set_nombre(nuevo_nombre)
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        print("Inventario:")
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                data = json.load(file)
                return [Producto(**producto) for producto in data]
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo al agregar productos.")
            return []
        except PermissionError:
            print(f"No se tiene permiso para acceder al archivo {self.archivo}. Verifica los permisos.")
            return []

    def guardar_inventario(self):
        with open(self.archivo, 'w') as file:
            data = [producto.obtener_datos() for producto in self.productos]
            json.dump(data, file, indent=2)

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Inventario")
        print("6. Salir")

        try: #Excepcion
            opcion = input("Seleccione una opción (1-6): ")

            if opcion == "1":
                id = input("Ingrese ID del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad del producto: "))
                precio = float(input("Ingrese precio del producto: "))
                nuevo_producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
                inventario.guardar_inventario()

            elif opcion == "2":
                id = input("Ingrese ID del producto a eliminar: ")
                inventario.eliminar_producto(id)
                inventario.guardar_inventario()

            elif opcion == "3":
                id = input("Ingrese ID del producto a actualizar: ")
                nuevo_nombre = input("Ingrese nuevo nombre (deje en blanco para no cambiar): ")
                cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
                precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
                inventario.actualizar_producto(id, nuevo_nombre, int(cantidad) if cantidad else None, float(precio) if precio else None)
                inventario.guardar_inventario()

            elif opcion == "4":
                nombre = input("Ingrese nombre del producto a buscar: ")
                resultados = inventario.buscar_producto_por_nombre(nombre)
                if resultados:
                    print("Resultados de la búsqueda:")
                    for p in resultados:
                        print(
                            f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
                else:
                    print("No se encontraron productos con ese nombre.")

            elif opcion == "5":
                inventario.mostrar_inventario()

            elif opcion == "6":
                print("Saliendo del programa.")
                inventario.guardar_inventario()
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except KeyboardInterrupt:
            print("\nEl Programa ha sido detenido exitosamente.")
            inventario.guardar_inventario()
            break

if __name__ == "__main__":
    menu()
