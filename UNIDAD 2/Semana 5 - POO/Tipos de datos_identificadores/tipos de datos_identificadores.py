# Programa: Calculadora de Área de Triángulo
# Descripción: Este programa calcula el área de un triángulo dados la base y la altura.

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Args:
        base (float): La base del triángulo.
        altura (float): La altura del triángulo.

    Returns:
        float: El área calculada del triángulo.
    """
    area = (base * altura) / 2
    return area

if __name__ == "__main__":
    # Solicitar al usuario la base y la altura del triángulo
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    # Calcular el área del triángulo
    area_triangulo = calcular_area_triangulo(base, altura)

    # Mostrar el resultado
    print(f"El área del triángulo con base {base} y altura {altura} es: {area_triangulo}")