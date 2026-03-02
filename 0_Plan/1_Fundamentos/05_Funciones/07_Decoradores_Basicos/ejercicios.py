"""
Ejercicios de Decoradores Básicos
===================================

Completa los ejercicios siguientes. Las soluciones están al final.
"""

from functools import wraps

print("=" * 60)
print("EJERCICIOS - DECORADORES BÁSICOS")
print("=" * 60)

# ============================================
# EJERCICIO 1: Decorador Simple
# ============================================
print("\nEJERCICIO 1: Decorador de Bienvenida")
print("-" * 60)
print("Crea un decorador 'agregar_bienvenida' que antes de ejecutar")
print("la función imprima '--- Inicio ---' y después '--- Fin ---'.")
print("Aplícalo a una función 'mostrar_info()' que imprima cualquier texto.")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 2: Decorador de Log
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Decorador de Log")
print("-" * 60)
print("Crea un decorador 'log_llamada' que imprima:")
print("  'Llamando a: <nombre_funcion> con args=(...) kwargs={...}'")
print("Antes de ejecutar cualquier función decorada.")
print("Aplícalo a 'sumar(a, b)' y 'saludar(nombre, saludo='Hola')'.")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 3: Decorador de Caché Simple
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Caché Simple")
print("-" * 60)
print("Crea un decorador 'cache_simple' que almacene los resultados")
print("ya calculados en un diccionario. Si la función ya fue llamada")
print("con los mismos argumentos, devuelve el resultado del cache")
print("sin volver a calcular.")
print("Pruébalo con: 'fibonacci(n)' calculado recursivamente.")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 4: Closure - Generador de Multiplicadores
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Closures")
print("-" * 60)
print("Crea una función 'crear_multiplicador(n)' que retorne una")
print("función que multiplica su argumento por n.")
print("Ejemplo:")
print("  doble  = crear_multiplicador(2)")
print("  triple = crear_multiplicador(3)")
print("  doble(5)   # 10")
print("  triple(5)  # 15")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 5: RETO - Decorador con Parámetros
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 5: RETO - Decorador con Parámetros")
print("-" * 60)
print("Crea un decorador 'reintentar(max_intentos=3)' que")
print("vuelva a ejecutar la función si lanza una excepción.")
print("Imprime un mensaje en cada reintento.")
print("Pruébalo con una función que falle aleatoriamente.")

import random

# TODO: Escribe tu código aquí
# Pista: usa try/except dentro del wrapper
# La función de prueba puede ser:
# def funcion_inestable():
#     if random.random() < 0.7:
#         raise ValueError("Fallo aleatorio")
#     return "¡Éxito!"




# ============================================
# SOLUCIONES
# ============================================
# def agregar_bienvenida(funcion):
#     @wraps(funcion)
#     def wrapper(*args, **kwargs):
#         print("--- Inicio ---")
#         resultado = funcion(*args, **kwargs)
#         print("--- Fin ---")
#         return resultado
#     return wrapper
#
# @agregar_bienvenida
# def mostrar_info():
#     print("Información del sistema")
#
# mostrar_info()
