# Leer cantidad de números
N = int(input())

# Inicializar suma de pares
suma_pares = 0

# Procesar cada número
for _ in range(N):
    x = int(input())
    if x % 2 == 0:
        suma_pares += x
# Imprimir resultado
print(suma_pares)