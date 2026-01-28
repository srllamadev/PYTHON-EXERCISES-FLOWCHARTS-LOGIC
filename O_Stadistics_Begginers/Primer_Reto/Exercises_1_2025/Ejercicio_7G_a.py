# Leer cantidad de edades
N = int(input())

if N <= 0:
    # Sin datos, varianza cero
    print(0.0)
else:
    # Leer edades y almacenar
    edades = [float(input()) for _ in range(N)]
    # Calcular media
    media = sum(edades) / N
    # Calcular varianza poblacional
    varianza = sum((e - media) ** 2 for e in edades) / N
    # Imprimir resultado
    print(round(varianza,2))