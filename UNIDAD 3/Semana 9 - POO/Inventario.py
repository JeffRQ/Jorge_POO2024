class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre}: {self.cantidad} unidades, ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' añadido.")

    def eliminar(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                print(f"Producto con ID '{id}' eliminado.")
                return
        print(f"Producto con ID '{id}' no encontrado.")

    def actualizar(self, id, cantidad, precio):
        for producto in self.productos:
            if producto.id == id:
                producto.cantidad = cantidad
                producto.precio = precio
                print(f"Producto con ID '{id}' actualizado.")
                return
        print(f"Producto con ID '{id}' no encontrado.")

    def mostrar(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Productos en el inventario:")
            for producto in self.productos:
                print(producto)


def menu():
    inventario = Inventario()

    # Añadiendo productos predefinidos
    productos_predefinidos = [
        Producto("001", "Manzana", 50, 0.5),
        Producto("002", "Banana", 30, 0.3),
        Producto("003", "Naranja", 40, 0.4),
        Producto("004", "Pera", 20, 0.6),
        Producto("005", "Mango", 25, 1.0)
    ]

    for producto in productos_predefinidos:
        inventario.añadir(producto)

    # Operaciones
    print("Estado inicial del inventario:")
    inventario.mostrar()

    # Añadiendo un nuevo producto
    print("\nAñadiendo un nuevo producto:")
    inventario.añadir(Producto("006", "Kiwi", 15, 0.8))
    inventario.mostrar()

    # Actualizando un producto
    print("\nActualizando un producto:")
    inventario.actualizar("002", 35, 0.35)
    inventario.mostrar()

    # Eliminando un producto
    print("\nEliminando un producto:")
    inventario.eliminar("003")
    inventario.mostrar()

    print("\nSaliendo...")
    print("Fin de la operación.")


menu()
