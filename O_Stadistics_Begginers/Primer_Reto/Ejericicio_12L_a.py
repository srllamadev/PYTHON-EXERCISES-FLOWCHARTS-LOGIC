# Leer cantidad de números
N = int(input())

# Inicializar conteno de numeros pares
cont = 0

# Procesar cada número
for _ in range(N):
    x = int(input())
    if x % 2 == 0:
        cont += 1
# Imprimir resultado
print(cont)