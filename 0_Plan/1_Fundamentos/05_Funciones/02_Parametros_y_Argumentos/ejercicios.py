"""
Ejercicios de Parámetros y Argumentos
=======================================

Completa los ejercicios siguientes. Las soluciones están al final.
"""

print("=" * 60)
print("EJERCICIOS - PARÁMETROS Y ARGUMENTOS")
print("=" * 60)

# ============================================
# EJERCICIO 1: Función de Bienvenida
# ============================================
print("\nEJERCICIO 1: Función de Bienvenida")
print("-" * 60)
print("Crea 'bienvenida(nombre, idioma)' que imprima:")
print("  - Si idioma='es' -> 'Hola, {nombre}!'")
print("  - Si idioma='en' -> 'Hello, {nombre}!'")
print("  - Si idioma='fr' -> 'Bonjour, {nombre}!'")
print("Con valor por defecto idioma='es'.")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 2: Calculadora de Geometría
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Calculadora de Geometría")
print("-" * 60)
print("Crea 'area_triangulo(base, altura)' que calcule")
print("e imprima el área de un triángulo.")
print("Llámala con distintos argumentos posicionales y por nombre.")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 3: Perfil de Usuario
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Perfil de Usuario")
print("-" * 60)
print("Crea 'crear_usuario(nombre, apellido, edad, activo=True)'")
print("que imprima un perfil formateado. Pruébala:")
print("  - Solo con nombre y apellido (resto por defecto)")
print("  - Con todos los argumentos por nombre")
print("  - Con activo=False")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 4: Convertidor de Temperatura
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Convertidor de Temperatura")
print("-" * 60)
print("Crea 'convertir_temp(valor, de_unidad='C', a_unidad='F')'")
print("Fórmulas:")
print("  C -> F: (C * 9/5) + 32")
print("  F -> C: (F - 32) * 5/9")
print("  C -> K: C + 273.15")

# TODO: Escribe tu código aquí




# ============================================
# SOLUCIONES
# ============================================
# def bienvenida(nombre, idioma='es'):
#     if idioma == 'es':
#         print(f"¡Hola, {nombre}!")
#     elif idioma == 'en':
#         print(f"Hello, {nombre}!")
#     elif idioma == 'fr':
#         print(f"Bonjour, {nombre}!")
#
# bienvenida("Ana")
# bienvenida("Ana", idioma="en")
# bienvenida("Ana", "fr")
