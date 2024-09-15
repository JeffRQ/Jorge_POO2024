import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre}: {self.cantidad} unidades, ${self.precio:.2f}"

    def to_file_format(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

    @classmethod
    def from_file_format(cls, file_line):
        id, nombre, cantidad, precio = file_line.strip().split(',')
        return cls(id, nombre, int(cantidad), float(precio))


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for line in file:
                        producto = Producto.from_file_format(line)
                        self.productos.append(producto)
                print(f"Inventario cargado desde '{self.archivo}'.")
            except FileNotFoundError:
                print(f"Archivo '{self.archivo}' no encontrado.")
            except PermissionError:
                print(f"Permiso denegado al intentar leer '{self.archivo}'.")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
        else:
            print(f"El archivo '{self.archivo}' no existe, se creará al guardar.")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(producto.to_file_format())
            print(f"Inventario guardado en '{self.archivo}'.")
        except PermissionError:
            print(f"Permiso denegado al intentar escribir en '{self.archivo}'.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al guardar: {e}")

    def añadir(self, producto):
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(f"Producto '{producto.nombre}' añadido.")

    def eliminar(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print(f"Producto con ID '{id}' eliminado.")
                return
        print(f"Producto con ID '{id}' no encontrado.")

    def actualizar(self, id, cantidad, precio):
        for producto in self.productos:
            if producto.id == id:
                producto.cantidad = cantidad
                producto.precio = precio
                self.guardar_en_archivo()
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

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Mostrar inventario")
        print("2. Añadir producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.mostrar()
        elif opcion == "2":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            inventario.añadir(Producto(id, nombre, cantidad, precio))
        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            precio = float(input("Ingrese el nuevo precio: "))
            inventario.actualizar(id, cantidad, precio)
        elif opcion == "4":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar(id)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

    print("Fin de la operación.")


menu()