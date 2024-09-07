class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Constructor que inicializa los atributos del libro: título, autor, categoría e ISBN.
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        # Devuelve una representación en formato cadena del libro.
        return f"{self.titulo} por {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        # Constructor que inicializa los atributos del usuario: nombre e ID.
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar los libros prestados al usuario.
        self.libros_prestados = []

    def prestar_libro(self, libro):
        # Agrega el libro a la lista de libros prestados del usuario.
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        # Si el libro está en la lista de libros prestados, lo quita.
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        # Devuelve una representación en formato cadena del usuario, incluyendo los libros prestados.
        libros = ", ".join([libro.titulo for libro in self.libros_prestados]) or "Ninguno"
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {libros}"


class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar los libros disponibles en la biblioteca, usando el ISBN como clave.
        self.libros = {}
        # Conjunto para almacenar los ID de los usuarios registrados, garantizando que sean únicos.
        self.usuarios = set()
        # Diccionario que almacena objetos Usuario, con el ID del usuario como clave.
        self.usuarios_objetos = {}

    def añadir_libro(self, libro):
        # Añade el libro a la colección de libros de la biblioteca.
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        # Elimina el libro de la colección de libros disponibles, si existe.
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        # Registra un nuevo usuario si su ID no está en el conjunto de usuarios.
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.usuarios_objetos[usuario.id_usuario] = usuario

    def dar_baja_usuario(self, id_usuario):
        # Elimina al usuario si su ID está registrado en la biblioteca.
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_objetos[id_usuario]

    def prestar_libro(self, isbn, id_usuario):
        # Presta un libro a un usuario si el libro está disponible y el usuario está registrado.
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios_objetos[id_usuario]
            usuario.prestar_libro(libro)  # El usuario toma el libro prestado.
            del self.libros[isbn]  # El libro se elimina de la lista de disponibles.

    def devolver_libro(self, isbn, id_usuario):
        # El usuario devuelve un libro. El libro se vuelve a agregar a la lista de disponibles.
        if id_usuario in self.usuarios:
            usuario = self.usuarios_objetos[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    self.libros[isbn] = libro  # El libro vuelve a estar disponible.
                    usuario.devolver_libro(libro)  # Se elimina de los libros prestados del usuario.
                    break

    def buscar_libro(self, criterio, valor):
        # Busca libros que coincidan con un criterio (título, autor o categoría).
        resultados = []
        for libro in self.libros.values():
            if getattr(libro, criterio) == valor:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        # Devuelve la lista de libros prestados de un usuario dado su ID.
        if id_usuario in self.usuarios:
            usuario = self.usuarios_objetos[id_usuario]
            return usuario.libros_prestados
        return []

    def mostrar_estado(self):
        # Muestra el estado actual de la biblioteca, incluyendo libros disponibles y usuarios registrados.
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
        # Devuelve una representación en cadena de los libros disponibles en la biblioteca.
        libros = ", ".join([str(libro) for libro in self.libros.values()])
        return f"Libros en biblioteca: {libros}"


def mostrar_menu():
    # Imprime el menú de opciones y devuelve la opción seleccionada por el usuario.
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
    # Función principal que ejecuta el sistema de biblioteca.
    biblioteca = Biblioteca()

    while True:
        # Bucle principal del programa, que muestra el menú y ejecuta las acciones correspondientes.
        opcion = mostrar_menu()

        if opcion == "1":
            # Añadir un libro a la biblioteca.
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)
            print("Libro añadido con éxito.")

        elif opcion == "2":
            # Quitar un libro de la biblioteca.
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
            print("Libro quitado con éxito.")

        elif opcion == "3":
            # Registrar un nuevo usuario en la biblioteca.
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
            print("Usuario registrado con éxito.")

        elif opcion == "4":
            # Dar de baja a un usuario de la biblioteca.
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
            print("Usuario dado de baja con éxito.")

        elif opcion == "5":
            # Prestar un libro a un usuario.
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario que recibe el libro: ")
            biblioteca.prestar_libro(isbn, id_usuario)
            print("Libro prestado con éxito.")

        elif opcion == "6":
            # Devolver un libro prestado por un usuario.
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario que devuelve el libro: ")
            biblioteca.devolver_libro(isbn, id_usuario)
            print("Libro devuelto con éxito.")

        elif opcion == "7":
            # Buscar un libro en la biblioteca según un criterio dado (título, autor, categoría).
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
            # Listar los libros prestados a un usuario dado su ID.
            id_usuario = input("ID del usuario para listar libros prestados: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            if libros_prestados:
                print(f"\nLibros prestados a {id_usuario}:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print(f"No hay libros prestados para el usuario con ID {id_usuario}")

        elif opcion == "9":
            # Mostrar el estado actual de la biblioteca (libros disponibles y usuarios registrados).
            biblioteca.mostrar_estado()

        elif opcion == "10":
            # Salir del programa.
            print("Saliendo del programa.")
            break

        else:
            # Opción inválida ingresada por el usuario.
            print("Opción inválida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()
    # Punto de entrada del programa.
