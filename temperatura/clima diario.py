class RegistroDiario:


  def __init__(self, dia):
    self.dia = dia
    self.temperatura = None

  def ingresar_temperatura(self):
    """
    Solicita al usuario la temperatura del día.
    """
    self.temperatura = float(input(f"Ingrese la temperatura del {self.dia}: "))

  def obtener_temperatura(self):
    """
    Retorna el valor de la temperatura.
    """
    return self.temperatura

# Programa principal

# Lista para almacenar registros diarios
registros_semanales = []

# Creación de objetos RegistroDiario para cada día
for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
  registro_diario = RegistroDiario(dia)
  registro_diario.ingresar_temperatura()
  registros_semanales.append(registro_diario)

# Cálculo y presentación del promedio semanal
promedio_semanal = sum(registro.obtener_temperatura() for registro in registros_semanales) / len(registros_semanales)
print(f"El promedio semanal de temperaturas es de: {promedio_semanal:.2f}°C")
