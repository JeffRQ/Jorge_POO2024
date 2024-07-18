class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Crear objetos de las clases Perro y Gato
animales = [Perro(), Gato()]
for animal in animales:
    print(animal.hacer_sonido())

