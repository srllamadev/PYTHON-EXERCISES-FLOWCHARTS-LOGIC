"""
FOR LOOPS - Ejemplos Básicos
=============================
Ejemplos fundamentales del uso de bucles for
"""

# Ejemplo 1: Iterar sobre una lista
print("=== Ejemplo 1: Iterar sobre Lista ===")
frutas = ["manzana", "banana", "naranja", "uva", "pera"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

print()

# Ejemplo 2: Iterar sobre un string
print("=== Ejemplo 2: Iterar sobre String ===")
palabra = "Python"
for letra in palabra:
    print(f"Letra: {letra}")

print()

# Ejemplo 3: Iterar con números
print("=== Ejemplo 3: Números del 1 al 5 ===")
for numero in [1, 2, 3, 4, 5]:
    print(f"Número: {numero}")
    print(f"  Cuadrado: {numero ** 2}")
    print(f"  Cubo: {numero ** 3}")

print()

# Ejemplo 4: Suma de elementos
print("=== Ejemplo 4: Suma de Elementos ===")
numeros = [10, 20, 30, 40, 50]
suma_total = 0

for num in numeros:
    suma_total += num
    print(f"Sumando {num}, total parcial: {suma_total}")

print(f"Suma final: {suma_total}")

print()

# Ejemplo 5: Iterar sobre diccionario
print("=== Ejemplo 5: Diccionario - Solo claves ===")
edades = {"Ana": 25, "Luis": 30, "María": 28, "Carlos": 35}

for nombre in edades:
    print(f"{nombre}")

print("\n=== Diccionario - Claves y valores ===")
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")

print()

# Ejemplo 6: Filtrar elementos
print("=== Ejemplo 6: Filtrar Números Pares ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(f"Números originales: {numeros}")
print(f"Números pares: {pares}")

print()

# Ejemplo 7: Iterar sobre tupla
print("=== Ejemplo 7: Tupla de Coordenadas ===")
coordenadas = [(0, 0), (1, 2), (3, 5), (7, 1)]

for x, y in coordenadas:
    print(f"Punto: ({x}, {y})")
    distancia = (x**2 + y**2) ** 0.5
    print(f"  Distancia al origen: {distancia:.2f}")

print()

# Ejemplo 8: Crear nueva lista
print("=== Ejemplo 8: Convertir a Mayúsculas ===")
nombres = ["juan", "maría", "pedro", "lucía"]
nombres_mayusculas = []

for nombre in nombres:
    nombres_mayusculas.append(nombre.upper())

print(f"Original: {nombres}")
print(f"Mayúsculas: {nombres_mayusculas}")

print()

# Ejemplo 9: Contar elementos
print("=== Ejemplo 9: Contar Vocales ===")
frase = "Python es un lenguaje de programación"
vocales = "aeiouAEIOU"
contador_vocales = 0

for letra in frase:
    if letra in vocales:
        contador_vocales += 1

print(f"Frase: {frase}")
print(f"Cantidad de vocales: {contador_vocales}")

print()

# Ejemplo 10: Tabla de multiplicar
print("=== Ejemplo 10: Tabla de Multiplicar ===")
numero = 7
print(f"Tabla del {numero}:")
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    resultado = numero * i
    print(f"{numero} × {i} = {resultado}")
