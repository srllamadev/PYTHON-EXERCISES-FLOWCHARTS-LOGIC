"""
CONTINUE - Ejemplos
===================
Ejemplos de uso de la sentencia continue
"""

# Ejemplo 1: Saltar números pares
print("=== Ejemplo 1: Imprimir Solo Impares ===")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Salta los números pares
    print(f"Número impar: {num}")

print()

# Ejemplo 2: Filtrar elementos no válidos
print("=== Ejemplo 2: Procesar Solo Números Positivos ===")
numeros = [5, -2, 10, -7, 3, 0, 8, -1]

suma_positivos = 0
for num in numeros:
    if num <= 0:
        print(f"⏭️  Saltando {num} (no positivo)")
        continue
    
    suma_positivos += num
    print(f"✅ Sumando {num}, total: {suma_positivos}")

print(f"\nSuma de positivos: {suma_positivos}")

print()

# Ejemplo 3: Saltar elementos vacíos
print("=== Ejemplo 3: Procesar Solo Strings No Vacíos ===")
palabras = ["Python", "", "Java", "  ", "C++", "", "Rust"]

for palabra in palabras:
    if not palabra.strip():  # Si está vacío o solo espacios
        continue
    
    print(f"Palabra: {palabra} (longitud: {len(palabra)})")

print()

# Ejemplo 4: Validación de datos
print("=== Ejemplo 4: Validar y Procesar Edades ===")
edades = [25, -5, 30, 150, 18, 0, 45, 200]

print("Edades válidas (entre 1 y 120):")
for edad in edades:
    if edad < 1 or edad > 120:
        print(f"  ⚠️  {edad} - INVÁLIDA (saltada)")
        continue
    
    categoria = "Menor" if edad < 18 else "Adulto"
    print(f"  ✅ {edad} años - {categoria}")

print()

# Ejemplo 5: Procesar solo ciertos tipos de archivos
print("=== Ejemplo 5: Filtrar Archivos Python ===")
archivos = ["script.py", "datos.txt", "main.py", "imagen.jpg", "test.py", "config.ini"]

print("Archivos Python encontrados:")
for archivo in archivos:
    if not archivo.endswith('.py'):
        continue
    
    nombre = archivo[:-3]  # Quitar extensión
    print(f"  📄 {archivo} → nombre: {nombre}")

print()

# Ejemplo 6: Saltar divisiones por cero
print("=== Ejemplo 6: Cálculos Seguros (Evitar División por Cero) ===")
dividendos = [100, 50, 200, 75]
divisores = [5, 0, 10, 0]

print("Resultados de divisiones:")
for dividendo, divisor in zip(dividendos, divisores):
    if divisor == 0:
        print(f"  ⚠️  {dividendo} ÷ {divisor} → SALTADO (división por cero)")
        continue
    
    resultado = dividendo / divisor
    print(f"  ✅ {dividendo} ÷ {divisor} = {resultado}")

print()

# Ejemplo 7: Procesar solo usuarios activos
print("=== Ejemplo 7: Filtrar Usuarios Activos ===")
usuarios = [
    {"nombre": "Ana", "activo": True, "edad": 25},
    {"nombre": "Luis", "activo": False, "edad": 30},
    {"nombre": "María", "activo": True, "edad": 28},
    {"nombre": "Carlos", "activo": False, "edad": 35}
]

print("Usuarios activos:")
for usuario in usuarios:
    if not usuario["activo"]:
        continue
    
    print(f"  👤 {usuario['nombre']} - {usuario['edad']} años")

print()

# Ejemplo 8: Saltar comentarios en procesamiento de texto
print("=== Ejemplo 8: Procesar Código (Saltar Comentarios) ===")
lineas_codigo = [
    "x = 10",
    "# Este es un comentario",
    "y = 20",
    "# Otro comentario",
    "z = x + y",
    "print(z)"
]

print("Código ejecutable (sin comentarios):")
linea_num = 1
for linea in lineas_codigo:
    if linea.strip().startswith('#'):
        continue
    
    print(f"  {linea_num}. {linea}")
    linea_num += 1

print()

# Ejemplo 9: Procesar transacciones válidas
print("=== Ejemplo 9: Validar Transacciones Bancarias ===")
transacciones = [
    {"tipo": "deposito", "monto": 100},
    {"tipo": "retiro", "monto": -50},  # Monto negativo (inválido)
    {"tipo": "deposito", "monto": 200},
    {"tipo": "transferencia", "monto": 0},  # Monto cero (inválido)
    {"tipo": "retiro", "monto": 30}
]

saldo = 1000
print(f"Saldo inicial: ${saldo}")

for trans in transacciones:
    tipo = trans["tipo"]
    monto = trans["monto"]
    
    # Validaciones
    if monto <= 0:
        print(f"  ❌ {tipo.capitalize()} de ${monto} - INVÁLIDO (saltado)")
        continue
    
    if tipo == "deposito":
        saldo += monto
        print(f"  ✅ Depósito: +${monto} → Saldo: ${saldo}")
    elif tipo == "retiro":
        if monto > saldo:
            print(f"  ❌ Retiro de ${monto} - SALDO INSUFICIENTE (saltado)")
            continue
        saldo -= monto
        print(f"  ✅ Retiro: -${monto} → Saldo: ${saldo}")

print(f"\nSaldo final: ${saldo}")

print()

# Ejemplo 10: Combo - Continue con enumerate
print("=== Ejemplo 10: Procesar Lista con Índices ===")
tareas = ["Estudiar", "", "Hacer ejercicio", "  ", "Leer libro", "Cocinar"]

print("Tareas válidas:")
for i, tarea in enumerate(tareas, start=1):
    if not tarea.strip():
        print(f"  {i}. [VACÍO - saltado]")
        continue
    
    print(f"  {i}. {tarea} ✓")
