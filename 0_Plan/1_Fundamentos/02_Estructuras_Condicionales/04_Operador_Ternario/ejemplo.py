"""
Ejemplos del Operador Ternario en Python
========================================

Este archivo contiene ejemplos del operador condicional ternario.
"""

# ============================================
# 1. SINTAXIS BÁSICA
# ============================================
print("=" * 60)
print("1. SINTAXIS BÁSICA DEL OPERADOR TERNARIO")
print("=" * 60)

edad = 20

# Forma tradicional con if-else
if edad >= 18:
    estado_tradicional = "Mayor de edad"
else:
    estado_tradicional = "Menor de edad"

# Forma con operador ternario
estado_ternario = "Mayor de edad" if edad >= 18 else "Menor de edad"

print(f"Edad: {edad}")
print(f"Con if-else: {estado_tradicional}")
print(f"Con ternario: {estado_ternario}")

# Estructura del ternario
print("\nEstructura:")
print("  valor_si_true if condicion else valor_si_false")

# ============================================
# 2. ASIGNACIONES SIMPLES
# ============================================
print("\n" + "=" * 60)
print("2. ASIGNACIONES SIMPLES")
print("=" * 60)

# Ejemplo 1: Verificar paridad
numero = 7
tipo = "Par" if numero % 2 == 0 else "Impar"
print(f"{numero} es {tipo}")

# Ejemplo 2: Estado de usuario
is_active = True
estado = "Activo" if is_active else "Inactivo"
print(f"Usuario: {estado}")

# Ejemplo 3: Descuento
es_miembro = True
descuento = 15 if es_miembro else 0
print(f"Descuento: {descuento}%")

# ============================================
# 3. VALORES POR DEFECTO
# ============================================
print("\n" + "=" * 60)
print("3. VALORES POR DEFECTO")
print("=" * 60)

# Simular entrada de usuario
input_nombre = ""
input_edad = 25

# Usar ternario para valores por defecto
nombre = input_nombre if input_nombre else "Anónimo"
edad_texto = str(input_edad) if input_edad else "No especificada"

print(f"Nombre: {nombre}")
print(f"Edad: {edad_texto}")

# Comparación con 'or' (alternativa)
nombre_or = input_nombre or "Anónimo"
print(f"\nUsando 'or': {nombre_or}")

# ============================================
# 4. MAYOR Y MENOR DE DOS NÚMEROS
# ============================================
print("\n" + "=" * 60)
print("4. MAYOR Y MENOR DE DOS NÚMEROS")
print("=" * 60)

a = 15
b = 23

maximo = a if a > b else b
minimo = a if a < b else b

print(f"a = {a}, b = {b}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# Comparación con funciones built-in
print(f"\nUsando max(): {max(a, b)}")
print(f"Usando min(): {min(a, b)}")

# ============================================
# 5. FORMATEO DE SALIDA
# ============================================
print("\n" + "=" * 60)
print("5. FORMATEO DE SALIDA")
print("=" * 60)

# Singular vs Plural
items = [1, 3, 0]

for cantidad in items:
    # Ternario en f-string
    texto = f"Tienes {cantidad} {'item' if cantidad == 1 else 'items'}"
    print(texto)

# Otro ejemplo
puntos = 1500
mensaje = "¡Alto puntaje!" if puntos > 1000 else "Sigue intentando"
print(f"\nPuntos: {puntos} - {mensaje}")

# ============================================
# 6. EN FUNCIONES
# ============================================
print("\n" + "=" * 60)
print("6. OPERADOR TERNARIO EN FUNCIONES")
print("=" * 60)

# Función con ternario en return
def obtener_descuento(es_vip):
    return 0.20 if es_vip else 0.0

# Función para obtener signo
def obtener_signo(numero):
    return "positivo" if numero >= 0 else "negativo"

# Función para clasificar edad
def es_adulto(edad):
    return True if edad >= 18 else False
    # Mejor: return edad >= 18

print(f"Descuento VIP: {obtener_descuento(True)*100}%")
print(f"Descuento Normal: {obtener_descuento(False)*100}%")
print(f"Signo de 5: {obtener_signo(5)}")
print(f"Signo de -3: {obtener_signo(-3)}")

# ============================================
# 7. TERNARIOS ANIDADOS (CUIDADO)
# ============================================
print("\n" + "=" * 60)
print("7. TERNARIOS ANIDADOS (Usar con precaución)")
print("=" * 60)

nota = 85

# Ternario anidado (difícil de leer)
letra_ternario = "A" if nota >= 90 else ("B" if nota >= 80 else ("C" if nota >= 70 else "F"))
print(f"Nota {nota} → Letra (ternario anidado): {letra_ternario}")

# Mejor forma: if-elif-else tradicional
if nota >= 90:
    letra_claro = "A"
elif nota >= 80:
    letra_claro = "B"
elif nota >= 70:
    letra_claro = "C"
else:
    letra_claro = "F"

print(f"Nota {nota} → Letra (if-elif-else): {letra_claro}")

print("\n⚠️  Los ternarios anidados son poco legibles.")
print("    Para 3+ condiciones, usa if-elif-else")

# ============================================
# 8. EJEMPLO: CALCULADORA DE DESCUENTOS
# ============================================
print("\n" + "=" * 60)
print("8. EJEMPLO: CALCULADORA DE DESCUENTOS")
print("=" * 60)

compras = [
    {"monto": 150, "es_vip": False},
    {"monto": 1200, "es_vip": True},
    {"monto": 500, "es_vip": True},
]

for i, compra in enumerate(compras, 1):
    monto = compra["monto"]
    es_vip = compra["es_vip"]
    
    # Ternario para descuento
    descuento_porcentaje = 20 if es_vip else (10 if monto >= 1000 else 0)
    descuento_monto = monto * descuento_porcentaje / 100
    total = monto - descuento_monto
    
    print(f"\nCompra {i}:")
    print(f"  Monto: ${monto:.2f}")
    print(f"  VIP: {'Sí' if es_vip else 'No'}")
    print(f"  Descuento: {descuento_porcentaje}% (${descuento_monto:.2f})")
    print(f"  Total: ${total:.2f}")

# ============================================
# 9. EJEMPLO: VALIDACIONES
# ============================================
print("\n" + "=" * 60)
print("9. EJEMPLO: VALIDACIONES")
print("=" * 60)

usuarios = [
    {"edad": 25, "tiene_licencia": True},
    {"edad": 16, "tiene_licencia": False},
    {"edad": 20, "tiene_licencia": False},
]

for usuario in usuarios:
    edad = usuario["edad"]
    licencia = usuario["tiene_licencia"]
    
    # Múltiples ternarios
    puede_conducir = "Sí" if (edad >= 18 and licencia) else "No"
    emoji = "✅" if puede_conducir == "Sí" else "❌"
    razon = "" if puede_conducir == "Sí" else (
        "(menor de edad)" if edad < 18 else "(sin licencia)"
    )
    
    print(f"{emoji} Edad: {edad}, Licencia: {licencia} → Puede conducir: {puede_conducir} {razon}")

# ============================================
# 10. EN COMPRENSIONES DE LISTA
# ============================================
print("\n" + "=" * 60)
print("10. TERNARIO EN COMPRENSIONES DE LISTA")
print("=" * 60)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Duplicar pares, triplicar impares
resultado = [n*2 if n % 2 == 0 else n*3 for n in numeros]

print(f"Original: {numeros}")
print(f"Resultado: {resultado}")

# Clasificar números
clasificacion = ["Par" if n % 2 == 0 else "Impar" for n in numeros]
print(f"Clasificación: {clasificacion}")

# ============================================
# 11. EJEMPLO: SALUDO SEGÚN HORA
# ============================================
print("\n" + "=" * 60)
print("11. EJEMPLO: SALUDO SEGÚN HORA")
print("=" * 60)

horas = [8, 14, 22]

for hora in horas:
    # Ternario anidado para saludo
    saludo = (
        "Buenos días" if hora < 12 
        else ("Buenas tardes" if hora < 20 
              else "Buenas noches")
    )
    
    print(f"{hora:02d}:00 → {saludo}")

# ============================================
# 12. EJEMPLO: CATEGORIZACIÓN DE PRODUCTOS
# ============================================
print("\n" + "=" * 60)
print("12. EJEMPLO: CATEGORIZACIÓN DE PRODUCTOS")
print("=" * 60)

productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 0},
    {"nombre": "Teclado", "precio": 80, "stock": 15},
]

for prod in productos:
    nombre = prod["nombre"]
    precio = prod["precio"]
    stock = prod["stock"]
    
    # Varios ternarios
    categoria = "Premium" if precio > 1000 else "Standard"
    disponibilidad = "En stock" if stock > 0 else "Agotado"
    urgencia = "¡Últimas unidades!" if 0 < stock < 10 else ""
    
    print(f"\n{nombre}:")
    print(f"  Precio: ${precio}")
    print(f"  Categoría: {categoria}")
    print(f"  Estado: {disponibilidad} {urgencia}")

# ============================================
# 13. ALTERNATIVAS AL TERNARIO
# ============================================
print("\n" + "=" * 60)
print("13. ALTERNATIVAS AL TERNARIO")
print("=" * 60)

# Opción 1: Ternario anidado (poco legible)
dia_num = 3
dia_ternario = (
    "Lunes" if dia_num == 1 else
    ("Martes" if dia_num == 2 else
     ("Miércoles" if dia_num == 3 else
      ("Jueves" if dia_num == 4 else
       ("Viernes" if dia_num == 5 else
        ("Sábado" if dia_num == 6 else "Domingo")))))
)

# Opción 2: Diccionario (mucho mejor)
dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}
dia_dict = dias.get(dia_num, "Día inválido")

print(f"Día {dia_num}:")
print(f"  Con ternario: {dia_ternario}")
print(f"  Con diccionario: {dia_dict}")

# ============================================
# 14. BUENAS VS MALAS PRÁCTICAS
# ============================================
print("\n" + "=" * 60)
print("14. BUENAS VS MALAS PRÁCTICAS")
print("=" * 60)

x = 5

print("✅ BUENO: Ternario simple y claro")
resultado_bueno = "positivo" if x > 0 else "no positivo"
print(f"   {resultado_bueno}")

print("\n❌ MALO: Ternario muy complejo")
print("   resultado = funcion_larga() if condicion_compleja and otra_condicion else procesar_alternativa()")
print("   → Mejor usar if-else tradicional")

print("\n✅ BUENO: Simplificar expresión booleana")
es_par_mal = True if x % 2 == 0 else False  # Redundante
es_par_bien = x % 2 == 0  # Directo
print(f"   {x} es par: {es_par_bien}")

# ============================================
# 15. CASOS PRÁCTICOS FINALES
# ============================================
print("\n" + "=" * 60)
print("15. CASOS PRÁCTICOS FINALES")
print("=" * 60)

# Caso 1: Mensaje personalizado
nombre_usuario = "Juan"
saludo_personalizado = f"Hola {nombre_usuario}" if nombre_usuario else "Hola invitado"
print(f"Saludo: {saludo_personalizado}")

# Caso 2: Formateo de moneda
monto = 1234.56
formato = f"${monto:,.2f}" if monto >= 0 else f"-${abs(monto):,.2f}"
print(f"Formato: {formato}")

# Caso 3: Estado de conexión
intentos = 3
max_intentos = 5
estado_conexion = "Conectando..." if intentos < max_intentos else "Error: Máximo de intentos"
print(f"Estado ({intentos}/{max_intentos}): {estado_conexion}")

# Caso 4: Prioridad de tarea
urgente = True
prioridad = "🔴 Alta" if urgente else "🟢 Normal"
print(f"Prioridad: {prioridad}")

print("\n" + "=" * 60)
print("FIN DE LOS EJEMPLOS")
print("=" * 60)

print("\n💡 RECORDATORIO:")
print("   - Usa ternario para asignaciones simples")
print("   - Evita ternarios anidados complejos")
print("   - La legibilidad siempre es más importante que la brevedad")
