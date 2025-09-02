# Leer cantidad de números
N = int(input())

# Si N no es positivo, promedio cero
if N <= 0:
    print(0)
else:
    suma_cuad = 0
    # Leer números y acumular sus cuadrados
    for _ in range(N):
        x = int(input())
        suma_cuad += x * x
    # Calcular promedio de los cuadrados
    promedio = suma_cuad / N
    print(promedio)