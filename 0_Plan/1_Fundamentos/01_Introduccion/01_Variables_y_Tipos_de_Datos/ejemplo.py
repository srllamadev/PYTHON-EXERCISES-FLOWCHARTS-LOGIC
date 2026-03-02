"""
Ejemplos de Variables y Tipos de Datos en Python
==============================================

Este archivo contiene ejemplos ejecutables de los conceptos
básicos de variables y tipos de datos.
"""

# ============================================
# 1. TIPOS DE DATOS NUMÉRICOS
# ============================================
print("=" * 50)
print("1. TIPOS DE DATOS NUMÉRICOS")
print("=" * 50)

# Enteros (int)
edad = 25
año = 2024
temperatura = -10

print(f"Edad: {edad} (tipo: {type(edad)})")
print(f"Año: {año} (tipo: {type(año)})")
print(f"Temperatura: {temperatura}°C")

# Decimales (float)
altura = 1.75
precio = 99.99
pi = 3.14159

print(f"\nAltura: {altura}m (tipo: {type(altura)})")
print(f"Precio: ${precio}")
print(f"Pi: {pi}")

# Números complejos
complejo = 3 + 4j
print(f"\nNúmero complejo: {complejo} (tipo: {type(complejo)})")

# ============================================
# 2. CADENAS DE TEXTO (STRINGS)
# ============================================
print("\n" + "=" * 50)
print("2. CADENAS DE TEXTO (STRINGS)")
print("=" * 50)

nombre = "Juan"
apellido = 'Pérez'
mensaje = """Este es un mensaje
de múltiples líneas"""

print(f"Nombre: {nombre} (tipo: {type(nombre)})")
print(f"Apellido: {apellido}")
print(f"Mensaje:\n{mensaje}")

# Concatenación de strings
nombre_completo = nombre + " " + apellido
print(f"Nombre completo: {nombre_completo}")

# ============================================
# 3. BOOLEANOS
# ============================================
print("\n" + "=" * 50)
print("3. VALORES BOOLEANOS")
print("=" * 50)

es_estudiante = True
tiene_descuento = False
es_mayor_edad = edad >= 18

print(f"¿Es estudiante?: {es_estudiante} (tipo: {type(es_estudiante)})")
print(f"¿Tiene descuento?: {tiene_descuento}")
print(f"¿Es mayor de edad?: {es_mayor_edad}")

# ============================================
# 4. TIPO NONE
# ============================================
print("\n" + "=" * 50)
print("4. TIPO NONE (Ausencia de Valor)")
print("=" * 50)

resultado = None
print(f"Resultado: {resultado} (tipo: {type(resultado)})")

# ============================================
# 5. CONVERSIÓN DE TIPOS (CASTING)
# ============================================
print("\n" + "=" * 50)
print("5. CONVERSIÓN DE TIPOS (CASTING)")
print("=" * 50)

# String a número
edad_texto = "30"
edad_numero = int(edad_texto)
print(f"'{edad_texto}' convertido a int: {edad_numero}")

# Float a int (pierde decimales)
precio_decimal = 99.99
precio_entero = int(precio_decimal)
print(f"{precio_decimal} convertido a int: {precio_entero}")

# Número a string
numero = 42
numero_texto = str(numero)
print(f"{numero} convertido a string: '{numero_texto}'")

# String a float
altura_texto = "1.75"
altura_decimal = float(altura_texto)
print(f"'{altura_texto}' convertido a float: {altura_decimal}")

# ============================================
# 6. VERIFICACIÓN DE TIPOS
# ============================================
print("\n" + "=" * 50)
print("6. VERIFICACIÓN DE TIPOS")
print("=" * 50)

dato1 = 42
dato2 = "Python"
dato3 = 3.14
dato4 = True

print(f"type({dato1}): {type(dato1)}")
print(f"type('{dato2}'): {type(dato2)}")
print(f"type({dato3}): {type(dato3)}")
print(f"type({dato4}): {type(dato4)}")

# Verificar si es de un tipo específico
print(f"\n¿{dato1} es int?: {isinstance(dato1, int)}")
print(f"¿'{dato2}' es str?: {isinstance(dato2, str)}")
print(f"¿{dato3} es float?: {isinstance(dato3, float)}")

# ============================================
# 7. ASIGNACIÓN MÚLTIPLE
# ============================================
print("\n" + "=" * 50)
print("7. ASIGNACIÓN MÚLTIPLE")
print("=" * 50)

# Asignar múltiples variables en una línea
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

# Asignar el mismo valor a múltiples variables
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

# Intercambiar valores (swap)
antes_x, antes_y = x, y
x, y = y, x
print(f"Antes: x={antes_x}, y={antes_y}")
print(f"Después: x={x}, y={y}")

# ============================================
# 8. EJEMPLO PRÁCTICO: CALCULADORA DE IMC
# ============================================
print("\n" + "=" * 50)
print("8. EJEMPLO PRÁCTICO: CALCULADORA DE IMC")
print("=" * 50)

# Datos de ejemplo
peso = 70.5  # kg
altura_persona = 1.75  # metros

# Cálculo del IMC
imc = peso / (altura_persona ** 2)

print(f"Peso: {peso} kg")
print(f"Altura: {altura_persona} m")
print(f"IMC: {imc:.2f}")

# Interpretación básica
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Categoría: {categoria}")

# ============================================
# 9. CONSTANTES (POR CONVENCIÓN)
# ============================================
print("\n" + "=" * 50)
print("9. CONSTANTES (MAYÚSCULAS POR CONVENCIÓN)")
print("=" * 50)

PI = 3.14159
VELOCIDAD_LUZ = 299792458  # m/s
GRAVEDAD = 9.81  # m/s²

print(f"Pi: {PI}")
print(f"Velocidad de la luz: {VELOCIDAD_LUZ:,} m/s")
print(f"Gravedad: {GRAVEDAD} m/s²")

# ============================================
# 10. EJEMPLO FINAL: FICHA DE PERSONA
# ============================================
print("\n" + "=" * 50)
print("10. EJEMPLO FINAL: FICHA DE PERSONA")
print("=" * 50)

# Información personal
nombre_persona = "María García"
edad_persona = 28
altura_persona = 1.65
peso_persona = 60.0
es_empleado = True
salario = 3500.50

# Mostrar información formateada
print(f"""
╔══════════════════════════════════════╗
║      INFORMACIÓN PERSONAL            ║
╚══════════════════════════════════════╝

Nombre:      {nombre_persona}
Edad:        {edad_persona} años
Altura:      {altura_persona} m
Peso:        {peso_persona} kg
Empleado:    {"Sí" if es_empleado else "No"}
Salario:     ${salario:,.2f}

IMC:         {peso_persona / (altura_persona ** 2):.2f}
""")

print("\n" + "=" * 50)
print("FIN DE LOS EJEMPLOS")
print("=" * 50)
