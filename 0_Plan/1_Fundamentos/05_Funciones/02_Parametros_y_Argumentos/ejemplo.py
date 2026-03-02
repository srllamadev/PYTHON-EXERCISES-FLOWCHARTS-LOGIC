"""
Ejemplos de Parámetros y Argumentos
=====================================

Este archivo muestra los distintos tipos de parámetros
y cómo pasar argumentos al llamar funciones.
"""

# ============================================
# 1. PARÁMETROS POSICIONALES
# ============================================
print("=" * 50)
print("1. PARÁMETROS POSICIONALES")
print("=" * 50)

def presentar(nombre, edad, ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad:   {edad}")
    print(f"Ciudad: {ciudad}")
    print()

presentar("Ana", 28, "Madrid")
presentar("Carlos", 35, "Buenos Aires")
presentar("Lucía", 22, "Ciudad de México")

# ============================================
# 2. ARGUMENTOS POR NOMBRE (KEYWORD ARGUMENTS)
# ============================================
print("=" * 50)
print("2. KEYWORD ARGUMENTS")
print("=" * 50)

def crear_perfil(usuario, correo, rol):
    print(f"Usuario: {usuario} | Correo: {correo} | Rol: {rol}")

# El orden no importa cuando usamos el nombre del parámetro
crear_perfil("admin", "admin@mail.com", "Administrador")
crear_perfil(correo="user@mail.com", rol="Usuario", usuario="user01")

# ============================================
# 3. VALORES POR DEFECTO
# ============================================
print("\n" + "=" * 50)
print("3. VALORES POR DEFECTO")
print("=" * 50)

def saludar(nombre, saludo="Hola", puntuacion="!"):
    print(f"{saludo}, {nombre}{puntuacion}")

saludar("María")                         # Usa todos los valores por defecto
saludar("Pedro", "Buenos días")          # Cambia saludo
saludar("Juan", "Buenas noches", ".")    # Cambia todo
saludar("Ana", puntuacion="?")           # Cambia solo puntuacion

# ============================================
# 4. COMBINANDO POSICIONAL Y KEYWORD
# ============================================
print("\n" + "=" * 50)
print("4. COMBINANDO POSICIONAL Y KEYWORD")
print("=" * 50)

def calcular_precio(precio, descuento=0, impuesto=0.16):
    total = precio * (1 - descuento) * (1 + impuesto)
    print(f"Precio base:  ${precio:.2f}")
    print(f"Descuento:    {descuento*100:.0f}%")
    print(f"Impuesto:     {impuesto*100:.0f}%")
    print(f"Total:        ${total:.2f}")
    print()

calcular_precio(100)
calcular_precio(200, 0.10)
calcular_precio(500, descuento=0.20, impuesto=0.08)

# ============================================
# 5. PARÁMETROS EN FUNCIONES MATEMÁTICAS
# ============================================
print("=" * 50)
print("5. FUNCIONES MATEMÁTICAS CON PARÁMETROS")
print("=" * 50)

def area_rectangulo(base, altura):
    area = base * altura
    print(f"Área del rectángulo ({base} x {altura}): {area}")

def area_circulo(radio, pi=3.14159):
    area = pi * radio ** 2
    print(f"Área del círculo (r={radio}): {area:.4f}")

area_rectangulo(5, 3)
area_rectangulo(altura=7, base=4)
area_circulo(5)
area_circulo(5, pi=3.141592653589793)
