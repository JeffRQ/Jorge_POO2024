# Definición de funciones

def ingresar_temperatura(dia):
  """
  Función para ingresar la temperatura de un día específico.

  Parámetros:
    dia (str): Nombre del día de la semana.

  Retorno:
    float: Valor de la temperatura ingresada.
  """
  temperatura = float(input(f"Ingrese la temperatura del {dia}: "))
  return temperatura

def calcular_promedio_semanal(temperaturas):
  """
  Función para calcular el promedio semanal de temperaturas.

  Parámetros:
    temperaturas (list): Lista con las temperaturas de cada día.

  Retorno:
    float: Promedio semanal de temperaturas.
  """
  promedio = sum(temperaturas) / len(temperaturas)
  return promedio

# Programa principal

# Inicialización de lista vacía para almacenar temperaturas diarias
temperaturas_semanales = []

# Ingreso de temperaturas diarias
for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
  temperatura_dia = ingresar_temperatura(dia)
  temperaturas_semanales.append(temperatura_dia)

# Cálculo y presentación del promedio semanal
promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)
print(f"El promedio semanal de temperaturas es de: {promedio_semanal:.2f}°C")
