"""
Formateo de Strings en Python
==============================

Ejemplos ejecutables de las tres formas de formatear strings:
  1. f-strings  (Python 3.6+) — Recomendado
  2. str.format()             — Clásico
  3. %-formatting             — Estilo antiguo
"""

# ============================================
# 1. F-STRINGS — BÁSICOS
# ============================================
print("=" * 55)
print("1. F-STRINGS — BÁSICOS")
print("=" * 55)

nombre = "Ana"
edad = 28
ciudad = "Madrid"

print(f"Hola, {nombre}. Tienes {edad} años y vives en {ciudad}.")

# Expresiones directas dentro de {}
a, b = 5, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} ** {b} = {a ** b}")
print(f"{'python'.upper()} es genial!")

# ============================================
# 2. F-STRINGS — ESPECIFICADORES NUMÉRICOS
# ============================================
print("\n" + "=" * 55)
print("2. F-STRINGS — ESPECIFICADORES NUMÉRICOS")
print("=" * 55)

pi = 3.141592653589793
ventas = 1234567.89
tasa = 0.1875

print(f"Pi (2 decimales):       {pi:.2f}")
print(f"Pi (5 decimales):       {pi:.5f}")
print(f"Pi (científico):        {pi:.3e}")
print(f"Ventas con comas:       {ventas:,.2f}")
print(f"Tasa como porcentaje:   {tasa:.1%}")
print(f"Entero con signo:       {42:+d}")
print(f"Entero con signo:       {-42:+d}")
print(f"Binario de 10:          {10:b}")
print(f"Octal de 8:             {8:o}")
print(f"Hex de 255:             {255:x}  (minúscula)")
print(f"Hex de 255:             {255:X}  (MAYÚSCULA)")
print(f"Con prefijo hex:        {255:#x}")

# ============================================
# 3. F-STRINGS — ALINEACIÓN Y RELLENO
# ============================================
print("\n" + "=" * 55)
print("3. F-STRINGS — ALINEACIÓN Y RELLENO")
print("=" * 55)

texto = "Python"
print(f"|{texto:<20}|  <- alineado a la izquierda (ancho 20)")
print(f"|{texto:>20}|  <- alineado a la derecha")
print(f"|{texto:^20}|  <- centrado")
print(f"|{texto:-^20}|  <- centrado con relleno '-'")
print(f"|{texto:*<20}|  <- relleno '*' a la derecha")

# Números con ancho fijo
for i in [1, 10, 100, 1000]:
    print(f"  Número: {i:6d}")

# Ceros a la izquierda
for i in range(1, 6):
    print(f"  Archivo_{i:03d}.txt")

# ============================================
# 4. F-STRINGS — TABLA DE DATOS REAL
# ============================================
print("\n" + "=" * 55)
print("4. F-STRINGS — TABLA DE DATOS")
print("=" * 55)

inventario = [
    ("Laptop Pro",    45,  1299.99),
    ("Mouse",        120,    29.95),
    ("Teclado",       88,    79.00),
    ("Monitor 27\"",  32,   449.50),
]

# Encabezado
print(f"{'Producto':<18} {'Stock':>6} {'Precio':>10} {'Total':>12}")
print("-" * 50)
for producto, stock, precio in inventario:
    total = stock * precio
    print(f"{producto:<18} {stock:>6} {precio:>10,.2f} {total:>12,.2f}")
print("-" * 50)
total_inv = sum(s * p for _, s, p in inventario)
print(f"{'TOTAL INVENTARIO':>36} {total_inv:>12,.2f}")

# ============================================
# 5. STR.FORMAT() — FORMA CLÁSICA
# ============================================
print("\n" + "=" * 55)
print("5. STR.FORMAT() — FORMA CLÁSICA")
print("=" * 55)

# Posicional
print("Hola, {}. Tienes {} años.".format("Luis", 35))

# Índices
print("{0} + {1} = {2}. También {1} + {0} = {2}".format(3, 4, 7))

# Nombres
plantilla = "Bienvenido, {nombre}. Tu saldo es {saldo:.2f}€."
print(plantilla.format(nombre="Carlos", saldo=1500.5))

# Desde un diccionario
datos = {"producto": "Café", "precio": 2.50, "cantidad": 3}
print("Factura: {cantidad}x {producto} a {precio:.2f}€ = {total:.2f}€".format(
    total=datos["precio"] * datos["cantidad"],
    **datos
))

# ============================================
# 6. %-FORMATTING — ESTILO ANTIGUO
# ============================================
print("\n" + "=" * 55)
print("6. %-FORMATTING — ESTILO ANTIGUO")
print("=" * 55)

nombre = "Pedro"
nota = 9.25
print("El estudiante %s obtuvo una nota de %.1f" % (nombre, nota))
print("Hay %d manzanas y %d naranjas." % (5, 3))
print("El valor en hex es: %x" % 255)

# ============================================
# 7. F-STRINGS AVANZADOS (Python 3.8+: self-documenting)
# ============================================
print("\n" + "=" * 55)
print("7. F-STRINGS AVANZADOS (Python 3.8+)")
print("=" * 55)

x = 42
y = 3.14
lista = [1, 2, 3]

# {variable=} imprime el nombre y el valor (debugging)
print(f"{x=}")
print(f"{y=:.2f}")
print(f"{lista=}")
print(f"{x * 2 + 1=}")

# Formateo condicional
for nota in [10, 7, 4]:
    estado = "Aprobado" if nota >= 5 else "Reprobado"
    emoji = "✅" if nota >= 5 else "❌"
    print(f"Nota: {nota:2d} | {estado} {emoji}")
