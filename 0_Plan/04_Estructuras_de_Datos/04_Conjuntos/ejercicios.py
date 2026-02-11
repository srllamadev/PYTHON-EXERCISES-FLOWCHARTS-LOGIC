"""
Ejercicios de Conjuntos (set) en Python
Autor: Python Course
Fecha: 2026

Instrucciones: Completa cada función según lo indicado.
"""

# ============================================
# EJERCICIO 1: Crear y manipular conjuntos básicos
# ============================================
def ejercicio_1():
    """
    Crea un conjunto con los números del 1 al 10.
    Luego:
    - Agrega el número 11
    - Agrega los números 12, 13, 14
    - Elimina el número 5
    - Intenta eliminar el número 20 sin que cause error
    - Imprime el conjunto final
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 2: Eliminar duplicados
# ============================================
def eliminar_duplicados(lista):
    """
    Elimina duplicados de una lista y retorna una nueva lista SIN duplicados.
    Mantiene el orden de primera aparición.
    
    Ejemplo:
    eliminar_duplicados([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 3: Elementos comunes
# ============================================
def elementos_comunes(lista1, lista2):
    """
    Retorna un conjunto con los elementos que están en ambas listas.
    
    Ejemplo:
    elementos_comunes([1, 2, 3, 4], [3, 4, 5, 6]) -> {3, 4}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 4: Elementos únicos
# ============================================
def elementos_unicos(lista1, lista2):
    """
    Retorna un conjunto con elementos que están en una lista pero no en ambas.
    (Diferencia simétrica)
    
    Ejemplo:
    elementos_unicos([1, 2, 3, 4], [3, 4, 5, 6]) -> {1, 2, 5, 6}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 5: Verificar todos únicos
# ============================================
def todos_unicos(lista):
    """
    Verifica si todos los elementos de una lista son únicos.
    Retorna True si no hay duplicados, False si los hay.
    
    Ejemplo:
    todos_unicos([1, 2, 3, 4]) -> True
    todos_unicos([1, 2, 2, 3]) -> False
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 6: Unión de múltiples conjuntos
# ============================================
def union_multiple(*conjuntos):
    """
    Retorna la unión de múltiples conjuntos.
    Acepta cantidad variable de argumentos.
    
    Ejemplo:
    union_multiple({1, 2}, {2, 3}, {3, 4}) -> {1, 2, 3, 4}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 7: Intersección múltiple
# ============================================
def intersección_multiple(*conjuntos):
    """
    Retorna la intersección de múltiples conjuntos.
    (Elementos que están en TODOS los conjuntos)
    
    Ejemplo:
    intersección_multiple({1, 2, 3}, {2, 3, 4}, {2, 3, 5}) -> {2, 3}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 8: Es subconjunto
# ============================================
def es_subconjunto(conjunto_a, conjunto_b):
    """
    Verifica si conjunto_a es subconjunto de conjunto_b.
    Retorna True si todos los elementos de A están en B.
    
    Ejemplo:
    es_subconjunto({1, 2}, {1, 2, 3, 4}) -> True
    es_subconjunto({1, 5}, {1, 2, 3, 4}) -> False
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 9: Contar vocales únicas
# ============================================
def vocales_unicas(texto):
    """
    Retorna un conjunto con las vocales únicas presentes en el texto.
    Ignora mayúsculas/minúsculas.
    
    Ejemplo:
    vocales_unicas("Hola Mundo") -> {'o', 'a', 'u'}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 10: Diferencia de conjuntos
# ============================================
def solo_en_primero(conjunto_a, conjunto_b):
    """
    Retorna elementos que están en conjunto_a pero NO en conjunto_b.
    
    Ejemplo:
    solo_en_primero({1, 2, 3, 4}, {3, 4, 5, 6}) -> {1, 2}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 11: Palabras únicas en texto
# ============================================
def contar_palabras_unicas(texto):
    """
    Cuenta cuántas palabras únicas hay en un texto.
    Ignora mayúsculas/minúsculas y signos de puntuación básicos.
    
    Ejemplo:
    contar_palabras_unicas("Hola mundo. Hola Python.") -> 3
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 12: Conjunto de caracteres
# ============================================
def caracteres_unicos(texto):
    """
    Retorna un conjunto con todos los caracteres únicos del texto.
    Incluye espacios y signos de puntuación.
    
    Ejemplo:
    caracteres_unicos("hola") -> {'h', 'o', 'l', 'a'}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 13: Validar duplicados
# ============================================
def encontrar_duplicados(lista):
    """
    Encuentra y retorna un conjunto con los elementos que aparecen más de una vez.
    
    Ejemplo:
    encontrar_duplicados([1, 2, 2, 3, 1, 4]) -> {1, 2}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 14: Conjuntos disjuntos
# ============================================
def son_disjuntos(conjunto_a, conjunto_b):
    """
    Verifica si dos conjuntos son disjuntos (no tienen elementos en común).
    
    Ejemplo:
    son_disjuntos({1, 2, 3}, {4, 5, 6}) -> True
    son_disjuntos({1, 2, 3}, {3, 4, 5}) -> False
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 15: Filtrar por longitud
# ============================================
def palabras_longitud_n(palabras, n):
    """
    Retorna un conjunto con palabras que tienen exactamente n caracteres.
    
    Ejemplo:
    palabras_longitud_n(["hola", "mundo", "python", "go"], 5) -> {"hola", "mundo"}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 16: Crear set de tuplas
# ============================================
def crear_pares(lista):
    """
    Crea un conjunto de tuplas donde cada tupla es (elemento, índice).
    
    Ejemplo:
    crear_pares(['a', 'b', 'c']) -> {('a', 0), ('b', 1), ('c', 2)}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 17: Números primos
# ============================================
def numeros_primos_hasta(n):
    """
    Retorna un conjunto con todos los números primos menores o iguales a n.
    
    Ejemplo:
    numeros_primos_hasta(10) -> {2, 3, 5, 7}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 18: Anagramas
# ============================================
def son_anagramas(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas (tienen las mismas letras).
    Ignora mayúsculas/minúsculas.
    
    Ejemplo:
    son_anagramas("amor", "roma") -> True
    son_anagramas("python", "java") -> False
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 19: Set comprehension avanzado
# ============================================
def multiplos_no_comunes(n, a, b):
    """
    Retorna un conjunto con números del 1 al n que son múltiplos de a O de b,
    pero NO de ambos.
    
    Ejemplo:
    multiplos_no_comunes(20, 2, 3) -> {2, 3, 4, 8, 9, 10, 14, 15, 16, 20}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 20: Análisis de categorías
# ============================================
def analizar_categorias(productos_a, productos_b):
    """
    Dados dos conjuntos de productos de dos tiendas, retorna un diccionario con:
    - "comunes": productos en ambas tiendas
    - "solo_a": productos solo en tienda A
    - "solo_b": productos solo en tienda B
    - "total": todos los productos únicos
    
    Ejemplo:
    analizar_categorias(
        {"laptop", "mouse", "teclado"},
        {"laptop", "monitor", "teclado"}
    )
    ->
    {
        "comunes": {"laptop", "teclado"},
        "solo_a": {"mouse"},
        "solo_b": {"monitor"},
        "total": {"laptop", "mouse", "teclado", "monitor"}
    }
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
    # print(eliminar_duplicados([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
    
    # print("\nEjercicio 3:")
    # print(elementos_comunes([1, 2, 3, 4], [3, 4, 5, 6]))  # {3, 4}
    
    # print("\nEjercicio 4:")
    # print(elementos_unicos([1, 2, 3, 4], [3, 4, 5, 6]))  # {1, 2, 5, 6}
    
    # print("\nEjercicio 5:")
    # print(todos_unicos([1, 2, 3, 4]))  # True
    # print(todos_unicos([1, 2, 2, 3]))  # False
    
    # print("\nEjercicio 6:")
    # print(union_multiple({1, 2}, {2, 3}, {3, 4}))  # {1, 2, 3, 4}
    
    # print("\nEjercicio 7:")
    # print(intersección_multiple({1, 2, 3}, {2, 3, 4}, {2, 3, 5}))  # {2, 3}
    
    # print("\nEjercicio 8:")
    # print(es_subconjunto({1, 2}, {1, 2, 3, 4}))  # True
    
    # print("\nEjercicio 9:")
    # print(vocales_unicas("Hola Mundo"))  # {'o', 'a', 'u'}
    
    # print("\nEjercicio 10:")
    # print(solo_en_primero({1, 2, 3, 4}, {3, 4, 5, 6}))  # {1, 2}
    
    # print("\nEjercicio 11:")
    # print(contar_palabras_unicas("Hola mundo. Hola Python."))  # 3
    
    # print("\nEjercicio 12:")
    # print(caracteres_unicos("hola"))  # {'h', 'o', 'l', 'a'}
    
    # print("\nEjercicio 13:")
    # print(encontrar_duplicados([1, 2, 2, 3, 1, 4]))  # {1, 2}
    
    # print("\nEjercicio 14:")
    # print(son_disjuntos({1, 2, 3}, {4, 5, 6}))  # True
    
    # print("\nEjercicio 15:")
    # print(palabras_longitud_n(["hola", "mundo", "python", "go"], 5))  # {"hola", "mundo"}
    
    # print("\nEjercicio 17:")
    # print(numeros_primos_hasta(10))  # {2, 3, 5, 7}
    
    # print("\nEjercicio 18:")
    # print(son_anagramas("amor", "roma"))  # True
    
    # print("\nEjercicio 19:")
    # print(multiplos_no_comunes(20, 2, 3))
    
    # print("\nEjercicio 20:")
    # print(analizar_categorias({"laptop", "mouse", "teclado"}, {"laptop", "monitor", "teclado"}))
    
    print("\n¡Descomenta las pruebas para verificar tus soluciones!")
