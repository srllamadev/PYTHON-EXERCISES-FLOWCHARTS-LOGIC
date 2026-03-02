"""
Ejemplos de Input/Output en Python
===================================

Este archivo contiene ejemplos ejecutables de entrada y salida
de datos, formateo de texto y conversión de tipos.
"""

# ============================================
# 1. FUNCIÓN PRINT BÁSICA
# ============================================
print("=" * 60)
print("1. FUNCIÓN PRINT BÁSICA")
print("=" * 60)

print("Hola Mundo")
print(42)
print(3.14159)
print(True)
print([1, 2, 3, 4, 5])

# Imprimir múltiples valores
nombre = "Juan"
edad = 25
print("Nombre:", nombre, "- Edad:", edad)

# ============================================
# 2. PARÁMETROS DE PRINT
# ============================================
print("\n" + "=" * 60)
print("2. PARÁMETROS DE PRINT (sep y end)")
print("=" * 60)

# Parámetro sep (separador)
print("Python", "Java", "C++", sep=" | ")
print("2024", "01", "29", sep="-")
print("Ruta:", "carpeta1", "carpeta2", "archivo.txt", sep="/")

# Parámetro end (final de línea)
print("\nImprimiendo en la misma línea:")
print("Cargando", end="...")
print("50%", end="...")
print("Completado!")

print("\nNúmeros en fila:")
for i in range(1, 6):
    print(i, end=" ")
print()  # Nueva línea al final

# ============================================
# 3. CARACTERES ESPECIALES
# ============================================
print("\n" + "=" * 60)
print("3. CARACTERES ESPECIALES")
print("=" * 60)

print("Línea 1\nLínea 2\nLínea 3")  # \n = nueva línea
print("\nColumna1\tColumna2\tColumna3")  # \t = tabulación
print("Texto \"entre comillas\"")  # \" = comilla escapada
print("Ruta de Windows: C:\\Users\\Documents")  # \\ = barra invertida

# ============================================
# 4. FORMATEO CON F-STRINGS (Recomendado)
# ============================================
print("\n" + "=" * 60)
print("4. FORMATEO CON F-STRINGS")
print("=" * 60)

nombre = "María"
edad = 28
altura = 1.65
salario = 3500.75

# Básico
print(f"Me llamo {nombre} y tengo {edad} años")

# Con expresiones
print(f"El año que viene tendré {edad + 1} años")
print(f"Mi altura al cuadrado es {altura ** 2:.4f}")

# Formateo de números
precio = 1234.56789
print(f"\nPrecio: ${precio:.2f}")  # 2 decimales
print(f"Precio: ${precio:,.2f}")  # Con separador de miles
print(f"Salario: ${salario:>10,.2f}")  # Alineado a la derecha

# Alineación
print(f"\n{'Izquierda':<15}|")
print(f"{'Centro':^15}|")
print(f"{'Derecha':>15}|")

# Relleno con caracteres
titulo = "Python"
print(f"\n{titulo:*^30}")
print(f"{titulo:-^30}")
print(f"{titulo:=^30}")

# ============================================
# 5. MÉTODO .format()
# ============================================
print("\n" + "=" * 60)
print("5. MÉTODO .format()")
print("=" * 60)

# Básico
mensaje = "Me llamo {} y tengo {} años".format("Carlos", 30)
print(mensaje)

# Con índices
mensaje = "{0} {1} tiene {2} años. {1} vive en {3}".format(
    "El señor", "Pérez", 45, "Madrid"
)
print(mensaje)

# Con nombres
mensaje = "Me llamo {nombre} {apellido} y tengo {edad} años".format(
    nombre="Ana",
    apellido="López",
    edad=25
)
print(mensaje)

# ============================================
# 6. FUNCIÓN INPUT
# ============================================
print("\n" + "=" * 60)
print("6. FUNCIÓN INPUT (Entrada de Datos)")
print("=" * 60)

print("NOTA: Los ejemplos de input están comentados.")
print("Descomenta para probar interactivamente.\n")

# Ejemplo básico (comentado)
# nombre_usuario = input("¿Cómo te llamas? ")
# print(f"Hola {nombre_usuario}!")

# Ejemplo con conversión de tipos
print("Ejemplo de conversión:")
print("  edad_texto = input('¿Cuántos años tienes? ')")
print("  edad = int(edad_texto)")
print("  print(f'Tienes {edad} años')")

# ============================================
# 7. EJEMPLO PRÁCTICO: TABLA FORMATEADA
# ============================================
print("\n" + "=" * 60)
print("7. EJEMPLO: TABLA DE PRODUCTOS")
print("=" * 60)

# Encabezado
print(f"{'Producto':<20} {'Precio':>10} {'Stock':>8} {'Total':>12}")
print("-" * 52)

# Datos
productos = [
    ("Laptop", 1299.99, 5),
    ("Mouse", 29.99, 150),
    ("Teclado", 79.99, 45),
    ("Monitor", 399.99, 12)
]

for producto, precio, stock in productos:
    total = precio * stock
    print(f"{producto:<20} ${precio:>9.2f} {stock:>8} ${total:>11.2f}")

# Total general
total_inventario = sum(p * s for _, p, s in productos)
print("-" * 52)
print(f"{'TOTAL':>40} ${total_inventario:>11.2f}")

# ============================================
# 8. EJEMPLO: RECIBO DE COMPRA
# ============================================
print("\n" + "=" * 60)
print("8. EJEMPLO: RECIBO DE COMPRA")
print("=" * 60)

producto = "Laptop Gaming"
precio_unitario = 1299.99
cantidad = 2
subtotal = precio_unitario * cantidad
iva = subtotal * 0.16
total = subtotal + iva

print(f"""
╔════════════════════════════════════════════╗
║          RECIBO DE COMPRA                  ║
╚════════════════════════════════════════════╝

Producto:       {producto}
Precio unit.:   ${precio_unitario:,.2f}
Cantidad:       {cantidad}
              ──────────────
Subtotal:       ${subtotal:,.2f}
IVA (16%):      ${iva:,.2f}
              ══════════════
TOTAL:          ${total:,.2f}

        ¡Gracias por su compra!
""")

# ============================================
# 9. EJEMPLO: FICHA DE ESTUDIANTE
# ============================================
print("\n" + "=" * 60)
print("9. EJEMPLO: FICHA DE ESTUDIANTE")
print("=" * 60)

estudiante = "Ana García"
matricula = "2024-001"
carrera = "Ingeniería en Sistemas"
calificaciones = [9.5, 8.7, 9.0, 8.5, 9.2]
promedio = sum(calificaciones) / len(calificaciones)

print(f"""
{'═' * 50}
           FICHA DE ESTUDIANTE
{'═' * 50}

Nombre:        {estudiante}
Matrícula:     {matricula}
Carrera:       {carrera}

CALIFICACIONES:
{'-' * 50}
""")

for i, calif in enumerate(calificaciones, 1):
    print(f"   Materia {i}:     {calif:.1f}")

print(f"""
{'-' * 50}
   PROMEDIO:     {promedio:.2f}
{'═' * 50}
""")

# ============================================
# 10. EJEMPLO: CONVERSIÓN DE UNIDADES
# ============================================
print("\n" + "=" * 60)
print("10. EJEMPLO: CONVERSIÓN DE TEMPERATURAS")
print("=" * 60)

celsius = 25
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

print(f"Temperatura: {celsius}°C")
print(f"  → Fahrenheit: {fahrenheit:.2f}°F")
print(f"  → Kelvin:     {kelvin:.2f}K")

# Tabla de conversiones
print(f"\n{'Celsius':>10} {'Fahrenheit':>12} {'Kelvin':>10}")
print("-" * 34)
for c in [0, 10, 20, 25, 30, 100]:
    f = c * 9/5 + 32
    k = c + 273.15
    print(f"{c:>10}°C {f:>12.1f}°F {k:>10.2f}K")

# ============================================
# 11. EJEMPLO: BARRA DE PROGRESO
# ============================================
print("\n" + "=" * 60)
print("11. EJEMPLO: BARRA DE PROGRESO")
print("=" * 60)

import time

print("\nCargando archivos...")
for porcentaje in range(0, 101, 10):
    barra = "█" * (porcentaje // 10) + "░" * (10 - porcentaje // 10)
    print(f"\r[{barra}] {porcentaje}%", end="")
    time.sleep(0.1)

print("\n¡Completado!")

# ============================================
# 12. EJEMPLO: FORMATEO AVANZADO
# ============================================
print("\n" + "=" * 60)
print("12. EJEMPLOS DE FORMATEO AVANZADO")
print("=" * 60)

# Números con formato
numero = 1234567.89
print(f"Original:       {numero}")
print(f"Con comas:      {numero:,}")
print(f"2 decimales:    {numero:.2f}")
print(f"Científico:     {numero:e}")
print(f"Porcentaje:     {0.856:.1%}")

# Fechas (usando formato manual)
dia, mes, año = 29, 1, 2024
print(f"\nFecha: {dia:02d}/{mes:02d}/{año}")

# Binario, octal, hexadecimal
num = 42
print(f"\nNúmero: {num}")
print(f"Binario:        {num:b}")
print(f"Octal:          {num:o}")
print(f"Hexadecimal:    {num:x}")
print(f"Hexadecimal:    {num:X}")

# Relleno con ceros
numero = 7
print(f"\n{numero:05d}")  # 00007

print("\n" + "=" * 60)
print("FIN DE LOS EJEMPLOS")
print("=" * 60)

# ============================================
# SECCIÓN INTERACTIVA (DESCOMENTA PARA USAR)
# ============================================
"""
print("\n" + "=" * 60)
print("SECCIÓN INTERACTIVA")
print("=" * 60)

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
ciudad = input("¿De dónde eres? ")

print(f"\n{'=' * 40}")
print(f"Hola {nombre}!")
print(f"Tienes {edad} años y vives en {ciudad}")
print(f"{'=' * 40}")
"""
