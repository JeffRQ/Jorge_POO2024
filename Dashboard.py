import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
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
        '1': 'UNIDAD 1/Semana 2 - POO/Abstracción/Abstracción.py',
        '2': 'UNIDAD 1/Semana 2 - POO/Encapsulación/Encapsulación.py',
        '3': 'UNIDAD 1/Semana 2 - POO/Herencia/Herencia.py',
        '4': 'UNIDAD 1/Semana 2 - POO/Polimorfismo/Polimorfismo.py',
        '5': 'UNIDAD 1/Semana 2 - POO/abstracción_encapsulación_herencia_y_polimorfismo.py',
        '6': 'UNIDAD 1/Semana 3 - POO/temperatura/clima diario.py',
        '7': 'UNIDAD 1/Semana 3 - POO/temperatura/temperatura_funciones.py',
        '8': 'UNIDAD 1/Semana 4 - POO/Características de la Programación Orientada a Objetos/animal polimorfismo s4.py',
        '9': 'UNIDAD 1/Semana 4 - POO/Características de la Programación Orientada a Objetos/Banco encapsulación.py',
        '10': 'UNIDAD 1/Semana 4 - POO/Características de la Programación Orientada a Objetos/clase s4.py',
        '11': 'UNIDAD 1/Semana 4 - POO/Características de la Programación Orientada a Objetos/empleados herencia s4.py',
        '12': 'UNIDAD 2/Semana 5 - POO/Tipos de datos_identificadores/tipos de datos_identificadores.py',
        '13': 'UNIDAD 2/Semana 6 - POO/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '14': 'UNIDAD 2/Semana 7 - POO/Constructores y destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
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
