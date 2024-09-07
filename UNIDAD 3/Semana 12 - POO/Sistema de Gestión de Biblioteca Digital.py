class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        libros = ", ".join([libro.titulo for libro in self.libros_prestados]) or "Ninguno"
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {libros}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN como clave, objeto Libro como valor
        self.usuarios = set()  # IDs de usuario únicos
        self.usuarios_objetos = {}  # ID de usuario como clave, objeto Usuario como valor

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.usuarios_objetos[usuario.id_usuario] = usuario

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_objetos[id_usuario]

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios_objetos[id_usuario]
            usuario.prestar_libro(libro)
            del self.libros[isbn]

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios_objetos[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    self.libros[isbn] = libro
                    usuario.devolver_libro(libro)
                    break

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if getattr(libro, criterio) == valor:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios_objetos[id_usuario]
            return usuario.libros_prestados
        return []

    def mostrar_estado(self):
        print("\n--- Estado actual de la biblioteca ---")
        if self.libros:
            print("\nLibros disponibles:")
            for libro in self.libros.values():
                print(libro)
        else:
            print("No hay libros disponibles.")

        if self.usuarios_objetos:
            print("\nUsuarios registrados:")
            for usuario in self.usuarios_objetos.values():
                print(usuario)
        else:
            print("No hay usuarios registrados.")

    def __str__(self):
        libros = ", ".join([str(libro) for libro in self.libros.values()])
        return f"Libros en biblioteca: {libros}"


def mostrar_menu():
    print("\n--- Menú Biblioteca ---")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Mostrar estado")
    print("10. Salir")
    return input("Selecciona una opción: ")


def main():
    biblioteca = Biblioteca()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)
            print("Libro añadido con éxito.")

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
            print("Libro quitado con éxito.")

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
            print("Usuario registrado con éxito.")

        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
            print("Usuario dado de baja con éxito.")

        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario que recibe el libro: ")
            biblioteca.prestar_libro(isbn, id_usuario)
            print("Libro prestado con éxito.")

        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario que devuelve el libro: ")
            biblioteca.devolver_libro(isbn, id_usuario)
            print("Libro devuelto con éxito.")

        elif opcion == "7":
            criterio = input("Criterio de búsqueda (titulo/autor/categoria): ")
            valor = input(f"Valor del criterio ({criterio}): ")
            resultados = biblioteca.buscar_libro(criterio, valor)
            if resultados:
                print("\n--- Libros encontrados ---")
                for libro in resultados:
                    print(libro)
            else:
                print(f"No se encontraron libros que coincidan con {criterio}: {valor}")

        elif opcion == "8":
            id_usuario = input("ID del usuario para listar libros prestados: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            if libros_prestados:
                print(f"\nLibros prestados a {id_usuario}:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print(f"No hay libros prestados para el usuario con ID {id_usuario}")

        elif opcion == "9":
            biblioteca.mostrar_estado()

        elif opcion == "10":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()

