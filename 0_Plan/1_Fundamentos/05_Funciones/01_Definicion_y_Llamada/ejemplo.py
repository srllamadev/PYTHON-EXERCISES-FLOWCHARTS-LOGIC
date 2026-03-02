"""
Ejemplos de Definición y Llamada de Funciones
==============================================

Este archivo contiene ejemplos ejecutables sobre cómo
definir y llamar funciones en Python.
"""

# ============================================
# 1. FUNCIÓN MÁS SIMPLE
# ============================================
print("=" * 50)
print("1. FUNCIÓN MÁS SIMPLE")
print("=" * 50)

def saludar():
    print("¡Hola, mundo!")

# Llamada a la función
saludar()
saludar()  # Se puede llamar múltiples veces
saludar()

# ============================================
# 2. FUNCIÓN CON VARIAS INSTRUCCIONES
# ============================================
print("\n" + "=" * 50)
print("2. FUNCIÓN CON VARIAS INSTRUCCIONES")
print("=" * 50)

def mostrar_menu():
    print("--- MENÚ PRINCIPAL ---")
    print("1. Nueva partida")
    print("2. Cargar partida")
    print("3. Opciones")
    print("4. Salir")
    print("----------------------")

mostrar_menu()

# ============================================
# 3. ORDEN IMPORTA: DEFINIR ANTES DE LLAMAR
# ============================================
print("\n" + "=" * 50)
print("3. ORDEN DE DEFINICIÓN")
print("=" * 50)

def presentarse():
    print("Soy una función definida correctamente.")
    print("Fui definida ANTES de ser llamada.")

# Correcto: llamar después de definir
presentarse()

# ============================================
# 4. FUNCIONES DESCRIBEN UN PROCESO
# ============================================
print("\n" + "=" * 50)
print("4. FUNCIÓN QUE DESCRIBE UN PROCESO")
print("=" * 50)

def preparar_cafe():
    print("Proceso: Preparar un café")
    print("  1. Hervir agua")
    print("  2. Colocar filtro en la cafetera")
    print("  3. Agregar café molido")
    print("  4. Verter agua caliente")
    print("  5. Esperar 4 minutos")
    print("  6. ¡Café listo!")

preparar_cafe()

# ============================================
# 5. REUTILIZACIÓN DE FUNCIONES
# ============================================
print("\n" + "=" * 50)
print("5. REUTILIZACIÓN DE CÓDIGO")
print("=" * 50)

def separador():
    print("-" * 30)

# Sin funciones habríamos escrito print("-"*30) muchas veces
separador()
print("Sección A")
separador()
print("Sección B")
separador()
print("Sección C")
separador()

# ============================================
# 6. FUNCIONES QUE LLAMAN A OTRAS FUNCIONES
# ============================================
print("\n" + "=" * 50)
print("6. FUNCIONES QUE LLAMAN A OTRAS FUNCIONES")
print("=" * 50)

def bienvenida():
    print("¡Bienvenido al programa!")

def despedida():
    print("¡Hasta pronto!")

def ejecutar_programa():
    bienvenida()
    print("  ... realizando tareas ...")
    despedida()

ejecutar_programa()
