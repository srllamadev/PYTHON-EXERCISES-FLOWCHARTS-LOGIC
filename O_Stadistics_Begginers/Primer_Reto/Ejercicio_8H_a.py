# Leer cantidad de números
N = int(input())

# Si no hay datos, imprimir 0
if N <= 0:
    print(0)
else:
    # Inicializar mínimo con el primer valor
    mn = int(input())
    # Procesar el resto de números
    for _ in range(N - 1):
        x = int(input())
        if x < mn:
            mn = x
    # Imprimir el número mínimo
    print(mn)