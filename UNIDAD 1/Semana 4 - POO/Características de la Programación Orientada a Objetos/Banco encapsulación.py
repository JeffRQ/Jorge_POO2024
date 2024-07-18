class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.__saldo


# Crear un objeto de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("Jorge Ramírez",1000)
mi_cuenta.depositar(500)
print(mi_cuenta.obtener_saldo())
mi_cuenta.retirar(300)
print(mi_cuenta.obtener_saldo())
