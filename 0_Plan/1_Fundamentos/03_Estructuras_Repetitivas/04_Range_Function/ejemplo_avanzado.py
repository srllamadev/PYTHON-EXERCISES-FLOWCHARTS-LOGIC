"""
RANGE FUNCTION - Ejemplos Avanzados
====================================
Patrones complejos y aplicaciones prácticas de range()
"""

# Ejemplo 1: Range con enumerate
print("=== Ejemplo 1: Combinar range() y enumerate() ===")
nombres = ["Ana", "Luis", "María", "Carlos"]

print("Opción 1 - Con range:")
for i in range(len(nombres)):
    print(f"{i+1}. {nombres[i]}")

print("\nOpción 2 - Con enumerate (más Pythónico):")
for i, nombre in enumerate(nombres, start=1):
    print(f"{i}. {nombre}")

print()

# Ejemplo 2: Matriz con range anidados
print("=== Ejemplo 2: Generar Matriz ===")
filas = 3
columnas = 4

print(f"Matriz {filas}×{columnas}:")
for i in range(filas):
    for j in range(columnas):
        valor = i * columnas + j + 1
        print(f"{valor:3d}", end=" ")
    print()  # Nueva línea después de cada fila

print()

# Ejemplo 3: Progresión aritmética
print("=== Ejemplo 3: Progresión Aritmética ===")
# Generar: 5, 12, 19, 26, 33, 40
inicio = 5
salto = 7
cantidad = 6

print(f"Progresión: inicio={inicio}, salto={salto}, términos={cantidad}")
for i in range(cantidad):
    termino = inicio + (i * salto)
    print(f"a[{i}] = {termino}", end="  ")
print("\n")

# Con range directamente
print("Usando range directamente:")
progresion = list(range(inicio, inicio + cantidad * salto, salto))
print(progresion)

print()

# Ejemplo 4: Pirámide de números
print("=== Ejemplo 4: Pirámide de Números ===")
altura = 5
for i in range(1, altura + 1):
    # Espacios
    print(" " * (altura - i), end="")
    # Números ascendentes
    for j in range(1, i + 1):
        print(j, end="")
    # Números descendentes
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print()

# Ejemplo 5: Slice simulation con range
print("=== Ejemplo 5: Simular Slicing con Range ===")
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f"Lista original: {lista}")
print("\nObtener elementos de índice 2 a 7:")
print(f"  Slice [2:8]: {lista[2:8]}")

print(f"  Con range: ", end="")
sublista = []
for i in range(2, 8):
    sublista.append(lista[i])
print(sublista)

print()

# Ejemplo 6: Fibonacci con range
print("=== Ejemplo 6: Serie Fibonacci ===")
n = 15
a, b = 0, 1
fibonacci = [a, b]

for _ in range(n - 2):
    a, b = b, a + b
    fibonacci.append(b)

print(f"Primeros {n} números de Fibonacci:")
print(fibonacci)

print()

# Ejemplo 7: Tabla de multiplicar completa
print("=== Ejemplo 7: Tabla de Multiplicar (1-10) ===")
print("    ", end="")
for i in range(1, 11):
    print(f"{i:4d}", end="")
print("\n" + "-" * 48)

for i in range(1, 11):
    print(f"{i:2d} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4d}", end="")
    print()

print()

# Ejemplo 8: Números primos con range
print("=== Ejemplo 8: Números Primos hasta 50 ===")
primos = []

for num in range(2, 51):
    es_primo = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)

print(f"Primos: {primos}")
print(f"Total: {len(primos)} números primos")

print()

# Ejemplo 9: Cronómetro regresivo
print("=== Ejemplo 9: Cronómetro Visual ===")
import time

print("Cuenta regresiva de 5 segundos:")
for segundos in range(5, 0, -1):
    print(f"⏰ {segundos}...", end=" ", flush=True)
    time.sleep(1)
print("¡Tiempo!")

print()

# Ejemplo 10: Generar contraseñas numéricas
print("=== Ejemplo 10: Generar PINs de 4 Dígitos ===")
import random

pins_generados = []
for _ in range(5):
    pin = ""
    for _ in range(4):
        pin += str(random.randint(0, 9))
    pins_generados.append(pin)

print("5 PINs aleatorios generados:")
for i, pin in enumerate(pins_generados, 1):
    print(f"  {i}. {pin}")

print()

# Ejemplo 11: Multiplicación de matrices (simplificado)
print("=== Ejemplo 11: Producto Punto de Vectores ===")
vector_a = [1, 2, 3, 4, 5]
vector_b = [2, 3, 4, 5, 6]

producto_punto = 0
for i in range(len(vector_a)):
    producto_punto += vector_a[i] * vector_b[i]

print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}")
print(f"Producto punto: {producto_punto}")

print()

# Ejemplo 12: Calendario simplificado
print("=== Ejemplo 12: Mes (30 días) ===")
print("Lun Mar Mie Jue Vie Sab Dom")
print("-" * 28)

dia_inicio = 3  # El mes empieza en miércoles (0=Lun, ..., 6=Dom)
# Espacios iniciales
print("    " * dia_inicio, end="")

for dia in range(1, 31):
    print(f"{dia:3d} ", end="")
    if (dia + dia_inicio) % 7 == 0:
        print()  # Nueva semana

print("\n")

# Ejemplo 13: ASCII Art con range
print("=== Ejemplo 13: Triángulo de Asteriscos ===")
altura = 7
for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

print()

# Ejemplo 14: Sumatorias matemáticas
print("=== Ejemplo 14: Sumatorias ===")

# Suma de cuadrados: Σ(i²) de 1 a n
n = 10
suma_cuadrados = sum(i**2 for i in range(1, n + 1))
print(f"Σ(i²) de 1 a {n} = {suma_cuadrados}")

# Suma de cubos
suma_cubos = sum(i**3 for i in range(1, n + 1))
print(f"Σ(i³) de 1 a {n} = {suma_cubos}")

# Suma alterna
suma_alterna = sum((-1)**i * i for i in range(1, n + 1))
print(f"Σ((-1)^i × i) de 1 a {n} = {suma_alterna}")

print()

# Ejemplo 15: Patrones complejos
print("=== Ejemplo 15: Patrón Diamante ===")
n = 5

# Parte superior
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Parte inferior
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

print()

# Ejemplo 16: Análisis de rendimiento
print("=== Ejemplo 16: Eficiencia de Range ===")
import sys

# Lista vs Range
lista_grande = list(range(1000000))
range_grande = range(1000000)

print(f"Tamaño de list(range(1000000)): {sys.getsizeof(lista_grande):,} bytes")
print(f"Tamaño de range(1000000): {sys.getsizeof(range_grande):,} bytes")
print(f"Range es {sys.getsizeof(lista_grande) // sys.getsizeof(range_grande)}× más eficiente en memoria")
