"""
Ejercicios de Variables y Tipos de Datos
========================================

Completa los ejercicios siguientes. Las soluciones están al final.
"""

print("=" * 60)
print("EJERCICIOS DE VARIABLES Y TIPOS DE DATOS")
print("=" * 60)

# ============================================
# EJERCICIO 1: Variables Básicas
# ============================================
print("\nEJERCICIO 1: Variables Básicas")
print("-" * 60)
print("Crea variables para almacenar tu información personal:")
print("- nombre (string)")
print("- edad (int)")
print("- altura en metros (float)")
print("- es_estudiante (bool)")
print("\nLuego imprime todos los valores con mensajes descriptivos.")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 2: Calculadora de IMC
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Calculadora de IMC")
print("-" * 60)
print("Crea variables para peso (kg) y altura (m),")
print("luego calcula el IMC usando la fórmula: IMC = peso / (altura ** 2)")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 3: Conversión de Tipos
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Conversión de Tipos")
print("-" * 60)
print("Convierte los siguientes valores:")
print("- '123' a int")
print("- 45.67 a int")
print("- 100 a string")
print("- '3.14' a float")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 4: Información de Producto
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Información de Producto")
print("-" * 60)
print("Crea variables para un producto:")
print("- nombre_producto (string)")
print("- precio (float)")
print("- cantidad_stock (int)")
print("- disponible (bool)")
print("\nImprime un resumen formateado.")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 5: Calculadora de Edad
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 5: Calculadora de Edad")
print("-" * 60)
print("Dado un año de nacimiento, calcula:")
print("- Edad actual")
print("- Edad en meses")
print("- Edad en días (aproximado: años * 365)")

año_nacimiento = 1995  # Modifica este valor

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 6: Swap de Variables
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 6: Intercambio de Variables")
print("-" * 60)
print("Intercambia los valores de dos variables sin usar una tercera.")

a = 10
b = 20

print(f"Antes: a = {a}, b = {b}")

# TODO: Intercambia los valores aquí



print(f"Después: a = {a}, b = {b}")




print("\n" + "=" * 60)
print("¡Revisa tus soluciones al final del archivo!")
print("=" * 60)


"""
═══════════════════════════════════════════════════════════
                    SOLUCIONES
═══════════════════════════════════════════════════════════

# SOLUCIÓN EJERCICIO 1:
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} m")
print(f"¿Es estudiante?: {es_estudiante}")


# SOLUCIÓN EJERCICIO 2:
peso = 70
altura = 1.75
imc = peso / (altura ** 2)
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")


# SOLUCIÓN EJERCICIO 3:
texto_a_int = int("123")
float_a_int = int(45.67)
int_a_texto = str(100)
texto_a_float = float("3.14")

print(f"'123' a int: {texto_a_int}")
print(f"45.67 a int: {float_a_int}")
print(f"100 a string: '{int_a_texto}'")
print(f"'3.14' a float: {texto_a_float}")


# SOLUCIÓN EJERCICIO 4:
nombre_producto = "Laptop"
precio = 1299.99
cantidad_stock = 15
disponible = True

print(f"Producto: {nombre_producto}")
print(f"Precio: ${precio}")
print(f"Stock: {cantidad_stock} unidades")
print(f"Disponible: {'Sí' if disponible else 'No'}")


# SOLUCIÓN EJERCICIO 5:
año_actual = 2024
año_nacimiento = 1995

edad = año_actual - año_nacimiento
edad_meses = edad * 12
edad_dias = edad * 365

print(f"Año de nacimiento: {año_nacimiento}")
print(f"Edad: {edad} años")
print(f"Edad en meses: {edad_meses}")
print(f"Edad en días: {edad_dias} (aproximado)")


# SOLUCIÓN EJERCICIO 6:
a = 10
b = 20
print(f"Antes: a = {a}, b = {b}")

# Método pythónico
a, b = b, a

print(f"Después: a = {a}, b = {b}")

"""
