"""
Ejercicios de Listas en Python
Autor: Python Course
Fecha: 2026

Instrucciones: Completa cada función según lo indicado.
"""

# ============================================
# EJERCICIO 1: Crear y manipular listas básicas
# ============================================
def ejercicio_1():
    """
    Crea una lista con los números del 1 al 10.
    Imprime:
    - La lista completa
    - El primer elemento
    - El último elemento
    - Los elementos del índice 2 al 5
    - La lista en orden inverso
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 2: Métodos de listas
# ============================================
def ejercicio_2():
    """
    Dada la lista: frutas = ["manzana", "banana"]
    
    1. Agrega "cereza" al final
    2. Inserta "durazno" en la posición 1
    3. Elimina "banana"
    4. Agrega ["kiwi", "mango"] al final
    5. Imprime la lista resultante
    """
    frutas = ["manzana", "banana"]
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 3: Sumar elementos
# ============================================
def sumar_elementos(lista):
    """
    Recibe una lista de números y retorna la suma de todos sus elementos.
    NO uses la función sum() incorporada.
    
    Ejemplo:
    sumar_elementos([1, 2, 3, 4, 5]) -> 15
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 4: Encontrar el máximo
# ============================================
def encontrar_maximo(lista):
    """
    Recibe una lista de números y retorna el valor máximo.
    NO uses la función max() incorporada.
    
    Ejemplo:
    encontrar_maximo([3, 7, 2, 9, 1]) -> 9
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 5: Invertir lista
# ============================================
def invertir_lista(lista):
    """
    Recibe una lista y retorna una nueva lista con los elementos en orden inverso.
    NO uses slicing [::-1] ni el método reverse().
    
    Ejemplo:
    invertir_lista([1, 2, 3, 4]) -> [4, 3, 2, 1]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 6: Eliminar duplicados
# ============================================
def eliminar_duplicados(lista):
    """
    Recibe una lista y retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de la primera aparición.
    
    Ejemplo:
    eliminar_duplicados([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 7: Contar ocurrencias
# ============================================
def contar_ocurrencias(lista, elemento):
    """
    Cuenta cuántas veces aparece un elemento en una lista.
    NO uses el método count().
    
    Ejemplo:
    contar_ocurrencias([1, 2, 2, 3, 2, 4], 2) -> 3
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 8: Filtrar pares
# ============================================
def filtrar_pares(lista):
    """
    Recibe una lista de números y retorna una nueva lista solo con los números pares.
    
    Ejemplo:
    filtrar_pares([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 9: Multiplicar por índice
# ============================================
def multiplicar_por_indice(lista):
    """
    Recibe una lista de números y retorna una nueva lista donde cada elemento
    está multiplicado por su índice.
    
    Ejemplo:
    multiplicar_por_indice([2, 3, 4, 5]) -> [0, 3, 8, 15]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 10: Aplanar lista anidada
# ============================================
def aplanar_lista(lista):
    """
    Recibe una lista de listas y retorna una lista simple con todos los elementos.
    
    Ejemplo:
    aplanar_lista([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 11: Encontrar índices
# ============================================
def encontrar_indices(lista, valor):
    """
    Recibe una lista y un valor, retorna una lista con todos los índices
    donde aparece ese valor.
    
    Ejemplo:
encontrar_indices([1, 2, 3, 2, 4, 2], 2) -> [1, 3, 5]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 12: Ordenar sin sort
# ============================================
def ordenar_burbuja(lista):
    """
    Implementa el algoritmo de ordenamiento burbuja.
    Retorna una nueva lista ordenada de menor a mayor.
    NO uses sort() ni sorted().
    
    Ejemplo:
    ordenar_burbuja([5, 2, 8, 1, 9]) -> [1, 2, 5, 8, 9]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 13: Rotar lista
# ============================================
def rotar_lista(lista, n):
    """
    Rota una lista n posiciones hacia la derecha.
    
    Ejemplo:
    rotar_lista([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
    rotar_lista([1, 2, 3, 4, 5], -2) -> [3, 4, 5, 1, 2]
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 14: Combinar listas alternadas
# ============================================
def combinar_alternado(lista1, lista2):
    """
    Combina dos listas alternando sus elementos.
    Si una lista es más larga, agrega los elementos restantes al final.
    
    Ejemplo:
    combinar_alternado([1, 2, 3], ['a', 'b', 'c']) -> [1, 'a', 2, 'b', 3, 'c']
    combinar_alternado([1, 2], ['a', 'b', 'c', 'd']) -> [1, 'a', 2, 'b', 'c', 'd']
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 15: Promedio de sublistas
# ============================================
def promedio_sublistas(matriz):
    """
    Recibe una lista de listas (matriz) de números.
    Retorna una lista con el promedio de cada sublista.
    
    Ejemplo:
    promedio_sublistas([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [2.0, 5.0, 8.0]
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
    # print(sumar_elementos([1, 2, 3, 4, 5]))  # Esperado: 15
    
    # print("\nEjercicio 4:")
    # print(encontrar_maximo([3, 7, 2, 9, 1]))  # Esperado: 9
    
    # print("\nEjercicio 5:")
    # print(invertir_lista([1, 2, 3, 4]))  # Esperado: [4, 3, 2, 1]
    
    # print("\nEjercicio 6:")
    # print(eliminar_duplicados([1, 2, 2, 3, 1, 4]))  # Esperado: [1, 2, 3, 4]
    
    # print("\nEjercicio 7:")
    # print(contar_ocurrencias([1, 2, 2, 3, 2, 4], 2))  # Esperado: 3
    
    # print("\nEjercicio 8:")
    # print(filtrar_pares([1, 2, 3, 4, 5, 6]))  # Esperado: [2, 4, 6]
    
    # print("\nEjercicio 9:")
    # print(multiplicar_por_indice([2, 3, 4, 5]))  # Esperado: [0, 3, 8, 15]
    
    # print("\nEjercicio 10:")
    # print(aplanar_lista([[1, 2], [3, 4], [5, 6]]))  # Esperado: [1, 2, 3, 4, 5, 6]
    
    # print("\nEjercicio 11:")
    # print(encontrar_indices([1, 2, 3, 2, 4, 2], 2))  # Esperado: [1, 3, 5]
    
    # print("\nEjercicio 12:")
    # print(ordenar_burbuja([5, 2, 8, 1, 9]))  # Esperado: [1, 2, 5, 8, 9]
    
    # print("\nEjercicio 13:")
    # print(rotar_lista([1, 2, 3, 4, 5], 2))  # Esperado: [4, 5, 1, 2, 3]
    
    # print("\nEjercicio 14:")
    # print(combinar_alternado([1, 2, 3], ['a', 'b', 'c']))  # Esperado: [1, 'a', 2, 'b', 3, 'c']
    
    # print("\nEjercicio 15:")
    # print(promedio_sublistas([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Esperado: [2.0, 5.0, 8.0]
    
    print("\n¡Descomenta las pruebas para verificar tus soluciones!")
