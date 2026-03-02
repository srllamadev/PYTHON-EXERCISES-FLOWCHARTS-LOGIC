"""
Ejemplos prácticos de Listas en Python
Autor: Python Course
Fecha: 2026
"""

# ============================================
# 1. CREACIÓN DE LISTAS
# ============================================

print("=" * 50)
print("1. CREACIÓN DE LISTAS")
print("=" * 50)

# Diferentes formas de crear listas
lista_vacia = []
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza", "durazno"]
mixta = [1, "dos", 3.0, True, None]
anidada = [[1, 2], [3, 4], [5, 6]]

# Constructor list()
del_string = list("Python")
del_rango = list(range(1, 11))
del_tuple = list((1, 2, 3))

print(f"Lista vacía: {lista_vacia}")
print(f"Números: {numeros}")
print(f"Frutas: {frutas}")
print(f"Mixta: {mixta}")
print(f"Desde string: {del_string}")
print(f"Desde rango: {del_rango}")

# ============================================
# 2. ACCESO A ELEMENTOS
# ============================================

print("\n" + "=" * 50)
print("2. ACCESO A ELEMENTOS")
print("=" * 50)

colores = ["rojo", "verde", "azul", "amarillo", "morado"]

print(f"Primer elemento: {colores[0]}")
print(f"Tercer elemento: {colores[2]}")
print(f"Último elemento: {colores[-1]}")
print(f"Penúltimo elemento: {colores[-2]}")

# Modificar elementos
colores[1] = "verde claro"
print(f"Lista modificada: {colores}")

# ============================================
# 3. SLICING (REBANADO)
# ============================================

print("\n" + "=" * 50)
print("3. SLICING")
print("=" * 50)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Original: {numeros}")
print(f"Primeros 5: {numeros[:5]}")
print(f"Últimos 3: {numeros[-3:]}")
print(f"Del índice 2 al 7: {numeros[2:8]}")
print(f"Cada 2 elementos: {numeros[::2]}")
print(f"Lista invertida: {numeros[::-1]}")
print(f"Del 1 al 8 cada 2: {numeros[1:9:2]}")

# ============================================
# 4. MÉTODOS DE LISTAS
# ============================================

print("\n" + "=" * 50)
print("4. MÉTODOS DE LISTAS")
print("=" * 50)

# append() - Agregar al final
tareas = ["estudiar", "cocinar"]
tareas.append("limpiar")
print(f"Después de append: {tareas}")

# extend() - Extender con otra lista
tareas.extend(["leer", "ejercicio"])
print(f"Después de extend: {tareas}")

# insert() - Insertar en posición específica
tareas.insert(0, "desayunar")
print(f"Después de insert: {tareas}")

# remove() - Eliminar elemento específico
tareas.remove("cocinar")
print(f"Después de remove: {tareas}")

# pop() - Eliminar y retornar
ultima_tarea = tareas.pop()
print(f"Tarea eliminada: {ultima_tarea}")
print(f"Después de pop: {tareas}")

# index() - Encontrar índice
indice = tareas.index("estudiar")
print(f"Índice de 'estudiar': {indice}")

# count() - Contar ocurrencias
numeros_repetidos = [1, 2, 2, 3, 2, 4, 2, 5]
cuenta = numeros_repetidos.count(2)
print(f"El 2 aparece {cuenta} veces en {numeros_repetidos}")

# ============================================
# 5. ORDENAMIENTO
# ============================================

print("\n" + "=" * 50)
print("5. ORDENAMIENTO")
print("=" * 50)

numeros_desordenados = [5, 2, 8, 1, 9, 3]
print(f"Original: {numeros_desordenados}")

# sort() - Ordena in-place
numeros_desordenados.sort()
print(f"Después de sort(): {numeros_desordenados}")

# sorted() - Retorna nueva lista ordenada
numeros_random = [7, 3, 9, 1, 5]
numeros_ordenados = sorted(numeros_random)
print(f"Original intacto: {numeros_random}")
print(f"Nueva lista ordenada: {numeros_ordenados}")

# Ordenar en reversa
numeros_descendente = sorted(numeros_random, reverse=True)
print(f"Orden descendente: {numeros_descendente}")

# Ordenar strings
frutas = ["banana", "manzana", "cereza", "durazno"]
frutas.sort()
print(f"Frutas ordenadas: {frutas}")

# ============================================
# 6. LISTAS ANIDADAS (MATRICES)
# ============================================

print("\n" + "=" * 50)
print("6. LISTAS ANIDADAS")
print("=" * 50)

# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for fila in matriz:
    print(fila)

print(f"\nElemento [0][0]: {matriz[0][0]}")
print(f"Elemento [1][2]: {matriz[1][2]}")
print(f"Elemento [2][1]: {matriz[2][1]}")

# Modificar elemento en matriz
matriz[1][1] = 50
print(f"\nMatriz modificada:")
for fila in matriz:
    print(fila)

# ============================================
# 7. ITERACIÓN
# ============================================

print("\n" + "=" * 50)
print("7. ITERACIÓN SOBRE LISTAS")
print("=" * 50)

lenguajes = ["Python", "JavaScript", "Java", "C++", "Ruby"]

# For simple
print("Lenguajes:")
for lenguaje in lenguajes:
    print(f"  - {lenguaje}")

# Enumerate
print("\nCon enumerate:")
for i, lenguaje in enumerate(lenguajes, start=1):
    print(f"  {i}. {lenguaje}")

# Iterar múltiples listas con zip
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
print("\nCon zip:")
for nombre, edad in zip(nombres, edades):
    print(f"  {nombre} tiene {edad} años")

# ============================================
# 8. OPERACIONES CON LISTAS
# ============================================

print("\n" + "=" * 50)
print("8. OPERACIONES")
print("=" * 50)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenación
concatenada = lista1 + lista2
print(f"Concatenación: {concatenada}")

# Repetición
repetida = lista1 * 3
print(f"Repetición: {repetida}")

# Pertenencia
print(f"¿2 está en lista1? {2 in lista1}")
print(f"¿10 está en lista1? {10 in lista1}")

# Longitud
print(f"Longitud de lista1: {len(lista1)}")

# Min, Max, Sum (con números)
numeros = [5, 2, 8, 1, 9, 3]
print(f"Mínimo: {min(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Suma: {sum(numeros)}")
print(f"Promedio: {sum(numeros) / len(numeros)}")

# ============================================
# 9. COPIAR LISTAS
# ============================================

print("\n" + "=" * 50)
print("9. COPIAR LISTAS")
print("=" * 50)

original = [1, 2, 3, 4, 5]

# Referencia (NO es copia)
referencia = original
referencia[0] = 999
print(f"Original (modificado): {original}")
print(f"Referencia: {referencia}")

# Copia superficial con copy()
original = [1, 2, 3, 4, 5]
copia = original.copy()
copia[0] = 111
print(f"\nOriginal (intacto): {original}")
print(f"Copia: {copia}")

# Copia con slicing
copia_slice = original[:]
print(f"Copia con slicing: {copia_slice}")

# ============================================
# 10. EJEMPLO PRÁCTICO: GESTIÓN DE ESTUDIANTES
# ============================================

print("\n" + "=" * 50)
print("10. EJEMPLO PRÁCTICO")
print("=" * 50)

# Sistema simple de gestión de calificaciones
estudiantes = []

# Agregar estudiantes
estudiantes.append({"nombre": "Ana", "calificaciones": [85, 90, 78]})
estudiantes.append({"nombre": "Luis", "calificaciones": [92, 88, 95]})
estudiantes.append({"nombre": "María", "calificaciones": [78, 82, 80]})

print("Reporte de estudiantes:")
print("-" * 40)

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    califs = estudiante["calificaciones"]
    promedio = sum(califs) / len(califs)
    print(f"{nombre:10} | Calificaciones: {califs} | Promedio: {promedio:.2f}")

# Encontrar mejor promedio
mejor_promedio = 0
mejor_estudiante = ""

for estudiante in estudiantes:
    promedio = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = estudiante["nombre"]

print(f"\nMejor estudiante: {mejor_estudiante} con promedio {mejor_promedio:.2f}")

print("\n" + "=" * 50)
print("FIN DE LOS EJEMPLOS")
print("=" * 50)
