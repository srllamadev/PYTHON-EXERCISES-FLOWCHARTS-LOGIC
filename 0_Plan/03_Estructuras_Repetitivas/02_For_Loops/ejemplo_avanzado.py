"""
FOR LOOPS - Ejemplos Avanzados
===============================
Patrones avanzados y funciones útiles con for
"""

# Ejemplo 1: enumerate() - Obtener índice y valor
print("=== Ejemplo 1: enumerate() ===")
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía"]

for indice, estudiante in enumerate(estudiantes):
    print(f"{indice + 1}. {estudiante}")

print("\n--- Con índice desde 1 ---")
for indice, estudiante in enumerate(estudiantes, start=1):
    print(f"{indice}. {estudiante}")

print()

# Ejemplo 2: zip() - Iterar múltiples listas
print("=== Ejemplo 2: zip() - Combinar listas ===")
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

print()

# Ejemplo 3: List comprehension
print("=== Ejemplo 3: List Comprehension ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Forma tradicional
cuadrados = []
for num in numeros:
    cuadrados.append(num ** 2)
print(f"Forma tradicional: {cuadrados}")

# List comprehension (más Pythónico)
cuadrados = [num ** 2 for num in numeros]
print(f"List comprehension: {cuadrados}")

# Con condición
pares_cuadrados = [num ** 2 for num in numeros if num % 2 == 0]
print(f"Cuadrados de pares: {pares_cuadrados}")

print()

# Ejemplo 4: Bucles anidados - Matriz
print("=== Ejemplo 4: Bucles Anidados - Matriz ===")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Recorriendo matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Nueva línea después de cada fila

print("\nSuma de cada fila:")
for i, fila in enumerate(matriz):
    suma_fila = sum(fila)
    print(f"Fila {i}: {fila} → Suma = {suma_fila}")

print()

# Ejemplo 5: reversed() y sorted()
print("=== Ejemplo 5: reversed() y sorted() ===")
numeros = [5, 2, 8, 1, 9, 3]

print("Original:", numeros)
print("Reverso:", list(reversed(numeros)))
print("Ordenado:", sorted(numeros))
print("Orden descendente:", sorted(numeros, reverse=True))

print("\nIteración en reverso:")
for num in reversed(numeros):
    print(num, end=" ")
print()

print()

# Ejemplo 6: Diccionario - Métodos .keys(), .values(), .items()
print("=== Ejemplo 6: Métodos de Diccionario ===")
productos = {
    "laptop": 1200,
    "mouse": 25,
    "teclado": 75,
    "monitor": 300
}

print("Solo productos:")
for producto in productos.keys():
    print(f"  - {producto}")

print("\nSolo precios:")
for precio in productos.values():
    print(f"  ${precio}")

print("\nProductos y precios:")
for producto, precio in productos.items():
    print(f"  {producto}: ${precio}")

# Calcular total
total = sum(productos.values())
print(f"\nTotal de todos los productos: ${total}")

print()

# Ejemplo 7: Patrones complejos
print("=== Ejemplo 7: Generar Patrón ===")
for i in range(1, 6):
    print("* " * i)

print()

# Ejemplo 8: Procesar datos estructurados
print("=== Ejemplo 8: Datos Estructurados ===")
estudiantes = [
    {"nombre": "Ana", "edad": 20, "notas": [8, 9, 7]},
    {"nombre": "Luis", "edad": 22, "notas": [6, 7, 8]},
    {"nombre": "María", "edad": 21, "notas": [9, 9, 10]}
]

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    edad = estudiante["edad"]
    notas = estudiante["notas"]
    promedio = sum(notas) / len(notas)
    
    print(f"{nombre} ({edad} años)")
    print(f"  Notas: {notas}")
    print(f"  Promedio: {promedio:.2f}")
    print()

# Ejemplo 9: Set comprehension y Dict comprehension
print("=== Ejemplo 9: Comprehensions Avanzadas ===")

# Set comprehension
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unicos_cuadrados = {num ** 2 for num in numeros}
print(f"Cuadrados únicos: {unicos_cuadrados}")

# Dict comprehension
palabras = ["python", "java", "rust", "go"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(f"Longitudes: {longitudes}")

print()

# Ejemplo 10: Combinación práctica
print("=== Ejemplo 10: Análisis de Ventas ===")
ventas = [
    {"producto": "Laptop", "cantidad": 2, "precio": 1200},
    {"producto": "Mouse", "cantidad": 5, "precio": 25},
    {"producto": "Teclado", "cantidad": 3, "precio": 75}
]

print("REPORTE DE VENTAS")
print("-" * 50)
total_general = 0

for i, venta in enumerate(ventas, start=1):
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    subtotal = cantidad * precio
    total_general += subtotal
    
    print(f"{i}. {producto}")
    print(f"   Cantidad: {cantidad} × ${precio} = ${subtotal}")

print("-" * 50)
print(f"TOTAL: ${total_general}")
