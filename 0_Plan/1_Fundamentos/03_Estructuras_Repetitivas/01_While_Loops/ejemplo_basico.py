"""
WHILE LOOPS - Ejemplos Básicos
================================
Ejemplos fundamentales del uso de bucles while
"""

# Ejemplo 1: Contador simple
print("=== Ejemplo 1: Contador Simple ===")
contador = 1
while contador <= 5:
    print(f"Iteración {contador}")
    contador += 1

print()

# Ejemplo 2: Suma acumulativa
print("=== Ejemplo 2: Suma Acumulativa ===")
suma = 0
numero = 1
while numero <= 10:
    suma += numero
    numero += 1
print(f"La suma de 1 a 10 es: {suma}")

print()

# Ejemplo 3: Validación de entrada
print("=== Ejemplo 3: Validación de Entrada ===")
password_correcto = "python123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    password = input("Ingresa la contraseña: ")
    if password == password_correcto:
        print("¡Acceso concedido!")
        break
    else:
        intentos += 1
        if intentos < max_intentos:
            print(f"Contraseña incorrecta. Te quedan {max_intentos - intentos} intentos")
        else:
            print("Has agotado tus intentos. Acceso denegado.")

print()

# Ejemplo 4: Menu interactivo
print("=== Ejemplo 4: Menú Interactivo ===")
opcion = ""
while opcion != "4":
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Mostrar fecha")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("¿Cómo te llamas? ")
        print(f"¡Hola {nombre}! Bienvenido/a")
    elif opcion == "2":
        print("¡Hasta pronto!")
    elif opcion == "3":
        from datetime import date
        print(f"Hoy es: {date.today()}")
    elif opcion == "4":
        print("Cerrando programa...")
    else:
        print("Opción no válida")

print()

# Ejemplo 5: While con bandera (flag)
print("=== Ejemplo 5: While con Bandera ===")
activo = True
puntos = 0

while activo:
    print(f"\nPuntos actuales: {puntos}")
    accion = input("¿Quieres sumar puntos? (s/n): ").lower()
    
    if accion == 's':
        puntos += 10
        print("+10 puntos!")
    elif accion == 'n':
        activo = False
        print(f"Juego terminado. Puntos finales: {puntos}")
    else:
        print("Respuesta no válida")
