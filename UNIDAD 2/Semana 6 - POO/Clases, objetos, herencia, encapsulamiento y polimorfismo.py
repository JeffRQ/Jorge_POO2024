class Cliente:
    """
    Clase base para representar a un cliente de la tienda online.

    Atributos:
        nombre (str): Nombre del cliente.
        apellido (str): Apellido del cliente.
        correo_electronico (str): Correo electrónico del cliente.

    Métodos:
        obtener_informacion(self):
            Muestra la información del cliente.
    """
    print("<<<<<<<<<<<<<<< USUARIO GENERAL >>>>>>>>>>>>>>>")
    def __init__(self, nombre, apellido, correo_electronico):
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico

    def obtener_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Correo electrónico: {self.correo_electronico}")


class ClienteVIP(Cliente):
    """
    Clase derivada para representar a un cliente VIP de la tienda online.

    Atributos heredados:
        nombre (str): Nombre del cliente.
        apellido (str): Apellido del cliente.
        correo_electronico (str): Correo electrónico del cliente.

    Atributos adicionales:
        puntos_acumulados (int): Puntos de fidelidad acumulados.
        nivel_vip (str): Nivel de VIP del cliente (Bronce, Plata, Oro).

    Métodos heredados:
        obtener_informacion(self):
            Muestra la información del cliente, incluyendo los puntos VIP y el nivel.

    Métodos adicionales:
        obtener_descuento(self, monto_compra):
            Calcula y aplica el descuento correspondiente al nivel VIP del cliente.
    """

    def __init__(self, nombre, apellido, correo_electronico, puntos_acumulados, nivel_vip):
        super().__init__(nombre, apellido, correo_electronico)
        self.__puntos_acumulados = puntos_acumulados
        self.__nivel_vip = nivel_vip

    def obtener_informacion(self):
        print("<<<<<<<<<<<<<<< USUARIO PREMIUM >>>>>>>>>>>>>>>")
        super().obtener_informacion()
        print(f"Puntos VIP: {self.__puntos_acumulados}")
        print(f"Nivel VIP: {self.__nivel_vip}")

    def obtener_descuento(self, monto_compra):
        if self.__nivel_vip == "Bronce":
            descuento = monto_compra * 0.05
        elif self.__nivel_vip == "Plata":
            descuento = monto_compra * 0.1
        elif self.__nivel_vip == "Oro":
            descuento = monto_compra * 0.15
        else:
            descuento = 0

        monto_final = monto_compra - descuento
        print(f"Descuento aplicado: {descuento}")
        print(f"Monto final a pagar: {monto_final}")

# Ejemplo de uso

cliente1 = Cliente("Jorge", "Ramírez", "jj.ramirezq@uea.edu.ec")
cliente1.obtener_informacion()

clienteVIP1 = ClienteVIP("Jefferson", "Ramírez", "jefframirezq@gmail.com", 100, "Plata")
clienteVIP1.obtener_informacion()
clienteVIP1.obtener_descuento(500)
