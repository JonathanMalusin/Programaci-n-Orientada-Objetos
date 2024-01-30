class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}")

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta exitosa. {cantidad} unidades de {self.nombre} vendidas.")
        else:
            print(f"No hay suficiente stock de {self.nombre} para realizar la venta.")

class Cliente:
    def __init__(self, nombre, dinero_disponible):
        self.nombre = nombre
        self.dinero_disponible = dinero_disponible

    def comprar_producto(self, producto, cantidad):
        costo_total = producto.precio * cantidad
        if costo_total <= self.dinero_disponible:
            producto.vender(cantidad)
            self.dinero_disponible -= costo_total
            print(f"Compra exitosa. {cantidad} unidades de {producto.nombre} compradas.")
        else:
            print("No tienes suficiente dinero para realizar la compra.")

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la tienda.")

    def mostrar_catalogo(self):
        print(f"Catálogo de la tienda '{self.nombre}':")
        for producto in self.productos:
            producto.mostrar_informacion()


# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    laptop = Producto("Laptop", 1000, 10)
    smartphone = Producto("Smartphone", 500, 20)

    # Crear tienda
    mi_tienda = Tienda("Super Paco")

    # Agregar productos a la tienda
    mi_tienda.agregar_producto(laptop)
    mi_tienda.agregar_producto(smartphone)

    # Mostrar catálogo de la tienda
    mi_tienda.mostrar_catalogo()

    # Crear cliente
    cliente1 = Cliente("Jhon", 2500)

    # Realizar compras
    cliente1.comprar_producto(laptop, 2)
    cliente1.comprar_producto(smartphone, 3)

    # Mostrar catálogo de la tienda después de las compras
    mi_tienda.mostrar_catalogo()
