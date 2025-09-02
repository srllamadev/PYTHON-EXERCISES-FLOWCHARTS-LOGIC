# Leer cantidad de números
N = int(input())

if N <= 0:
    # Sin datos, mostrar 0 en cada resultado
    print(0)
    print(0)
    print(0)
    print(0)
else:
    # Leer primer número para inicializar
    first = int(input())
    max_val = first
    min_val = first
    total = first
    # Procesar el resto de números
    for _ in range(N - 1):
        x = int(input())
        total += x
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x
    # Calcular rango
    rango = max_val - min_val
    # Imprimir resultados
    print(max_val)
    print(min_val)
    print(rango)
    print(total)