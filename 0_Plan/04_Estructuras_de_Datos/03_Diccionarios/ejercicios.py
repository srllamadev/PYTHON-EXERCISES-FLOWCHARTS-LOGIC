"""
Ejercicios de Diccionarios en Python
Autor: Python Course
Fecha: 2026

Instrucciones: Completa cada función según lo indicado.
"""

from collections import defaultdict, Counter

# ============================================
# EJERCICIO 1: Crear y manipular diccionarios básicos
# ============================================
def ejercicio_1():
    """
    Crea un diccionario con información de un libro:
    titulo, autor, año, paginas, genero
    
    Imprime:
    - El diccionario completo
    - Solo el título y autor
    - Agrega un campo "leido" con valor True
    - Modifica el año a 2020
    - Elimina el campo "paginas"
    - Imprime el diccionario final
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 2: Contar frecuencias
# ============================================
def contar_frecuencia(texto):
    """
    Cuenta la frecuencia de cada carácter en un texto.
    Retorna un diccionario con los caracteres y sus frecuencias.
    Ignora mayúsculas/minúsculas y espacios.
    
    Ejemplo:
    contar_frecuencia("Hola Mundo") -> {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 3: Invertir diccionario
# ============================================
def invertir_diccionario(diccionario):
    """
    Invierte un diccionario (las claves se vuelven valores y viceversa).
    Asume que los valores son únicos.
    
    Ejemplo:
    invertir_diccionario({"a": 1, "b": 2, "c": 3}) -> {1: "a", 2: "b", 3: "c"}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 4: Fusionar diccionarios
# ============================================
def fusionar_diccionarios(dict1, dict2):
    """
    Fusiona dos diccionarios. Si hay claves duplicadas, suma los valores.
    
    Ejemplo:
    fusionar_diccionarios({"a": 1, "b": 2}, {"b": 3, "c": 4}) -> {"a": 1, "b": 5, "c": 4}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 5: Filtrar diccionario
# ============================================
def filtrar_mayores(diccionario, umbral):
    """
    Retorna un nuevo diccionario con solo los pares cuyo valor sea mayor al umbral.
    
    Ejemplo:
    filtrar_mayores({"a": 5, "b": 10, "c": 3, "d": 8}, 5) -> {"b": 10, "d": 8}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 6: Agrupar por longitud
# ============================================
def agrupar_por_longitud(palabras):
    """
    Agrupa una lista de palabras por su longitud.
    Retorna un diccionario donde las claves son longitudes
    y los valores son listas de palabras con esa longitud.
    
    Ejemplo:
    agrupar_por_longitud(["hola", "hi", "python", "go"]) 
    -> {4: ["hola"], 2: ["hi", "go"], 6: ["python"]}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 7: Diccionario de cuadrados
# ============================================
def crear_diccionario_cuadrados(n):
    """
    Crea un diccionario donde las claves son números del 1 al n
    y los valores son sus cuadrados.
    Usa dict comprehension.
    
    Ejemplo:
    crear_diccionario_cuadrados(5) -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 8: Encontrar clave por valor
# ============================================
def encontrar_clave(diccionario, valor):
    """
    Encuentra y retorna la primera clave que tenga el valor especificado.
    Si no existe, retorna None.
    
    Ejemplo:
    encontrar_clave({"a": 1, "b": 2, "c": 3}, 2) -> "b"
    encontrar_clave({"a": 1, "b": 2, "c": 3}, 5) -> None
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 9: Contar palabras
# ============================================
def contar_palabras(texto):
    """
    Cuenta cuántas veces aparece cada palabra en un texto.
    Ignora mayúsculas/minúsculas y signos de puntuación.
    Retorna un diccionario con las palabras y sus frecuencias.
    
    Ejemplo:
    contar_palabras("Hola mundo. Hola Python.") -> {"hola": 2, "mundo": 1, "python": 1}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 10: Promedio de calificaciones
# ============================================
def promedio_calificaciones(estudiantes):
    """
    Recibe un diccionario donde las claves son nombres de estudiantes
    y los valores son listas de calificaciones.
    Retorna un nuevo diccionario con los promedios.
    
    Ejemplo:
    promedio_calificaciones({
        "Ana": [85, 90, 92],
        "Luis": [78, 85, 88]
    }) -> {"Ana": 89.0, "Luis": 83.67}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 11: Diccionario anidado
# ============================================
def crear_agenda():
    """
    Crea y retorna un diccionario que represente una agenda de contactos.
    Cada contacto debe tener: teléfono, email, ciudad.
    Crea al menos 3 contactos.
    
    Formato esperado:
    {
        "Juan": {"telefono": "555-1234", "email": "juan@email.com", "ciudad": "Madrid"},
        ...
    }
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 12: Actualizar precios
# ============================================
def aplicar_descuento(productos, descuento):
    """
    Aplica un descuento porcentual a todos los precios de un diccionario.
    Modifica el diccionario original (in-place).
    
    Ejemplo:
    productos = {"laptop": 1000, "mouse": 25, "teclado": 75}
    aplicar_descuento(productos, 10)
    # productos ahora es {"laptop": 900.0, "mouse": 22.5, "teclado": 67.5}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 13: Diccionario de listas
# ============================================
def clasificar_numeros(numeros):
    """
    Clasifica una lista de números en "pares" e "impares".
    Retorna un diccionario con dos claves: "pares" e "impares",
    cada una con una lista de números correspondiente.
    
    Ejemplo:
    clasificar_numeros([1, 2, 3, 4, 5, 6]) -> {"pares": [2, 4, 6], "impares": [1, 3, 5]}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 14: Eliminar claves
# ============================================
def eliminar_claves(diccionario, claves):
    """
    Elimina una lista de claves de un diccionario.
    Retorna un nuevo diccionario sin esas claves.
    Si una clave no existe, simplemente ignórala.
    
    Ejemplo:
    eliminar_claves({"a": 1, "b": 2, "c": 3, "d": 4}, ["b", "d", "e"]) -> {"a": 1, "c": 3}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 15: Diccionario desde dos listas
# ============================================
def crear_diccionario_desde_listas(claves, valores):
    """
    Crea un diccionario a partir de dos listas: una de claves y otra de valores.
    Si las listas tienen diferente longitud, usa la más corta.
    
    Ejemplo:
    crear_diccionario_desde_listas(["a", "b", "c"], [1, 2, 3]) -> {"a": 1, "b": 2, "c": 3}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 16: Valor más frecuente
# ============================================
def valor_mas_frecuente(diccionario):
    """
    Encuentra el valor que más se repite en un diccionario.
    Retorna una tupla (valor, frecuencia).
    
    Ejemplo:
    valor_mas_frecuente({"a": 1, "b": 2, "c": 1, "d": 2, "e": 2}) -> (2, 3)
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 17: Aplanar diccionario anidado
# ============================================
def aplanar_diccionario(diccionario_anidado):
    """
    Aplana un diccionario anidado de un nivel.
    Usa el formato "clave_padre.clave_hija" para las nuevas claves.
    
    Ejemplo:
    aplanar_diccionario({
        "persona": {"nombre": "Ana", "edad": 25},
        "ciudad": "Madrid"
    }) -> {"persona.nombre": "Ana", "persona.edad": 25, "ciudad": "Madrid"}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 18: Rotación de diccionario
# ============================================
def rotar_valores(diccionario):
    """
    Rota los valores del diccionario una posición a la derecha.
    Las claves permanecen igual, solo los valores rotan.
    
    Ejemplo:
    rotar_valores({"a": 1, "b": 2, "c": 3}) -> {"a": 3, "b": 1, "c": 2}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 19: Intersección de diccionarios
# ============================================
def interseccion_diccionarios(dict1, dict2):
    """
    Retorna un nuevo diccionario con solo las claves que están en ambos diccionarios.
    Usa los valores del primer diccionario.
    
    Ejemplo:
    interseccion_diccionarios({"a": 1, "b": 2, "c": 3}, {"b": 5, "c": 6, "d": 7}) 
    -> {"b": 2, "c": 3}
    """
    # Tu código aquí
    pass


# ============================================
# EJERCICIO 20: Sistema de inventario
# ============================================
def gestionar_inventario():
    """
    Crea un sistema simple de inventario con las siguientes funciones:
    
    1. Crear inventario inicial con al menos 3 productos (nombre: cantidad)
    2. Agregar 5 unidades a un producto existente
    3. Vender 3 unidades de otro producto (restar del inventario)
    4. Agregar un nuevo producto
    5. Eliminar un producto que llegó a 0
    6. Mostrar el inventario final
    
    Imprime cada paso.
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
    # print(contar_frecuencia("Hola Mundo"))
    
    # print("\nEjercicio 3:")
    # print(invertir_diccionario({"a": 1, "b": 2, "c": 3}))
    
    # print("\nEjercicio 4:")
    # print(fusionar_diccionarios({"a": 1, "b": 2}, {"b": 3, "c": 4}))
    
    # print("\nEjercicio 5:")
    # print(filtrar_mayores({"a": 5, "b": 10, "c": 3, "d": 8}, 5))
    
    # print("\nEjercicio 6:")
    # print(agrupar_por_longitud(["hola", "hi", "python", "go"]))
    
    # print("\nEjercicio 7:")
    # print(crear_diccionario_cuadrados(5))
    
    # print("\nEjercicio 8:")
    # print(encontrar_clave({"a": 1, "b": 2, "c": 3}, 2))
    
    # print("\nEjercicio 9:")
    # print(contar_palabras("Hola mundo. Hola Python."))
    
    # print("\nEjercicio 10:")
    # print(promedio_calificaciones({"Ana": [85, 90, 92], "Luis": [78, 85, 88]}))
    
    # print("\nEjercicio 11:")
    # print(crear_agenda())
    
    # print("\nEjercicio 13:")
    # print(clasificar_numeros([1, 2, 3, 4, 5, 6]))
    
    # print("\nEjercicio 14:")
    # print(eliminar_claves({"a": 1, "b": 2, "c": 3, "d": 4}, ["b", "d", "e"]))
    
    # print("\nEjercicio 15:")
    # print(crear_diccionario_desde_listas(["a", "b", "c"], [1, 2, 3]))
    
    # print("\nEjercicio 17:")
    # print(aplanar_diccionario({"persona": {"nombre": "Ana", "edad": 25}, "ciudad": "Madrid"}))
    
    # print("\nEjercicio 20:")
    # gestionar_inventario()
    
    print("\n¡Descomenta las pruebas para verificar tus soluciones!")
