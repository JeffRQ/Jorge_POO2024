class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self._nombre = nombre
        self._fuerza = fuerza
        self._inteligencia = inteligencia
        self._defensa = defensa
        self._vida = vida

    def nombre(self):
        return self._nombre

    def fuerza(self):
        return self._fuerza

    def inteligencia(self):
        return self._inteligencia

    def defensa(self):
        return self._defensa

    def vida(self):
        return self._vida


    def calcular_danio(self, enemigo):
        pass


    def atacar(self, enemigo):
        pass

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self._fuerza += fuerza
        self._inteligencia += inteligencia
        self._defensa += defensa

    def esta_vivo(self):
        return self._vida > 0

    def morir(self):
        self._vida = 0
        print(self.nombre, "ha muerto")

    def _calcular_danio(self, enemigo):
        return self._fuerza - enemigo.defensa

    def _atacar(self, enemigo):
        danio = self._calcular_danio(enemigo)
        enemigo._vida -= danio
        print(self.nombre, "ha realizado", danio, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._espada = espada

    @property
    def espada(self):
        return self._espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self._espada = 8
        elif opcion == 2:
            self._espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def calcular_danio(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

    def atacar(self, enemigo):
        self._atacar(enemigo)

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._libro = libro

    @property
    def libro(self):
        return self._libro

    def calcular_danio(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

    def atacar(self, enemigo):
        self._atacar(enemigo)

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

def combatir(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de", jugador_1.nombre, ":")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de", jugador_2.nombre, ":")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combatir(personaje_1, personaje_2)
