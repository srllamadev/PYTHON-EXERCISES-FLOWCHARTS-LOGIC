"""
Ejercicios de Lambda Functions
================================

Completa los ejercicios siguientes. Las soluciones están al final.
"""

print("=" * 60)
print("EJERCICIOS - LAMBDA FUNCTIONS")
print("=" * 60)

# ============================================
# EJERCICIO 1: Lambdas Simples
# ============================================
print("\nEJERCICIO 1: Lambdas Simples")
print("-" * 60)
print("Crea lambdas para:")
print("  a) Calcular el área de un cuadrado (lado ** 2)")
print("  b) Convertir Celsius a Fahrenheit: (C * 9/5) + 32")
print("  c) Verificar si un número es positivo (retorna bool)")
print("  d) Obtener el último elemento de una lista")

# TODO: Escribe tus lambdas aquí




# ============================================
# EJERCICIO 2: sorted() con Lambda
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: sorted() con Lambda")
print("-" * 60)
print("Dada la siguiente lista de diccionarios:")
print("  alumnos = [")
print("      {'nombre': 'Carlos', 'nota': 7.5},")
print("      {'nombre': 'Ana',    'nota': 9.0},")
print("      {'nombre': 'Luis',   'nota': 6.0},")
print("      {'nombre': 'María',  'nota': 8.5},")
print("  ]")
print("Ordénalos:")
print("  a) Por nota de mayor a menor")
print("  b) Por nombre alfabéticamente")

alumnos = [
    {'nombre': 'Carlos', 'nota': 7.5},
    {'nombre': 'Ana',    'nota': 9.0},
    {'nombre': 'Luis',   'nota': 6.0},
    {'nombre': 'María',  'nota': 8.5},
]

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 3: map() y filter()
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: map() y filter()")
print("-" * 60)
numeros = [3, -1, 8, -4, 15, 2, -9, 6, 11, -3]
print(f"Lista: {numeros}")
print("Usando lambdas con map/filter:")
print("  a) Filtra solo los positivos")
print("  b) Eleva al cuadrado todos los números")
print("  c) Filtra los que son múltiplos de 3")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 4: RETO - Procesamiento de Datos
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: RETO - Procesar Nombres")
print("-" * 60)
nombres = ["  ana  ", "CARLOS", "maría", " LUiS ", "PEDRO"]
print(f"Nombres originales: {nombres}")
print("Usa map con lambda para:")
print("  - Eliminar espacios y convertir a título (str.strip + str.title)")

# TODO: Escribe tu código aquí




# ============================================
# SOLUCIONES
# ============================================
# area_cuadrado    = lambda lado: lado ** 2
# celsius_a_f      = lambda c: (c * 9/5) + 32
# es_positivo      = lambda x: x > 0
# ultimo_elemento  = lambda lst: lst[-1]
#
# print(area_cuadrado(5))     # 25
# print(celsius_a_f(100))     # 212.0
# print(es_positivo(-3))      # False
# print(ultimo_elemento([1, 2, 3]))  # 3
