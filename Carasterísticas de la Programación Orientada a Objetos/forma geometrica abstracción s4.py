from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass


class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2


class Rectangulo(FormaGeometrica):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho


# Crear objetos de las clases Circulo y Rectangulo
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
print(f"Área del círculo: {circulo.area()}")
print(f"Área del rectángulo: {rectangulo.area()}")
