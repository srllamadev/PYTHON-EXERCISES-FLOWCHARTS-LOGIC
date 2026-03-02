"""
Ejemplos prácticos de Comprensiones en Python
Autor: Python Course
Fecha: 2026
"""

import sys

# ============================================
# 1. LIST COMPREHENSIONS BÁSICAS
# ============================================

print("=" * 50)
print("1. LIST COMPREHENSIONS BÁSICAS")
print("=" * 50)

# Cuadrados
cuadrados = [x**2 for x in range(10)]
print(f"Cuadrados 0-9: {cuadrados}")

# Números pares
pares = [x for x in range(20) if x % 2 == 0]
print(f"Pares 0-19: {pares}")

# Múltiplos de 3
multiplos_3 = [x for x in range(1, 31) if x % 3 == 0]
print(f"Múltiplos de 3 (1-30): {multiplos_3}")

# Conversión de temperaturas
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(9/5) * temp + 32 for temp in celsius]
print(f"\nCelsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# ============================================
# 2. LIST COMPREHENSIONS CON IF-ELSE
# ============================================

print("\n" + "=" * 50)
print("2. LIST COMPREHENSIONS CON IF-ELSE")
print("=" * 50)

# Clasificar números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
clasificacion = ["par" if x % 2 == 0 else "impar" for x in numeros]
print(f"Números: {numeros}")
print(f"Clasificación: {clasificacion}")

# Positivo, negativo o cero
valores = [-5, 0, 3, -2, 8, -1]
signos = ["positivo" if x > 0 else "negativo" if x < 0 else "cero" for x in valores]
print(f"\nValores: {valores}")
print(f"Signos: {signos}")

# Calificaciones (Aprobado/Reprobado)
calificaciones = [85, 62, 90, 45, 78, 95, 58]
resultados = ["Aprobado" if c >= 60 else "Reprobado" for c in calificaciones]
print(f"\nCalificaciones: {calificaciones}")
print(f"Resultados: {resultados}")

# ============================================
# 3. LIST COMPREHENSIONS CON STRINGS
# ============================================

print("\n" + "=" * 50)
print("3. COMPRENSIONES CON STRINGS")
print("=" * 50)

# Convertir a mayúsculas
palabras = ["python", "java", "javascript", "c++"]
mayusculas = [p.upper() for p in palabras]
print(f"Original: {palabras}")
print(f"Mayúsculas: {mayusculas}")

# Longitud de palabras
longitudes = [len(p) for p in palabras]
print(f"Longitudes: {longitudes}")

# Palabras que empiezan con 'j'
con_j = [p for p in palabras if p.startswith('j')]
print(f"Empiezan con 'j': {con_j}")

# Primera letra de cada palabra
iniciales = [p[0] for p in palabras]
print(f"Iniciales: {iniciales}")

# Invertir palabras
invertidas = [p[::-1] for p in palabras]
print(f"Invertidas: {invertidas}")

# ============================================
# 4. LIST COMPREHENSIONS ANIDADAS
# ============================================

print("\n" + "=" * 50)
print("4. COMPRENSIONES ANIDADAS")
print("=" * 50)

# Matriz 3x3
matriz = [[i*3 + j + 1 for j in range(3)] for i in range(3)]
print("Matriz 3x3:")
for fila in matriz:
    print(f"  {fila}")

# Aplanar matriz
matriz_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [num for fila in matriz_2d for num in fila]
print(f"\nMatriz 2D: {matriz_2d}")
print(f"Aplanada: {aplanada}")

# Producto cartesiano
colores = ["rojo", "azul"]
tamaños = ["S", "M", "L"]
productos = [(color, tamaño) for color in colores for tamaño in tamaños]
print(f"\nProducto cartesiano:")
print(f"Colores: {colores}, Tamaños: {tamaños}")
print(f"Combinaciones: {productos}")

# ============================================
# 5. DICT COMPREHENSIONS
# ============================================

print("\n" + "=" * 50)
print("5. DICT COMPREHENSIONS")
print("=" * 50)

# Cuadrados como diccionario
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados_dict}")

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3, "d": 4}
invertido = {v: k for k, v in original.items()}
print(f"\nOriginal: {original}")
print(f"Invertido: {invertido}")

# Filtrar diccionario
precios = {"laptop": 1000, "mouse": 25, "teclado": 75, "monitor": 300, "webcam": 80}
caros = {k: v for k, v in precios.items() if v > 50}
print(f"\nPrecios: {precios}")
print(f"Productos caros (>$50): {caros}")

# Desde dos listas con zip
nombres = ["Ana", "Luis", "María", "Carlos"]
edades = [25, 30, 28, 35]
personas = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(f"\nPersonas: {personas}")

# Transformar valores
productos_dict = {"laptop": 100, "mouse": 25, "teclado": 75}
con_iva = {prod: precio * 1.16 for prod, precio in productos_dict.items()}
print(f"\nProductos: {productos_dict}")
print(f"Con IVA (16%): {con_iva}")

# Contador de caracteres
texto = "python programming"
frecuencia = {char: texto.count(char) for char in set(texto) if char != " "}
print(f"\nTexto: '{texto}'")
print(f"Frecuencia: {frecuencia}")

# ============================================
# 6. SET COMPREHENSIONS
# ============================================

print("\n" + "=" * 50)
print("6. SET COMPREHENSIONS")
print("=" * 50)

# Cuadrados únicos
cuadrados_set = {x**2 for x in range(-5, 6)}
print(f"Cuadrados únicos (-5 a 5): {cuadrados_set}")

# Vocales en texto
texto = "Hola Mundo Python"
vocales = {c.lower() for c in texto if c.lower() in "aeiou"}
print(f"\nTexto: '{texto}'")
print(f"Vocales únicas: {vocales}")

# Longitudes únicas
palabras_lista = ["hola", "mundo", "python", "java", "go", "rust"]
longitudes_unicas = {len(p) for p in palabras_lista}
print(f"\nPalabras: {palabras_lista}")
print(f"Longitudes únicas: {longitudes_unicas}")

# Primeras letras únicas
primeras_letras = {p[0] for p in palabras_lista}
print(f"Primeras letras únicas: {primeras_letras}")

# ============================================
# 7. GENERATOR EXPRESSIONS
# ============================================

print("\n" + "=" * 50)
print("7. GENERATOR EXPRESSIONS")
print("=" * 50)

# List comprehension (carga todo en memoria)
lista = [x**2 for x in range(1000)]
print(f"List comprehension (1000 elementos): {sys.getsizeof(lista)} bytes")

# Generator expression (lazy evaluation)
generador = (x**2 for x in range(1000))
print(f"Generator expression: {sys.getsizeof(generador)} bytes")

# Usar generador con sum()
suma = sum(x**2 for x in range(100))
print(f"\nSuma de cuadrados (0-99): {suma}")

# Usar generador con max()
maximo = max(x**2 for x in range(10))
print(f"Máximo de cuadrados (0-9): {maximo}")

# Iterar sobre generador
print("\nPrimeros 5 cuadrados:")
gen = (x**2 for x in range(100))
for i, valor in enumerate(gen):
    if i >= 5:
        break
    print(f"  {i}: {valor}")

# ============================================
# 8. COMPRENSIONES CON MÚLTIPLES CONDICIONES
# ============================================

print("\n" + "=" * 50)
print("8. MÚLTIPLES CONDICIONES")
print("=" * 50)

# Números divisibles por 3 y 5
numeros = range(1, 101)
div_3_y_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]
print(f"Divisibles por 3 Y 5 (1-100): {div_3_y_5}")

# Números divisibles por 3 o 5 (pero no ambos)
div_3_o_5 = [x for x in range(1, 31) if (x % 3 == 0) != (x % 5 == 0)]
print(f"Divisibles por 3 XOR 5 (1-30): {div_3_o_5}")

# Palabras largas que empiezan con vocal
palabras_texto = ["hola", "python", "agua", "elefante", "casa", "arbol", "oro"]
largas_vocal = [p for p in palabras_texto if len(p) > 4 and p[0] in "aeiou"]
print(f"\nPalabras: {palabras_texto}")
print(f"Largas (>4) que empiezan con vocal: {largas_vocal}")

# ============================================
# 9. EJEMPLO PRÁCTICO: PROCESAMIENTO DE DATOS
# ============================================

print("\n" + "=" * 50)
print("9. EJEMPLO PRÁCTICO: ESTUDIANTES")
print("=" * 50)

# Datos de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificaciones": [85, 90, 92]},
    {"nombre": "Luis", "edad": 22, "calificaciones": [78, 85, 88]},
    {"nombre": "María", "edad": 21, "calificaciones": [95, 92, 98]},
    {"nombre": "Carlos", "edad": 23, "calificaciones": [70, 75, 72]},
]

# Promedios
promedios = {
    est["nombre"]: sum(est["calificaciones"]) / len(est["calificaciones"])
    for est in estudiantes
}
print("Promedios:")
for nombre, prom in promedios.items():
    print(f"  {nombre}: {prom:.2f}")

# Estudiantes aprobados (promedio >= 80)
aprobados = [
    est["nombre"] for est in estudiantes 
    if sum(est["calificaciones"]) / len(est["calificaciones"]) >= 80
]
print(f"\nAprobados (promedio >= 80): {aprobados}")

# Mayores de 21 años
mayores = [est["nombre"] for est in estudiantes if est["edad"] > 21]
print(f"Mayores de 21: {mayores}")

# ============================================
# 10. EJEMPLO PRÁCTICO: ANÁLISIS DE TEXTO
# ============================================

print("\n" + "=" * 50)
print("10. EJEMPLO PRÁCTICO: ANÁLISIS DE TEXTO")
print("=" * 50)

texto_largo = """
Python es un lenguaje de programación interpretado.
Su filosofía hace hincapié en la legibilidad del código.
Se trata de un lenguaje de programación multiparadigma.
"""

# Todas las palabras
palabras_todas = texto_largo.split()
print(f"Total palabras: {len(palabras_todas)}")

# Palabras únicas (sin puntuación)
import string
palabras_limpias = [
    p.strip(string.punctuation).lower() 
    for p in palabras_todas 
    if p.strip(string.punctuation)
]
palabras_unicas = set(palabras_limpias)
print(f"Palabras únicas: {len(palabras_unicas)}")

# Palabras largas (>7 caracteres)
palabras_largas = [p for p in palabras_unicas if len(p) > 7]
print(f"Palabras largas (>7): {sorted(palabras_largas)}")

# Frecuencia de longitudes
freq_longitudes = {
    long: len([p for p in palabras_unicas if len(p) == long])
    for long in range(1, max(len(p) for p in palabras_unicas) + 1)
}
print(f"\nFrecuencia de longitudes:")
for long, freq in sorted(freq_longitudes.items()):
    if freq > 0:
        print(f"  {long} letras: {freq} palabra(s)")

# ============================================
# 11. EJEMPLO PRÁCTICO: MATRIZ TRANSPUESTA
# ============================================

print("\n" + "=" * 50)
print("11. TRANSPOSICIÓN DE MATRIZ")
print("=" * 50)

# Matriz original
matriz_original = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Matriz original (3x4):")
for fila in matriz_original:
    print(f"  {fila}")

# Transponer
transpuesta = [[fila[i] for fila in matriz_original] for i in range(len(matriz_original[0]))]

print("\nMatriz transpuesta (4x3):")
for fila in transpuesta:
    print(f"  {fila}")

# ============================================
# 12. PATRÓN: FILTRAR NONE
# ============================================

print("\n" + "=" * 50)
print("12. PATRÓN: FILTRAR VALORES NONE")
print("=" * 50)

lista_con_none = [1, None, 3, None, 5, None, 7, 8, None, 10]
sin_none = [x for x in lista_con_none if x is not None]

print(f"Con None: {lista_con_none}")
print(f"Sin None: {sin_none}")

# ============================================
# 13. PATRÓN: COMBINAR MÚLTIPLES LISTAS
# ============================================

print("\n" + "=" * 50)
print("13. PATRÓN: COMBINAR LISTAS")
print("=" * 50)

nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]

# Como lista de diccionarios
personas_completo = [
    {"nombre": n, "edad": e, "ciudad": c}
    for n, e, c in zip(nombres, edades, ciudades)
]

print("Personas (lista de dicts):")
for persona in personas_completo:
    print(f"  {persona}")

# Como lista de tuplas
personas_tuplas = [(n, e, c) for n, e, c in zip(nombres, edades, ciudades)]
print(f"\nPersonas (tuplas): {personas_tuplas}")

# ============================================
# 14. COMPARACIÓN: COMPREHENSION VS BUCLE
# ============================================

print("\n" + "=" * 50)
print("14. COMPARACIÓN: COMPREHENSION VS BUCLE")
print("=" * 50)

import time

# Medir tiempo con comprehension
inicio = time.time()
comp = [x**2 for x in range(100000)]
tiempo_comp = time.time() - inicio

# Medir tiempo con bucle tradicional
inicio = time.time()
loop = []
for x in range(100000):
    loop.append(x**2)
tiempo_loop = time.time() - inicio

print(f"Comprehension: {tiempo_comp:.6f} segundos")
print(f"Bucle tradicional: {tiempo_loop:.6f} segundos")
print(f"Diferencia: {((tiempo_loop - tiempo_comp) / tiempo_comp * 100):.2f}% más rápido")

print("\n" + "=" * 50)
print("FIN DE LOS EJEMPLOS")
print("=" * 50)
