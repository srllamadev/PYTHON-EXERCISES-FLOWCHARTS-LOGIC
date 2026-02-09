"""
WHILE LOOPS - Ejemplos Avanzados
=================================
Patrones más complejos con bucles while
"""

# Ejemplo 1: Búsqueda en lista
print("=== Ejemplo 1: Búsqueda en Lista ===")
numeros = [15, 23, 8, 42, 16, 4, 31]
objetivo = 42
indice = 0
encontrado = False

while indice < len(numeros) and not encontrado:
    if numeros[indice] == objetivo:
        encontrado = True
        print(f"Número {objetivo} encontrado en posición {indice}")
    indice += 1

if not encontrado:
    print(f"Número {objetivo} no encontrado")

print()

# Ejemplo 2: Fibonacci con while
print("=== Ejemplo 2: Serie Fibonacci ===")
n = 10  # cuántos números generar
a, b = 0, 1
contador = 0
fibonacci = []

while contador < n:
    fibonacci.append(a)
    a, b = b, a + b
    contador += 1

print(f"Primeros {n} números de Fibonacci: {fibonacci}")

print()

# Ejemplo 3: Adivina el número
print("=== Ejemplo 3: Juego Adivina el Número ===")
import random

numero_secreto = random.randint(1, 100)
adivinado = False
intentos_realizados = 0

print("¡Adivina el número entre 1 y 100!")

while not adivinado:
    try:
        intento = int(input("\nTu intento: "))
        intentos_realizados += 1
        
        if intento < numero_secreto:
            print("📈 Muy bajo, intenta con un número mayor")
        elif intento > numero_secreto:
            print("📉 Muy alto, intenta con un número menor")
        else:
            adivinado = True
            print(f"🎉 ¡Correcto! El número era {numero_secreto}")
            print(f"Lo lograste en {intentos_realizados} intentos")
    except ValueError:
        print("❌ Por favor ingresa un número válido")

print()

# Ejemplo 4: Simulación de cuenta bancaria
print("=== Ejemplo 4: Simulación Cuenta Bancaria ===")
saldo = 1000
continuar = True

while continuar:
    print(f"\n💰 Saldo actual: ${saldo:.2f}")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Ver saldo")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        monto = float(input("Monto a depositar: $"))
        if monto > 0:
            saldo += monto
            print(f"✅ Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("❌ El monto debe ser positivo")
    
    elif opcion == "2":
        monto = float(input("Monto a retirar: $"))
        if monto > 0:
            if monto <= saldo:
                saldo -= monto
                print(f"✅ Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            else:
                print("❌ Saldo insuficiente")
        else:
            print("❌ El monto debe ser positivo")
    
    elif opcion == "3":
        print(f"💵 Tu saldo es: ${saldo:.2f}")
    
    elif opcion == "4":
        continuar = False
        print("👋 Gracias por usar nuestros servicios")
    
    else:
        print("⚠️ Opción no válida")

print()

# Ejemplo 5: While anidados - Tabla de multiplicar
print("=== Ejemplo 5: While Anidados - Tablas de Multiplicar ===")
tabla = 1
while tabla <= 5:
    print(f"\n--- Tabla del {tabla} ---")
    multiplicador = 1
    while multiplicador <= 10:
        resultado = tabla * multiplicador
        print(f"{tabla} × {multiplicador} = {resultado}")
        multiplicador += 1
    tabla += 1
