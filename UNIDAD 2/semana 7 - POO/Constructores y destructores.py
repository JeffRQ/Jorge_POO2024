class Moto:
    def __init__(self, nombre, velocidad_maxima):
        """
        Constructor que inicializa el objeto Moto.
        Establece el nombre de la moto y su velocidad máxima.
        """
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        print(f'Moto {nombre} creada con una velocidad máxima de {velocidad_maxima} km/h.')

    def acelerar(self, incremento):
        """
        Aumenta la velocidad actual de la moto.
        """
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
        else:
            self.velocidad_actual = self.velocidad_maxima
        print(f'{self.nombre} aceleró a {self.velocidad_actual} km/h.')

    def frenar(self, decremento):
        """
        Disminuye la velocidad actual de la moto.
        """
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            self.velocidad_actual = 0
        print(f'{self.nombre} frenó a {self.velocidad_actual} km/h.')

    def __del__(self):
        """
        Destructor que indica cuándo una moto es destruida.
        """
        print(f'Moto {self.nombre} destruida.')

# Ejemplo de uso de la clase Moto en una carrera

# Crear instancias de motos
moto1 = Moto('Yamaha R1', 300)
moto2 = Moto('Ducati Panigale', 320)

# Simular la carrera
moto1.acelerar(100)
moto2.acelerar(120)
moto1.acelerar(150)
moto2.acelerar(200)
moto1.frenar(50)
moto2.frenar(100)

# Eliminar las motos explícitamente (invocará a __del__)
del moto1
del moto2

# No es necesario eliminar las motos explícitamente,
# el recolector de basura lo hará automáticamente cuando ya no se usen.

