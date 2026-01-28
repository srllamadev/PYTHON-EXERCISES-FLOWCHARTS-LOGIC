import math

# Leer número de estudiantes
N = int(input())

# Si no hay datos, desviación cero
if N <= 0:
    print(0.0)
else:
    # Leer todas las notas
    notas = [float(input()) for _ in range(N)]
    # Calcular media
    media = sum(notas) / N
    # Calcular varianza poblacional
    varianza = sum((x - media) ** 2 for x in notas) / N
    # Desviación estándar
    desviacion = math.sqrt(varianza)
    # Imprimir resultado
    print(round(desviacion,2))