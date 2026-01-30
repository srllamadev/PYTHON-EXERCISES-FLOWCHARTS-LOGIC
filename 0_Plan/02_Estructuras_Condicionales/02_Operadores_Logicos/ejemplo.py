"""
Ejemplos de Operadores Lógicos en Python
========================================

Este archivo contiene ejemplos ejecutables de AND, OR y NOT.
"""

# ============================================
# 1. OPERADOR AND (Y LÓGICO)
# ============================================
print("=" * 60)
print("1. OPERADOR AND")
print("=" * 60)

edad = 25
tiene_licencia = True

print(f"Edad: {edad}")
print(f"Tiene licencia: {tiene_licencia}")

# Ambas condiciones deben ser True
puede_conducir = edad >= 18 and tiene_licencia
print(f"\n¿Puede conducir? {puede_conducir}")
print(f"  → Requiere: edad >= 18 AND tiene_licencia")

# Tabla de verdad de AND
print("\n📋 Tabla de verdad AND:")
print(f"   True  and True  = {True and True}")
print(f"   True  and False = {True and False}")
print(f"   False and True  = {False and True}")
print(f"   False and False = {False and False}")

# ============================================
# 2. OPERADOR OR (O LÓGICO)
# ============================================
print("\n" + "=" * 60)
print("2. OPERADOR OR")
print("=" * 60)

es_estudiante = False
es_senior = False
es_miembro = True

print(f"Es estudiante: {es_estudiante}")
print(f"Es senior: {es_senior}")
print(f"Es miembro: {es_miembro}")

# Al menos una condición debe ser True
tiene_descuento = es_estudiante or es_senior or es_miembro
print(f"\n¿Tiene descuento? {tiene_descuento}")
print(f"  → Requiere: estudiante OR senior OR miembro")

# Tabla de verdad de OR
print("\n📋 Tabla de verdad OR:")
print(f"   True  or True  = {True or True}")
print(f"   True  or False = {True or False}")
print(f"   False or True  = {False or True}")
print(f"   False or False = {False or False}")

# ============================================
# 3. OPERADOR NOT (NEGACIÓN)
# ============================================
print("\n" + "=" * 60)
print("3. OPERADOR NOT")
print("=" * 60)

archivo_procesado = False
usuario_activo = True

print(f"Archivo procesado: {archivo_procesado}")
print(f"Usuario activo: {usuario_activo}")

# Inversión de valores
necesita_procesar = not archivo_procesado
usuario_inactivo = not usuario_activo

print(f"\n¿Necesita procesar? {necesita_procesar}")
print(f"¿Usuario inactivo? {usuario_inactivo}")

# Tabla de verdad de NOT
print("\n📋 Tabla de verdad NOT:")
print(f"   not True  = {not True}")
print(f"   not False = {not False}")

# ============================================
# 4. COMBINACIÓN DE OPERADORES
# ============================================
print("\n" + "=" * 60)
print("4. COMBINACIÓN DE OPERADORES")
print("=" * 60)

edad_persona = 30
tiene_licencia_conducir = True
tiene_auto = False
es_instructor = False

print(f"Edad: {edad_persona}")
print(f"Tiene licencia: {tiene_licencia_conducir}")
print(f"Tiene auto: {tiene_auto}")
print(f"Es instructor: {es_instructor}")

# Combinación con paréntesis para claridad
puede_conducir_auto = (edad_persona >= 18 and tiene_licencia_conducir) or es_instructor
puede_conducir_propio = edad_persona >= 18 and tiene_licencia_conducir and tiene_auto

print(f"\n¿Puede conducir (auto de alguien)? {puede_conducir_auto}")
print(f"¿Puede conducir su propio auto? {puede_conducir_propio}")

# ============================================
# 5. EJEMPLO: VALIDACIÓN DE ACCESO
# ============================================
print("\n" + "=" * 60)
print("5. EJEMPLO: SISTEMA DE ACCESO")
print("=" * 60)

usuario = "admin"
contraseña = "1234"
edad_usuario = 25

print(f"Usuario: {usuario}")
print(f"Contraseña: {'*' * len(contraseña)}")
print(f"Edad: {edad_usuario}")

# Todas las validaciones deben pasar
acceso_concedido = (
    usuario == "admin" and
    contraseña == "1234" and
    edad_usuario >= 18
)

if acceso_concedido:
    print("\n✅ Acceso concedido")
else:
    print("\n❌ Acceso denegado")

# ============================================
# 6. EJEMPLO: DÍA LABORAL
# ============================================
print("\n" + "=" * 60)
print("6. EJEMPLO: VERIFICADOR DE DÍA LABORAL")
print("=" * 60)

dias = ["lunes", "miércoles", "sábado", "domingo"]

for dia in dias:
    # OR para múltiples opciones
    es_fin_semana = dia == "sábado" or dia == "domingo"
    es_laboral = not es_fin_semana
    
    emoji = "💼" if es_laboral else "🎉"
    tipo = "Laboral" if es_laboral else "Fin de semana"
    
    print(f"{emoji} {dia.capitalize():10} → {tipo}")

# ============================================
# 7. EJEMPLO: SISTEMA DE MEMBRESÍA
# ============================================
print("\n" + "=" * 60)
print("7. EJEMPLO: SISTEMA DE MEMBRESÍA")
print("=" * 60)

clientes = [
    {"nombre": "Juan", "es_premium": True, "antiguedad": 2, "gasto": 5000},
    {"nombre": "María", "es_premium": False, "antiguedad": 3, "gasto": 15000},
    {"nombre": "Pedro", "es_premium": False, "antiguedad": 0.5, "gasto": 500},
]

for cliente in clientes:
    nombre = cliente["nombre"]
    es_premium = cliente["es_premium"]
    antiguedad = cliente["antiguedad"]
    gasto = cliente["gasto"]
    
    # Lógica compleja con AND y OR
    es_vip = (es_premium and antiguedad > 1) or gasto > 10000
    es_regular = not es_premium and gasto >= 1000
    es_nuevo = antiguedad < 1
    
    if es_vip:
        categoria = "VIP"
        emoji = "⭐"
    elif es_regular:
        categoria = "Regular"
        emoji = "✓"
    else:
        categoria = "Nuevo"
        emoji = "🆕"
    
    print(f"{emoji} {nombre:8} → {categoria}")

# ============================================
# 8. EJEMPLO: VALIDACIÓN DE FORMULARIO
# ============================================
print("\n" + "=" * 60)
print("8. EJEMPLO: VALIDADOR DE FORMULARIO")
print("=" * 60)

formularios = [
    {"nombre": "Juan Pérez", "email": "juan@email.com", "edad": 25},
    {"nombre": "", "email": "maria@email.com", "edad": 30},
    {"nombre": "Pedro", "email": "pedro.email.com", "edad": 17},
]

for i, form in enumerate(formularios, 1):
    nombre = form["nombre"]
    email = form["email"]
    edad = form["edad"]
    
    # Múltiples validaciones con AND
    formulario_valido = (
        nombre != "" and
        len(nombre) >= 3 and
        "@" in email and
        "." in email and
        edad >= 18
    )
    
    estado = "✅ Válido" if formulario_valido else "❌ Inválido"
    
    print(f"\nFormulario {i}: {estado}")
    print(f"  Nombre: {nombre or '(vacío)'}")
    print(f"  Email: {email}")
    print(f"  Edad: {edad}")

# ============================================
# 9. EJEMPLO: ALERTAS METEOROLÓGICAS
# ============================================
print("\n" + "=" * 60)
print("9. EJEMPLO: SISTEMA DE ALERTAS METEOROLÓGICAS")
print("=" * 60)

condiciones = [
    {"temp": 35, "humedad": 85, "viento": 20},
    {"temp": 28, "humedad": 75, "viento": 15},
    {"temp": 32, "humedad": 60, "viento": 40},
    {"temp": 22, "humedad": 50, "viento": 10},
]

for cond in condiciones:
    temp = cond["temp"]
    humedad = cond["humedad"]
    viento = cond["viento"]
    
    # Diferentes niveles de alerta
    alerta_extrema = (temp > 30 and humedad > 80) or viento > 50
    alerta_alta = (temp > 30 or humedad > 70) and not alerta_extrema
    precaucion = (temp > 25 or humedad > 60 or viento > 30) and not alerta_extrema and not alerta_alta
    
    print(f"\nTemp: {temp}°C, Humedad: {humedad}%, Viento: {viento}km/h")
    
    if alerta_extrema:
        print("🔴 ALERTA EXTREMA: Condiciones peligrosas")
    elif alerta_alta:
        print("🟠 ALERTA ALTA: Precaución extrema")
    elif precaucion:
        print("🟡 PRECAUCIÓN: Condiciones adversas")
    else:
        print("🟢 NORMAL: Condiciones favorables")

# ============================================
# 10. CORTOCIRCUITO DE EVALUACIÓN
# ============================================
print("\n" + "=" * 60)
print("10. CORTOCIRCUITO DE EVALUACIÓN")
print("=" * 60)

print("Demostración de cortocircuito con AND:")
resultado = False and print("Esto NO se imprime")
print("  → Como el primer valor es False, no evalúa el segundo")

print("\nDemostración de cortocircuito con OR:")
resultado = True or print("Esto NO se imprime")
print("  → Como el primer valor es True, no evalúa el segundo")

# Uso práctico: evitar errores
print("\nUso práctico - evitar división por cero:")
divisor = 0
if divisor != 0 and 10 / divisor > 2:
    print("Resultado válido")
else:
    print("  → Evitó dividir por cero gracias al cortocircuito")

# ============================================
# 11. EJEMPLO: VALIDADOR DE CONTRASEÑA
# ============================================
print("\n" + "=" * 60)
print("11. EJEMPLO: VALIDADOR DE CONTRASEÑA SEGURA")
print("=" * 60)

contraseñas = ["abc", "Python2024", "Python2024!", "py"]

for pwd in contraseñas:
    longitud = len(pwd)
    tiene_mayuscula = any(c.isupper() for c in pwd)
    tiene_minuscula = any(c.islower() for c in pwd)
    tiene_numero = any(c.isdigit() for c in pwd)
    tiene_especial = any(c in "!@#$%^&*()" for c in pwd)
    
    # Todas las condiciones deben cumplirse
    es_segura = (
        longitud >= 8 and
        tiene_mayuscula and
        tiene_minuscula and
        tiene_numero and
        tiene_especial
    )
    
    estado = "🟢 Segura" if es_segura else "🔴 Insegura"
    
    print(f"\nContraseña: {'*' * len(pwd)} ({longitud} caracteres)")
    print(f"  Estado: {estado}")
    print(f"  Longitud >= 8: {'✓' if longitud >= 8 else '✗'}")
    print(f"  Mayúscula: {'✓' if tiene_mayuscula else '✗'}")
    print(f"  Minúscula: {'✓' if tiene_minuscula else '✗'}")
    print(f"  Número: {'✓' if tiene_numero else '✗'}")
    print(f"  Especial: {'✓' if tiene_especial else '✗'}")

# ============================================
# 12. PRECEDENCIA DE OPERADORES
# ============================================
print("\n" + "=" * 60)
print("12. PRECEDENCIA DE OPERADORES LÓGICOS")
print("=" * 60)

# NOT tiene mayor precedencia que AND
resultado1 = not False and True
print(f"not False and True = {resultado1}")
print("  → Se evalúa como: (not False) and True = True")

# AND tiene mayor precedencia que OR
resultado2 = True or False and False
print(f"\nTrue or False and False = {resultado2}")
print("  → Se evalúa como: True or (False and False) = True")

# Usando paréntesis para cambiar precedencia
resultado3 = (True or False) and False
print(f"\n(True or False) and False = {resultado3}")
print("  → Se evalúa como: (True) and False = False")

print("\n💡 Recomendación: Siempre usa paréntesis para claridad")

# ============================================
# 13. LEYES DE DE MORGAN
# ============================================
print("\n" + "=" * 60)
print("13. LEYES DE DE MORGAN")
print("=" * 60)

A = True
B = False

# Ley 1: not (A and B) = (not A) or (not B)
ley1_izq = not (A and B)
ley1_der = (not A) or (not B)
print(f"not (A and B) = {ley1_izq}")
print(f"(not A) or (not B) = {ley1_der}")
print(f"¿Son iguales? {ley1_izq == ley1_der}\n")

# Ley 2: not (A or B) = (not A) and (not B)
ley2_izq = not (A or B)
ley2_der = (not A) and (not B)
print(f"not (A or B) = {ley2_izq}")
print(f"(not A) and (not B) = {ley2_der}")
print(f"¿Son iguales? {ley2_izq == ley2_der}")

print("\n" + "=" * 60)
print("FIN DE LOS EJEMPLOS")
print("=" * 60)
