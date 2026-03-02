"""
Ejercicios de Comprensiones en Python
Autor: Python Course
Fecha: 2026

Instrucciones: Completa cada función usando comprensiones.
"""

# ============================================
# LIST COMPREHENSIONS
# ============================================

# EJERCICIO 1: Cubos
# ============================================
def cubos(n):
    """
    Retorna una lista con los cubos de números del 1 al n.
    Usa list comprehension.
    
    Ejemplo:
    cubos(5) -> [1, 8, 27, 64, 125]
    """
    # Tu código aquí
    pass


# EJERCICIO 2: Filtrar múltiplos
# ============================================
def multiplos_de_n(lista, n):
    """
    Retorna lista con solo los números que son múltiplos de n.
    
    Ejemplo:
    multiplos_de_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) -> [3, 6, 9]
    """
    # Tu código aquí
    pass


# EJERCICIO 3: Palabras capitalizadas
# ============================================
def capitalizar_palabras(frase):
    """
    Retorna lista de palabras capitalizadas (primera letra mayúscula).
    
    Ejemplo:
    capitalizar_palabras("hola mundo python") -> ["Hola", "Mundo", "Python"]
    """
    # Tu código aquí
    pass


# EJERCICIO 4: Números en rango
# ============================================
def numeros_en_rango(lista, min_val, max_val):
    """
    Retorna lista con números que están entre min_val y max_val (inclusive).
    
    Ejemplo:
    numeros_en_rango([1, 5, 10, 15, 20], 5, 15) -> [5, 10, 15]
    """
    # Tu código aquí
    pass


# EJERCICIO 5: Clasificar por paridad
# ============================================
def clasificar_paridad(numeros):
    """
    Retorna lista de strings: "PAR" o "IMPAR" para cada número.
    
    Ejemplo:
    clasificar_paridad([1, 2, 3, 4, 5]) -> ["IMPAR", "PAR", "IMPAR", "PAR", "IMPAR"]
    """
    # Tu código aquí
    pass


# EJERCICIO 6: Aplanar matriz
# ============================================
def aplanar(matriz):
    """
    Aplana una matriz (lista de listas) en una sola lista.
    
    Ejemplo:
    aplanar([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    # Tu código aquí
    pass


# EJERCICIO 7: Primeras letras
# ============================================
def primeras_letras(palabras):
    """
    Retorna lista con la primera letra de cada palabra.
    
    Ejemplo:
    primeras_letras(["Python", "Java", "C++"]) -> ["P", "J", "C"]
    """
    # Tu código aquí
    pass


# EJERCICIO 8: Producto cartesiano
# ============================================
def producto_cartesiano(lista1, lista2):
    """
    Retorna lista de tuplas con todas las combinaciones posibles.
    
    Ejemplo:
    producto_cartesiano([1, 2], ["a", "b"]) -> [(1, "a"), (1, "b"), (2, "a"), (2, "b")]
    """
    # Tu código aquí
    pass


# EJERCICIO 9: Filtrar strings vacíos
# ============================================
def filtrar_vacios(lista):
    """
    Retorna lista sin strings vacíos o que solo contienen espacios.
    
    Ejemplo:
    filtrar_vacios(["hola", "", "mundo", "  ", "python"]) -> ["hola", "mundo", "python"]
    """
    # Tu código aquí
    pass


# EJERCICIO 10: Números pares al cuadrado
# ============================================
def pares_al_cuadrado(n):
    """
    Retorna lista con los cuadrados de números pares del 0 al n.
    
    Ejemplo:
    pares_al_cuadrado(10) -> [0, 4, 16, 36, 64, 100]
    """
    # Tu código aquí
    pass


# ============================================
# DICT COMPREHENSIONS
# ============================================

# EJERCICIO 11: Diccionario de longitudes
# ============================================
def longitudes_palabras(palabras):
    """
    Retorna diccionario con palabra: longitud.
    
    Ejemplo:
    longitudes_palabras(["hola", "mundo", "python"]) -> {"hola": 4, "mundo": 5, "python": 6}
    """
    # Tu código aquí
    pass


# EJERCICIO 12: Invertir diccionario de listas
# ============================================
def invertir_dict_listas(diccionario):
    """
    Invierte un diccionario donde los valores son listas.
    Cada elemento de la lista se convierte en clave con el valor original como valor.
    
    Ejemplo:
    invertir_dict_listas({"a": [1, 2], "b": [3, 4]}) -> {1: "a", 2: "a", 3: "b", 4: "b"}
    """
    # Tu código aquí
    pass


# EJERCICIO 13: Filtrar diccionario
# ============================================
def filtrar_diccionario(diccionario, valor_minimo):
    """
    Retorna nuevo diccionario solo con pares donde valor > valor_minimo.
    
    Ejemplo:
    filtrar_diccionario({"a": 5, "b": 10, "c": 3}, 4) -> {"a": 5, "b": 10}
    """
    # Tu código aquí
    pass


# EJERCICIO 14: Cuadrados de pares
# ============================================
def dict_cuadrados_pares(n):
    """
    Retorna diccionario con números pares (0 a n) como claves y sus cuadrados como valores.
    
    Ejemplo:
    dict_cuadrados_pares(10) -> {0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
    """
    # Tu código aquí
    pass


# EJERCICIO 15: Contar vocales por palabra
# ============================================
def contar_vocales_por_palabra(palabras):
    """
    Retorna diccionario con palabra: cantidad de vocales.
    
    Ejemplo:
    contar_vocales_por_palabra(["hola", "python"]) -> {"hola": 2, "python": 1}
    """
    # Tu código aquí
    pass


# ============================================
# SET COMPREHENSIONS
# ============================================

# EJERCICIO 16: Caracteres únicos
# ============================================
def caracteres_unicos_multi(palabras):
    """
    Retorna conjunto con todos los caracteres únicos de todas las palabras.
    
    Ejemplo:
    caracteres_unicos_multi(["hola", "mundo"]) -> {"h", "o", "l", "a", "m", "u", "n", "d"}
    """
    # Tu código aquí
    pass


# EJERCICIO 17: Longitudes únicas
# ============================================
def longitudes_unicas(palabras):
    """
    Retorna conjunto con las longitudes únicas de las palabras.
    
    Ejemplo:
    longitudes_unicas(["hola", "hi", "python", "go"]) -> {2, 4, 6}
    """
    # Tu código aquí
    pass


# EJERCICIO 18: Dígitos en texto
# ============================================
def digitos_en_texto(texto):
    """
    Retorna conjunto con todos los dígitos que aparecen en el texto.
    
    Ejemplo:
    digitos_en_texto("En 2024 hay 365 días") -> {"2", "0", "4", "3", "6", "5"}
    """
    # Tu código aquí
    pass


# EJERCICIO 19: Primeras letras únicas mayúsculas
# ============================================
def primeras_letras_unicas(palabras):
    """
    Retorna conjunto con las primeras letras (en mayúsculas) de cada palabra.
    
    Ejemplo:
    primeras_letras_unicas(["python", "java", "javascript", "perl"]) -> {"P", "J"}
    """
    # Tu código aquí
    pass


# EJERCICIO 20: Factores únicos
# ============================================
def factores_unicos(numeros):
    """
    Retorna conjunto con todos los factores únicos de todos los números.
    
    Ejemplo:
    factores_unicos([6, 12]) -> {1, 2, 3, 4, 6, 12}
    """
    # Tu código aquí
    pass


# ============================================
# COMPREHENSIONS AVANZADAS
# ============================================

# EJERCICIO 21: Matriz transpuesta
# ============================================
def transponer(matriz):
    """
    Transpone una matriz usando list comprehension.
    
    Ejemplo:
    transponer([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
    """
    # Tu código aquí
    pass


# EJERCICIO 22: Promedio de sublistas
# ============================================
def promedios(matriz):
    """
    Retorna lista con el promedio de cada sublista.
    
    Ejemplo:
    promedios([[1, 2, 3], [4, 5, 6]]) -> [2.0, 5.0]
    """
    # Tu código aquí
    pass


# EJERCICIO 23: Frecuencia de caracteres
# ============================================
def frecuencia_caracteres(texto):
    """
    Retorna diccionario con la frecuencia de cada carácter (excepto espacios).
    Usa dict comprehension.
    
    Ejemplo:
    frecuencia_caracteres("hola") -> {"h": 1, "o": 1, "l": 1, "a": 1}
    """
    # Tu código aquí
    pass


# EJERCICIO 24: Crear rango con salto
# ============================================
def rango_personalizado(inicio, fin, salto):
    """
    Crea lista desde inicio hasta fin (exclusive) con saltos personalizados.
    
    Ejemplo:
    rango_personalizado(0, 20, 3) -> [0, 3, 6, 9, 12, 15, 18]
    """
    # Tu código aquí
    pass


# EJERCICIO 25: Combinar listas en diccionario
# ============================================
def listas_a_dict(claves, valores, defecto=None):
    """
    Combina dos listas en un diccionario.
    Si valores es más corto, usa defecto para claves restantes.
    
    Ejemplo:
    listas_a_dict(["a", "b", "c"], [1, 2], 0) -> {"a": 1, "b": 2, "c": 0}
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
    # print(cubos(5))  # [1, 8, 27, 64, 125]
    
    # print("\nEjercicio 2:")
    # print(multiplos_de_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # [3, 6, 9]
    
    # print("\nEjercicio 3:")
    # print(capitalizar_palabras("hola mundo python"))  # ["Hola", "Mundo", "Python"]
    
    # print("\nEjercicio 4:")
    # print(numeros_en_rango([1, 5, 10, 15, 20], 5, 15))  # [5, 10, 15]
    
    # print("\nEjercicio 5:")
    # print(clasificar_paridad([1, 2, 3, 4, 5]))  # ["IMPAR", "PAR", "IMPAR", "PAR", "IMPAR"]
    
    # print("\nEjercicio 6:")
    # print(aplanar([[1, 2], [3, 4], [5, 6]]))  # [1, 2, 3, 4, 5, 6]
    
    # print("\nEjercicio 7:")
    # print(primeras_letras(["Python", "Java", "C++"]))  # ["P", "J", "C"]
    
    # print("\nEjercicio 8:")
    # print(producto_cartesiano([1, 2], ["a", "b"]))
    
    # print("\nEjercicio 10:")
    # print(pares_al_cuadrado(10))  # [0, 4, 16, 36, 64, 100]
    
    # print("\nEjercicio 11:")
    # print(longitudes_palabras(["hola", "mundo", "python"]))
    
    # print("\nEjercicio 13:")
    # print(filtrar_diccionario({"a": 5, "b": 10, "c": 3}, 4))
    
    # print("\nEjercicio 14:")
    # print(dict_cuadrados_pares(10))
    
    # print("\nEjercicio 16:")
    # print(caracteres_unicos_multi(["hola", "mundo"]))
    
    # print("\nEjercicio 17:")
    # print(longitudes_unicas(["hola", "hi", "python", "go"]))
    
    # print("\nEjercicio 18:")
    # print(digitos_en_texto("En 2024 hay 365 días"))
    
    # print("\nEjercicio 21:")
    # print(transponer([[1, 2, 3], [4, 5, 6]]))
    
    # print("\nEjercicio 22:")
    # print(promedios([[1, 2, 3], [4, 5, 6]]))
    
    # print("\nEjercicio 23:")
    # print(frecuencia_caracteres("hola"))
    
    # print("\nEjercicio 24:")
    # print(rango_personalizado(0, 20, 3))
    
    # print("\nEjercicio 25:")
    # print(listas_a_dict(["a", "b", "c"], [1, 2], 0))
    
    print("\n¡Descomenta las pruebas para verificar tus soluciones!")
