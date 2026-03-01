"""
Ejercicios - Formateo de Strings
==================================

Practica el uso de f-strings, str.format() y especificadores de formato.
"""

print("=" * 60)
print("EJERCICIOS - FORMATEO DE STRINGS")
print("=" * 60)

# ============================================
# EJERCICIO 1: Recibo de compra
# ============================================
print("\nEJERCICIO 1: Recibo de compra")
print("-" * 60)
print("""
Genera un recibo con los siguientes datos:
  items = [("Café", 2.50, 2), ("Croissant", 1.80, 3), ("Zumo", 3.20, 1)]

Formato esperado:
------------------------------------------
           CAFETERÍA PYTHON
------------------------------------------
  Café             x2        5.00€
  Croissant        x3        5.40€
  Zumo             x1        3.20€
------------------------------------------
  SUBTOTAL:                 13.60€
  IVA (10%):                 1.36€
  TOTAL:                    14.96€
------------------------------------------

Usa f-strings con especificadores de ancho.
""")

items = [("Café", 2.50, 2), ("Croissant", 1.80, 3), ("Zumo", 3.20, 1)]

# TODO: Escribe tu código aquí


# ============================================
# EJERCICIO 2: Informe de notas
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Informe de notas")
print("-" * 60)
print("""
Dado el siguiente diccionario de notas:
notas = {"Ana": 9.3, "Luis": 6.7, "Marta": 8.5, "Pedro": 4.2, "Sofía": 7.9}

Imprime una tabla con:
  - Nombre alineado a la izquierda (20 chars)
  - Nota con 1 decimal (5 chars, alineada a la derecha)
  - Calificación: "Sobresaliente" (>=9), "Notable" (>=7), 
                  "Bien" (>=6), "Suficiente" (>=5), "Insuficiente" (<5)
  - Al final: promedio del grupo

Ejemplo de fila: "Ana                  9.3  Sobresaliente"
""")

notas = {"Ana": 9.3, "Luis": 6.7, "Marta": 8.5, "Pedro": 4.2, "Sofía": 7.9}

# TODO: Escribe tu código aquí


# ============================================
# EJERCICIO 3: Formatear unidades de tiempo
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Formatear unidades de tiempo")
print("-" * 60)
print("""
Crea una función formato_tiempo(segundos_totales) que reciba
un número de segundos y lo devuelva como string "HH:MM:SS".

Ejemplos:
  formato_tiempo(0)       -> "00:00:00"
  formato_tiempo(65)      -> "00:01:05"
  formato_tiempo(3661)    -> "01:01:01"
  formato_tiempo(86399)   -> "23:59:59"

Pista: usa división entera // y módulo % para calcular
       horas, minutos y segundos, luego f-strings con :02d.
""")

def formato_tiempo(segundos_totales):
    # TODO: Escribe tu código aquí
    pass

# Pruebas:
# print(formato_tiempo(0))
# print(formato_tiempo(65))
# print(formato_tiempo(3661))
# print(formato_tiempo(86399))


# ============================================
# EJERCICIO 4: Barra de progreso
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Barra de progreso")
print("-" * 60)
print("""
Crea una función barra_progreso(actual, total, ancho=30) que 
genere una barra de progreso visual.

Ejemplo para actual=7, total=10:
  [███████████████████░░░░░░░░░░░] 70.0%  (7/10)

Pista: calcula qué porcentaje de 'ancho' está lleno, y rellena
       con '█' y '░'. Usa f-strings para el porcentaje.
""")

def barra_progreso(actual, total, ancho=30):
    # TODO: Escribe tu código aquí
    pass

# Pruebas:
# for i in range(0, 11):
#     print(barra_progreso(i, 10))


# ============================================
# EJERCICIO 5: Plantilla de correo (str.format)
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 5: Plantilla de correo con str.format()")
print("-" * 60)
print("""
Define una PLANTILLA (string con {}) para un correo de bienvenida:
  - Saluda al {nombre}
  - Menciona su {rol} en la empresa {empresa}
  - Indica que su acceso expira en {dias} días
  - Firma como {firmante}

Luego genera 3 correos diferentes usando .format() con datos distintos.
""")

plantilla_correo = """
Estimado/a {nombre},

Bienvenido/a al equipo de {empresa} como {rol}.
Su acceso al sistema estará disponible durante los próximos {dias} días.

Para cualquier consulta, no dude en contactarnos.

Atentamente,
{firmante}
"""

empleados = [
    {"nombre": "Ana López",   "rol": "Desarrolladora",  "empresa": "TechCorp", "dias": 30, "firmante": "RRHH"},
    {"nombre": "Carlos Ruiz", "rol": "Diseñador",        "empresa": "TechCorp", "dias": 30, "firmante": "RRHH"},
    {"nombre": "Marta Gil",   "rol": "Project Manager",  "empresa": "TechCorp", "dias": 14, "firmante": "Dirección"},
]

# TODO: Genera los 3 correos usando plantilla_correo.format(**empleado)


# ============================================
# SOLUCIONES (descomenta para ver)
# ============================================
"""
# SOLUCIÓN 1:
ANCHO = 42
print("-" * ANCHO)
print("CAFETERÍA PYTHON".center(ANCHO))
print("-" * ANCHO)
subtotal = 0
for nombre, precio, cantidad in items:
    total_item = precio * cantidad
    subtotal += total_item
    print(f"  {nombre:<15} x{cantidad:<5} {total_item:>8.2f}€")
print("-" * ANCHO)
iva = subtotal * 0.10
total = subtotal + iva
print(f"  {'SUBTOTAL:':<25} {subtotal:>8.2f}€")
print(f"  {'IVA (10%):':<25} {iva:>8.2f}€")
print(f"  {'TOTAL:':<25} {total:>8.2f}€")
print("-" * ANCHO)

# SOLUCIÓN 2:
def calificacion(n):
    if n >= 9: return "Sobresaliente"
    if n >= 7: return "Notable"
    if n >= 6: return "Bien"
    if n >= 5: return "Suficiente"
    return "Insuficiente"

for nombre, nota in notas.items():
    print(f"{nombre:<20} {nota:>5.1f}  {calificacion(nota)}")
promedio = sum(notas.values()) / len(notas)
print(f"\\nPromedio del grupo: {promedio:.2f}")

# SOLUCIÓN 3:
def formato_tiempo(segundos_totales):
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

# SOLUCIÓN 4:
def barra_progreso(actual, total, ancho=30):
    porcentaje = actual / total
    lleno = int(porcentaje * ancho)
    barra = "█" * lleno + "░" * (ancho - lleno)
    return f"[{barra}] {porcentaje:.1%}  ({actual}/{total})"

# SOLUCIÓN 5:
for empleado in empleados:
    print(plantilla_correo.format(**empleado))
    print("=" * 50)
"""
