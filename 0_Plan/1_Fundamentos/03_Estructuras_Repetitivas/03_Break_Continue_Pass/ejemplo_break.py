"""
BREAK - Ejemplos
================
Ejemplos de uso de la sentencia break
"""

# Ejemplo 1: Búsqueda simple
print("=== Ejemplo 1: Búsqueda en Lista ===")
numeros = [3, 7, 2, 9, 4, 1, 8]
objetivo = 9

for i, num in enumerate(numeros):
    print(f"Buscando... índice {i}: valor {num}")
    if num == objetivo:
        print(f"¡Encontrado! {objetivo} está en el índice {i}")
        break
else:
    print(f"{objetivo} no se encontró en la lista")

print()

# Ejemplo 2: Validación de contraseña con límite de intentos
print("=== Ejemplo 2: Sistema de Login ===")
password_correcta = "python123"
max_intentos = 3

for intento in range(1, max_intentos + 1):
    print(f"\nIntento {intento} de {max_intentos}")
    password = input("Ingresa la contraseña: ")
    
    if password == password_correcta:
        print("✅ ¡Acceso concedido!")
        break
    else:
        if intento < max_intentos:
            print(f"❌ Contraseña incorrecta. Te quedan {max_intentos - intento} intentos")
        else:
            print("❌ Has agotado tus intentos")

print()

# Ejemplo 3: Detener cuando se alcanza un límite
print("=== Ejemplo 3: Suma hasta Límite ===")
numeros = [5, 10, 15, 20, 25, 30, 35]
limite = 50
suma = 0

print(f"Sumando números hasta alcanzar {limite}:")
for num in numeros:
    if suma + num > limite:
        print(f"\n🛑 Detenido: agregar {num} excedería el límite")
        print(f"   {suma} + {num} = {suma + num} > {limite}")
        break
    
    suma += num
    print(f"Sumando {num}: total = {suma}")

print(f"\nSuma final: {suma}")

print()

# Ejemplo 4: Búsqueda en texto
print("=== Ejemplo 4: Buscar Palabra en Texto ===")
texto = "Python es un lenguaje de programación muy popular"
palabras = texto.split()
palabra_buscar = "lenguaje"

for i, palabra in enumerate(palabras):
    if palabra == palabra_buscar:
        print(f"'{palabra_buscar}' encontrada en la posición {i}")
        print(f"Contexto: ...{' '.join(palabras[max(0,i-1):i+2])}...")
        break
else:
    print(f"'{palabra_buscar}' no encontrada")

print()

# Ejemplo 5: Salir de bucle anidado con bandera
print("=== Ejemplo 5: Búsqueda en Matriz ===")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
buscar = 5
encontrado = False

for i, fila in enumerate(matriz):
    for j, valor in enumerate(fila):
        if valor == buscar:
            print(f"Valor {buscar} encontrado en posición [{i}][{j}]")
            encontrado = True
            break
    if encontrado:
        break
else:
    print(f"Valor {buscar} no encontrado")

print()

# Ejemplo 6: Validar entrada hasta que sea correcta
print("=== Ejemplo 6: Validación de Entrada ===")
opciones_validas = ['1', '2', '3', 'salir']

for _ in range(5):  # Máximo 5 intentos
    opcion = input("Elige una opción (1, 2, 3, o 'salir'): ")
    
    if opcion in opciones_validas:
        if opcion == 'salir':
            print("👋 Saliendo del programa")
        else:
            print(f"✅ Opción {opcion} seleccionada")
        break
    else:
        print("❌ Opción no válida, intenta nuevamente")
else:
    print("⚠️ Demasiados intentos fallidos")

print()

# Ejemplo 7: Procesamiento hasta encontrar marca
print("=== Ejemplo 7: Lectura hasta Marca de Fin ===")
datos = [10, 20, 30, "FIN", 40, 50, 60]
suma_datos = 0

print("Procesando datos hasta encontrar 'FIN':")
for dato in datos:
    if dato == "FIN":
        print(f"🛑 Marca 'FIN' encontrada. Deteniendo procesamiento.")
        break
    
    if isinstance(dato, int):
        suma_datos += dato
        print(f"  Procesando: {dato}, suma parcial: {suma_datos}")

print(f"\nSuma total: {suma_datos}")

print()

# Ejemplo 8: Juego - Adivina el número con break
print("=== Ejemplo 8: Adivina el Número (3 intentos) ===")
import random

numero_secreto = random.randint(1, 20)
intentos_max = 3

print("Adivina el número entre 1 y 20")

for intento in range(1, intentos_max + 1):
    try:
        adivinanza = int(input(f"\nIntento {intento}: "))
        
        if adivinanza == numero_secreto:
            print(f"🎉 ¡CORRECTO! El número era {numero_secreto}")
            print(f"Lo lograste en {intento} intento(s)")
            break
        elif adivinanza < numero_secreto:
            print("📈 Muy bajo")
        else:
            print("📉 Muy alto")
            
    except ValueError:
        print("❌ Por favor ingresa un número válido")
else:
    print(f"\n😞 Se acabaron los intentos. El número era {numero_secreto}")
