class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"{self.marca} {self.modelo} del año {self.año}"


# Crear un objeto de la clase Vehiculo
mi_coche = Vehiculo("Toyota", "Corolla", 2020)
print(mi_coche.descripcion())
