"""
Ejercicios de Scope
====================

Completa los ejercicios siguientes. Las soluciones están al final.
"""

print("=" * 60)
print("EJERCICIOS - SCOPE (ALCANCE DE VARIABLES)")
print("=" * 60)

# ============================================
# EJERCICIO 1: Identificar el Scope
# ============================================
print("\nEJERCICIO 1: Identificar Output")
print("-" * 60)
print("¿Cuál es la salida de este código? Razona antes de correrlo:")
print()
print("  a = 'global'")
print("  def funcion():")
print("      a = 'local'")
print("      print(a)")
print("  funcion()")
print("  print(a)")
print()
print("Escribe tu respuesta como comentario, luego verifica:")

# TODO: Ejecuta el código y verifica tu respuesta
a = 'global'
def funcion():
    a = 'local'
    print(a)
funcion()
print(a)


# ============================================
# EJERCICIO 2: Arreglar el Bug de Scope
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Arregla el Bug")
print("-" * 60)
print("El siguiente código tiene un bug de scope.")
print("Arréglalo sin usar 'global':")
print()

# CÓDIGO BUGGY:
# total = 0
# def agregar(valor):
#     total += valor   # UnboundLocalError!
#
# agregar(10)
# agregar(20)
# print(total)

# TODO: Escribe la versión corregida usando return




# ============================================
# EJERCICIO 3: Acumulador con nonlocal
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Acumulador con nonlocal")
print("-" * 60)
print("Crea una función 'crear_acumulador()' que retorne una función")
print("interior 'agregar(n)' que acumule valores usando nonlocal.")
print("Ejemplo:")
print("  acc = crear_acumulador()")
print("  acc(10)  # retorna 10")
print("  acc(5)   # retorna 15")
print("  acc(20)  # retorna 35")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 4: Regla LEGB
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Trazar LEGB")
print("-" * 60)
print("Crea un ejemplo de 3 funciones anidadas donde cada nivel")
print("tenga una variable 'nivel' con valores distintos.")
print("Imprime el valor de 'nivel' en cada función.")

# TODO: Escribe tu código aquí




# ============================================
# SOLUCIONES
# ============================================
# EJERCICIO 2:
# def agregar(total, valor):
#     return total + valor
#
# total = 0
# total = agregar(total, 10)
# total = agregar(total, 20)
# print(total)   # 30
