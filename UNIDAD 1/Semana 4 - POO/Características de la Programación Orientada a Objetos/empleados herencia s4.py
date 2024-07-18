class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_detalles(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_detalles(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}"


# Crear objetos de las clases Empleado y Gerente
empleado1 = Empleado("Shirley Ramírez",3000)
gerente1 = Gerente("Genesis Zambrano",5000,"ventas")
print(empleado1.mostrar_detalles())
print(gerente1.mostrar_detalles())

