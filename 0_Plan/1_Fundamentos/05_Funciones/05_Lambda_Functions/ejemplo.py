"""
Ejemplos de Lambda Functions
==============================

Demuestra funciones lambda simples y su uso práctico
con sorted(), map() y filter().
"""

# ============================================
# 1. LAMBDA BÁSICA
# ============================================
print("=" * 50)
print("1. LAMBDA BÁSICA")
print("=" * 50)

# Comparación: función normal vs lambda
def cuadrado_normal(x):
    return x ** 2

cuadrado_lambda = lambda x: x ** 2

print(f"Normal:  cuadrado_normal(7)  = {cuadrado_normal(7)}")
print(f"Lambda:  cuadrado_lambda(7)  = {cuadrado_lambda(7)}")

# Lambdas con distintos números de parámetros
sin_arg   = lambda: 42
uno       = lambda x: x * 3
dos       = lambda x, y: x + y
tres      = lambda x, y, z: (x + y + z) / 3

print(f"\nSin argumentos: {sin_arg()}")
print(f"Un argumento:   {uno(5)}")
print(f"Dos argumentos: {dos(3, 7)}")
print(f"Tres argumentos (promedio): {tres(10, 20, 30)}")

# ============================================
# 2. LAMBDA CON sorted()
# ============================================
print("\n" + "=" * 50)
print("2. LAMBDA CON sorted()")
print("=" * 50)

# Ordenar lista de strings por longitud
palabras = ["banana", "kiwi", "manzana", "pera", "aguacate"]
por_longitud = sorted(palabras, key=lambda p: len(p))
print(f"Original:        {palabras}")
print(f"Por longitud:    {por_longitud}")

# Ordenar lista de tuplas (nombre, edad) por edad
personas = [("Carlos", 35), ("Ana", 22), ("Luis", 28), ("María", 19)]
por_edad = sorted(personas, key=lambda p: p[1])
por_nombre = sorted(personas, key=lambda p: p[0])
print(f"\nPersonas originales: {personas}")
print(f"Ordenado por edad:   {por_edad}")
print(f"Ordenado por nombre: {por_nombre}")

# Ordenar diccionarios
productos = [
    {"nombre": "Laptop", "precio": 999},
    {"nombre": "Mouse", "precio": 29},
    {"nombre": "Teclado", "precio": 79},
]
por_precio = sorted(productos, key=lambda p: p["precio"])
for p in por_precio:
    print(f"  {p['nombre']}: ${p['precio']}")

# ============================================
# 3. LAMBDA CON map()
# ============================================
print("\n" + "=" * 50)
print("3. LAMBDA CON map()")
print("=" * 50)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados  = list(map(lambda x: x ** 2, numeros))
cubos      = list(map(lambda x: x ** 3, numeros))
dobles     = list(map(lambda x: x * 2, numeros))

print(f"Originales: {numeros}")
print(f"Cuadrados:  {cuadrados}")
print(f"Cubos:      {cubos}")
print(f"Dobles:     {dobles}")

# Map con dos listas
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
sumas = list(map(lambda x, y: x + y, a, b))
print(f"\nSuma de {a} y {b}: {sumas}")

# ============================================
# 4. LAMBDA CON filter()
# ============================================
print("\n" + "=" * 50)
print("4. LAMBDA CON filter()")
print("=" * 50)

nums = list(range(1, 21))
pares    = list(filter(lambda x: x % 2 == 0, nums))
impares  = list(filter(lambda x: x % 2 != 0, nums))
mayores  = list(filter(lambda x: x > 10, nums))
divisibles = list(filter(lambda x: x % 3 == 0, nums))

print(f"Del 1 al 20:")
print(f"  Pares:          {pares}")
print(f"  Impares:        {impares}")
print(f"  Mayores que 10: {mayores}")
print(f"  Divisibles x3:  {divisibles}")

# ============================================
# 5. COMBINANDO map y filter
# ============================================
print("\n" + "=" * 50)
print("5. COMBINANDO map() Y filter()")
print("=" * 50)

# Cuadrado de los números pares del 1 al 10
resultado = list(map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 == 0, range(1, 11))
))
print(f"Cuadrado de pares del 1 al 10: {resultado}")
