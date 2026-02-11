"""
Ejercicios de Tuplas en Python
Autor: Python Course
Fecha: 2026

Instrucciones: Completa cada función según lo indicado.
"""

from collections import namedtuple

# ============================================
# EJERCICIO 1: Crear y manipular tuplas básicas
# ============================================
def ejercicio_1():
    """
    Crea una tupla con los días de la semana.
    Imprime:
    - La tupla completa
    - El primer y último día
    - Los días laborales (lunes a viernes)
    - Los días en orden inverso
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 2: Desempaquetado
# ============================================
def ejercicio_2():
    """
    Dada la tupla: datos = ("Python", 1991, "Guido van Rossum", True)
    
    Desempaqueta los valores en variables:
    lenguaje, año, creador, es_popular
    
    Imprime cada variable con un mensaje descriptivo.
    """
    datos = ("Python", 1991, "Guido van Rossum", True)
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 3: Swap de variables
# ============================================
def intercambiar_valores(a, b):
    """
    Intercambia los valores de dos variables usando tuplas.
    Retorna una tupla con los valores intercambiados.
    
    Ejemplo:
    intercambiar_valores(5, 10) -> (10, 5)
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 4: Encontrar elemento
# ============================================
def encontrar_posicion(tupla, elemento):
    """
    Encuentra la posición de un elemento en una tupla.
    Si no existe, retorna -1.
    
    Ejemplo:
    encontrar_posicion((1, 2, 3, 4), 3) -> 2
    encontrar_posicion((1, 2, 3, 4), 5) -> -1
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 5: Contar elementos
# ============================================
def contar_vocales(texto):
    """
    Cuenta cuántas veces aparece cada vocal en un texto.
    Retorna una tupla con los conteos en orden (a, e, i, o, u).
    
    Ejemplo:
    contar_vocales("hola mundo") -> (1, 0, 0, 2, 1)
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 6: Tuplas anidadas
# ============================================
def sumar_coordenadas(punto1, punto2):
    """
    Recibe dos tuplas que representan puntos 2D (x, y).
    Retorna una nueva tupla con la suma de las coordenadas.
    
    Ejemplo:
    sumar_coordenadas((1, 2), (3, 4)) -> (4, 6)
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 7: Convertir lista a tupla
# ============================================
def lista_a_tupla_anidada(lista):
    """
    Recibe una lista y retorna una tupla donde cada elemento
    es una tupla (índice, valor).
    
    Ejemplo:
    lista_a_tupla_anidada(['a', 'b', 'c']) -> ((0, 'a'), (1, 'b'), (2, 'c'))
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 8: Encontrar min y max
# ============================================
def minimo_maximo(tupla):
    """
    Recibe una tupla de números y retorna una tupla con (mínimo, máximo).
    NO uses las funciones min() y max() incorporadas.
    
    Ejemplo:
    minimo_maximo((5, 2, 8, 1, 9)) -> (1, 9)
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 9: Retornar múltiples valores
# ============================================
def estadisticas_texto(texto):
    """
    Analiza un texto y retorna una tupla con:
    (número de caracteres, número de palabras, número de vocales, número de consonantes)
    
    Ejemplo:
    estadisticas_texto("Hola mundo") -> (10, 2, 4, 5)
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 10: Tuplas como claves
# ============================================
def crear_tablero_ajedrez():
    """
    Crea un diccionario que represente un tablero de ajedrez 8x8.
    Las claves son tuplas (fila, columna) donde fila y columna van de 1 a 8.
    Los valores son "blanco" o "negro" según el patrón del tablero.
    
    Retorna el diccionario.
    Pista: Una casilla es blanca si (fila + columna) es par.
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 11: Tuplas nombradas
# ============================================
def ejercicio_11():
    """
    Crea una tupla nombrada 'Libro' con los campos:
    titulo, autor, año, paginas
    
    Crea 3 instancias de libros e imprímelas.
    Encuentra el libro con más páginas.
    """
    # Tu código aquí
    # Libro = namedtuple(...)
    pass


# ============================================
# EJERCICIO 12: Ordenar tupla de tuplas
# ============================================
def ordenar_por_segundo(tupla_de_tuplas):
    """
    Recibe una tupla de tuplas y retorna una lista ordenada
    por el segundo elemento de cada tupla interna.
    
    Ejemplo:
    ordenar_por_segundo((('a', 3), ('b', 1), ('c', 2))) -> [('b', 1), ('c', 2), ('a', 3)]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 13: Desempaquetado con *
# ============================================
def obtener_primero_ultimo_resto(tupla):
    """
    Recibe una tupla y retorna una tupla de 3 elementos:
    (primer elemento, último elemento, tupla con el resto)
    
    Ejemplo:
    obtener_primero_ultimo_resto((1, 2, 3, 4, 5)) -> (1, 5, (2, 3, 4))
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 14: Crear tupla desde rango
# ============================================
def crear_tupla_pares(n):
    """
    Crea y retorna una tupla con los números pares desde 0 hasta n (sin incluir n).
    
    Ejemplo:
    crear_tupla_pares(10) -> (0, 2, 4, 6, 8)
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 15: Matriz como tupla de tuplas
# ============================================
def transponer_matriz(matriz):
    """
    Recibe una matriz (tupla de tuplas) y retorna su transpuesta.
    
    Ejemplo:
    transponer_matriz(((1, 2, 3), (4, 5, 6))) -> ((1, 4), (2, 5), (3, 6))
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 16: Inmutabilidad
# ============================================
def ejercicio_16():
    """
    Demuestra la inmutabilidad de las tuplas.
    
    1. Crea una tupla con números [1, 2, 3, 4, 5]
    2. Intenta "modificar" el segundo elemento a 10 creando una nueva tupla
    3. Imprime ambas tuplas para demostrar que la original no cambió
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 17: Frecuencia de elementos
# ============================================
def frecuencia_elementos(tupla):
    """
    Recibe una tupla y retorna un diccionario con la frecuencia de cada elemento.
    
    Ejemplo:
    frecuencia_elementos((1, 2, 2, 3, 1, 4, 1)) -> {1: 3, 2: 2, 3: 1, 4: 1}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 18: Comparar tuplas
# ============================================
def tuplas_iguales(tupla1, tupla2):
    """
    Compara dos tuplas y retorna True si tienen los mismos elementos
    en el mismo orden, False en caso contrario.
    
    Ejemplo:
    tuplas_iguales((1, 2, 3), (1, 2, 3)) -> True
    tuplas_iguales((1, 2, 3), (3, 2, 1)) -> False
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 19: Producto cartesiano
# ============================================
def producto_cartesiano(tupla1, tupla2):
    """
    Retorna una tupla de tuplas representando el producto cartesiano
    de dos tuplas.
    
    Ejemplo:
    producto_cartesiano((1, 2), ('a', 'b')) -> ((1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'))
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 20: Sistema de coordenadas
# ============================================
def distancia_euclidiana(punto1, punto2):
    """
    Calcula la distancia euclidiana entre dos puntos 2D.
    Los puntos son tuplas (x, y).
    
    Fórmula: sqrt((x2-x1)² + (y2-y1)²)
    
    Ejemplo:
    distancia_euclidiana((0, 0), (3, 4)) -> 5.0
    """
    # Tu código aquí
    pass


# ============================================
# PRUEBAS (NO MODIFICAR)
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("PRUEBAS DE EJERCICIOS")
    print("=" * 50)
    
    # Descomentar para probar cada ejercicio
    
    # print("\nEjercicio 1:")
    # ejercicio_1()
    
    # print("\nEjercicio 2:")
    # ejercicio_2()
    
    # print("\nEjercicio 3:")
    # print(intercambiar_valores(5, 10))  # Esperado: (10, 5)
    
    # print("\nEjercicio 4:")
    # print(encontrar_posicion((1, 2, 3, 4), 3))  # Esperado: 2
    # print(encontrar_posicion((1, 2, 3, 4), 5))  # Esperado: -1
    
    # print("\nEjercicio 5:")
    # print(contar_vocales("hola mundo"))  # Esperado: (1, 0, 0, 2, 1)
    
    # print("\nEjercicio 6:")
    # print(sumar_coordenadas((1, 2), (3, 4)))  # Esperado: (4, 6)
    
    # print("\nEjercicio 7:")
    # print(lista_a_tupla_anidada(['a', 'b', 'c']))  # Esperado: ((0, 'a'), (1, 'b'), (2, 'c'))
    
    # print("\nEjercicio 8:")
    # print(minimo_maximo((5, 2, 8, 1, 9)))  # Esperado: (1, 9)
    
    # print("\nEjercicio 9:")
    # print(estadisticas_texto("Hola mundo"))  # Esperado: (10, 2, 4, 5)
    
    # print("\nEjercicio 12:")
    # print(ordenar_por_segundo((('a', 3), ('b', 1), ('c', 2))))  # Esperado: [('b', 1), ('c', 2), ('a', 3)]
    
    # print("\nEjercicio 13:")
    # print(obtener_primero_ultimo_resto((1, 2, 3, 4, 5)))  # Esperado: (1, 5, (2, 3, 4))
    
    # print("\nEjercicio 14:")
    # print(crear_tupla_pares(10))  # Esperado: (0, 2, 4, 6, 8)
    
    # print("\nEjercicio 15:")
    # print(transponer_matriz(((1, 2, 3), (4, 5, 6))))  # Esperado: ((1, 4), (2, 5), (3, 6))
    
    # print("\nEjercicio 17:")
    # print(frecuencia_elementos((1, 2, 2, 3, 1, 4, 1)))  # Esperado: {1: 3, 2: 2, 3: 1, 4: 1}
    
    # print("\nEjercicio 18:")
    # print(tuplas_iguales((1, 2, 3), (1, 2, 3)))  # Esperado: True
    
    # print("\nEjercicio 19:")
    # print(producto_cartesiano((1, 2), ('a', 'b')))  # Esperado: ((1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'))
    
    # print("\nEjercicio 20:")
    # print(distancia_euclidiana((0, 0), (3, 4)))  # Esperado: 5.0
    
    print("\n¡Descomenta las pruebas para verificar tus soluciones!")
