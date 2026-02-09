"""
RANGE FUNCTION - Ejemplos Básicos
==================================
Usos fundamentales de la función range()
"""

# Ejemplo 1: range(stop) - desde 0
print("=== Ejemplo 1: range(stop) ===")
print("range(5) genera: 0, 1, 2, 3, 4")
for i in range(5):
    print(i, end=" ")
print("\n")

# Ejemplo 2: range(start, stop)
print("=== Ejemplo 2: range(start, stop) ===")
print("range(3, 8) genera:")
for i in range(3, 8):
    print(i, end=" ")
print("\n")

# Ejemplo 3: range(start, stop, step)
print("=== Ejemplo 3: range(start, stop, step) ===")
print("range(0, 10, 2) - números pares:")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

print("range(1, 10, 2) - números impares:")
for i in range(1, 10, 2):
    print(i, end=" ")
print("\n")

# Ejemplo 4: Cuenta regresiva
print("=== Ejemplo 4: Cuenta Regresiva ===")
print("range(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")
print("¡Despegue! 🚀\n")

# Ejemplo 5: Convertir range a lista
print("=== Ejemplo 5: Range a Lista ===")
numeros = list(range(1, 6))
print(f"list(range(1, 6)) = {numeros}")

pares = list(range(0, 11, 2))
print(f"Pares del 0 al 10: {pares}")

print()

# Ejemplo 6: Repetir acción N veces
print("=== Ejemplo 6: Repetir N Veces ===")
print("Imprimiendo 'Hola' 3 veces:")
for _ in range(3):
    print("  Hola!")

print()

# Ejemplo 7: Generar tabla de multiplicar
print("=== Ejemplo 7: Tabla de Multiplicar ===")
numero = 5
print(f"Tabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i:2d} = {resultado:2d}")

print()

# Ejemplo 8: Suma de números
print("=== Ejemplo 8: Suma de Números del 1 al 100 ===")
suma = 0
for num in range(1, 101):
    suma += num
print(f"Suma: {suma}")
print(f"Verificación con fórmula n*(n+1)/2: {100*101//2}")

print()

# Ejemplo 9: Cuadrados de números
print("=== Ejemplo 9: Cuadrados ===")
print("Cuadrados del 1 al 10:")
for i in range(1, 11):
    print(f"{i}² = {i**2:3d}", end="  ")
    if i % 5 == 0:  # Nueva línea cada 5 números
        print()

print()

# Ejemplo 10: Índices de una lista
print("=== Ejemplo 10: Acceso por Índice ===")
frutas = ["manzana", "banana", "naranja", "uva", "pera"]

print("Usando range(len(lista)):")
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}")

print()

# Ejemplo 11: Range con valores negativos
print("=== Ejemplo 11: Range Negativo ===")
print("range(-5, 1):")
for i in range(-5, 1):
    print(i, end=" ")
print("\n")

print("range(0, -10, -2):")
for i in range(0, -10, -2):
    print(i, end=" ")
print("\n")

# Ejemplo 12: Serie numérica
print("=== Ejemplo 12: Múltiplos de 5 ===")
print("Múltiplos de 5 hasta 50:")
multiplos = list(range(0, 51, 5))
print(multiplos)

print()

# Ejemplo 13: Años
print("=== Ejemplo 13: Rango de Años ===")
año_inicio = 2020
año_fin = 2026
print(f"Años de {año_inicio} a {año_fin}:")
for año in range(año_inicio, año_fin + 1):
    print(año, end=" ")
print("\n")

# Ejemplo 14: Comparación con lista manual
print("=== Ejemplo 14: Range vs Lista Manual ===")
# Forma ineficiente
lista_manual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista manual: {lista_manual}")

# Forma eficiente
rango = range(10)
print(f"Range: {rango}")
print(f"Convertido a lista: {list(rango)}")
print(f"Son iguales: {lista_manual == list(rango)}")

print()

# Ejemplo 15: Pattern - Espaciado
print("=== Ejemplo 15: Saltos Grandes ===")
print("Números del 0 al 100, de 10 en 10:")
for i in range(0, 101, 10):
    print(i, end=" ")
print()
