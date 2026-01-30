"""
Ejemplos de if, elif, else en Python
====================================

Este archivo contiene ejemplos ejecutables de estructuras
condicionales básicas.
"""

# ============================================
# 1. IF SIMPLE
# ============================================
print("=" * 60)
print("1. SENTENCIA IF SIMPLE")
print("=" * 60)

edad = 20
print(f"Edad: {edad}")

if edad >= 18:
    print("✓ Eres mayor de edad")
    print("✓ Puedes votar")

print("Programa continúa...\n")

# Otro ejemplo
temperatura = 30
print(f"Temperatura: {temperatura}°C")

if temperatura > 25:
    print("🌡️ Hace calor, usa ropa ligera")

# ============================================
# 2. IF-ELSE
# ============================================
print("\n" + "=" * 60)
print("2. SENTENCIA IF-ELSE")
print("=" * 60)

edad_usuario = 15
print(f"Edad del usuario: {edad_usuario}")

if edad_usuario >= 18:
    print("✓ Mayor de edad")
    print("✓ Acceso permitido")
else:
    print("✗ Menor de edad")
    print("✗ Acceso denegado")

# Ejemplo con números
numero = -5
print(f"\nNúmero: {numero}")

if numero >= 0:
    print("El número es positivo o cero")
else:
    print("El número es negativo")

# ============================================
# 3. IF-ELIF-ELSE
# ============================================
print("\n" + "=" * 60)
print("3. SENTENCIA IF-ELIF-ELSE")
print("=" * 60)

calificacion = 85
print(f"Calificación: {calificacion}")

if calificacion >= 90:
    letra = "A"
    mensaje = "Excelente"
elif calificacion >= 80:
    letra = "B"
    mensaje = "Muy bien"
elif calificacion >= 70:
    letra = "C"
    mensaje = "Bien"
elif calificacion >= 60:
    letra = "D"
    mensaje = "Suficiente"
else:
    letra = "F"
    mensaje = "Reprobado"

print(f"Letra: {letra}")
print(f"Estado: {mensaje}")

# ============================================
# 4. COMPARACIONES ENCADENADAS
# ============================================
print("\n" + "=" * 60)
print("4. COMPARACIONES ENCADENADAS (PYTHÓNICO)")
print("=" * 60)

edad_persona = 35
print(f"Edad: {edad_persona}")

# Forma pythónica
if 18 <= edad_persona < 65:
    categoria = "Adulto en edad laboral"
elif edad_persona < 18:
    categoria = "Menor de edad"
else:
    categoria = "Adulto mayor"

print(f"Categoría: {categoria}")

# Ejemplo con rangos de temperatura
temp = 22
print(f"\nTemperatura: {temp}°C")

if temp < 10:
    clima = "Frío"
elif 10 <= temp < 20:
    clima = "Fresco"
elif 20 <= temp < 30:
    clima = "Templado"
else:
    clima = "Caluroso"

print(f"Clima: {clima}")

# ============================================
# 5. CONDICIONALES ANIDADOS
# ============================================
print("\n" + "=" * 60)
print("5. CONDICIONALES ANIDADOS")
print("=" * 60)

edad_conductor = 20
tiene_licencia = True

print(f"Edad: {edad_conductor}")
print(f"Tiene licencia: {tiene_licencia}")

if edad_conductor >= 18:
    if tiene_licencia:
        print("✓ Puede conducir")
    else:
        print("✗ Mayor de edad pero sin licencia")
else:
    print("✗ Menor de edad, no puede conducir")

print("\n--- Forma mejorada (sin anidación) ---")

# Mejor forma usando guard clauses
if edad_conductor < 18:
    print("✗ Menor de edad, no puede conducir")
elif not tiene_licencia:
    print("✗ Mayor de edad pero sin licencia")
else:
    print("✓ Puede conducir")

# ============================================
# 6. EJEMPLO PRÁCTICO: CALCULADORA DE IMC
# ============================================
print("\n" + "=" * 60)
print("6. EJEMPLO: CALCULADORA DE IMC")
print("=" * 60)

peso = 70  # kg
altura = 1.75  # metros

imc = peso / (altura ** 2)

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    categoria_imc = "Bajo peso"
    emoji = "⚠️"
    recomendacion = "Consulta a un nutricionista"
elif imc < 25:
    categoria_imc = "Peso normal"
    emoji = "✓"
    recomendacion = "Mantén tu estilo de vida saludable"
elif imc < 30:
    categoria_imc = "Sobrepeso"
    emoji = "⚠️"
    recomendacion = "Considera aumentar tu actividad física"
else:
    categoria_imc = "Obesidad"
    emoji = "⚠️"
    recomendacion = "Consulta a un profesional de la salud"

print(f"\n{emoji} Categoría: {categoria_imc}")
print(f"Recomendación: {recomendacion}")

# ============================================
# 7. EJEMPLO: CALCULADORA DE DESCUENTOS
# ============================================
print("\n" + "=" * 60)
print("7. EJEMPLO: CALCULADORA DE DESCUENTOS")
print("=" * 60)

monto_compra = 750.00

print(f"Monto de compra: ${monto_compra:.2f}")

if monto_compra >= 1000:
    descuento_porcentaje = 20
    descuento_monto = monto_compra * 0.20
elif monto_compra >= 500:
    descuento_porcentaje = 10
    descuento_monto = monto_compra * 0.10
else:
    descuento_porcentaje = 0
    descuento_monto = 0

precio_final = monto_compra - descuento_monto

print(f"Descuento: {descuento_porcentaje}% (${descuento_monto:.2f})")
print(f"Precio final: ${precio_final:.2f}")
print(f"Ahorras: ${descuento_monto:.2f}")

# ============================================
# 8. EJEMPLO: VERIFICADOR DE DÍA DE LA SEMANA
# ============================================
print("\n" + "=" * 60)
print("8. EJEMPLO: VERIFICADOR DE DÍA")
print("=" * 60)

dia = "miércoles"
print(f"Día: {dia}")

if dia == "lunes" or dia == "martes" or dia == "miércoles":
    periodo = "Inicio de semana"
    emoji = "💼"
elif dia == "jueves" or dia == "viernes":
    periodo = "Fin de semana laboral"
    emoji = "📅"
elif dia == "sábado" or dia == "domingo":
    periodo = "Fin de semana"
    emoji = "🎉"
else:
    periodo = "Día no válido"
    emoji = "❌"

print(f"{emoji} {periodo}")

# ============================================
# 9. EJEMPLO: CLASIFICADOR DE EDADES
# ============================================
print("\n" + "=" * 60)
print("9. EJEMPLO: CLASIFICADOR DE EDADES")
print("=" * 60)

edades = [5, 15, 25, 45, 70]

for edad_clasificar in edades:
    if edad_clasificar < 13:
        grupo = "Niño"
    elif edad_clasificar < 18:
        grupo = "Adolescente"
    elif edad_clasificar < 60:
        grupo = "Adulto"
    else:
        grupo = "Adulto mayor"
    
    print(f"Edad {edad_clasificar:2d} → {grupo}")

# ============================================
# 10. EJEMPLO: VALIDACIÓN DE CONTRASEÑA
# ============================================
print("\n" + "=" * 60)
print("10. EJEMPLO: VALIDADOR DE CONTRASEÑA")
print("=" * 60)

contraseña = "Python2024"
longitud = len(contraseña)

print(f"Contraseña: {'*' * longitud}")
print(f"Longitud: {longitud} caracteres")

if longitud < 6:
    seguridad = "Muy débil"
    emoji = "🔴"
elif longitud < 8:
    seguridad = "Débil"
    emoji = "🟠"
elif longitud < 12:
    seguridad = "Moderada"
    emoji = "🟡"
else:
    seguridad = "Fuerte"
    emoji = "🟢"

print(f"{emoji} Seguridad: {seguridad}")

# ============================================
# 11. EJEMPLO: CONVERSOR DE NOTAS
# ============================================
print("\n" + "=" * 60)
print("11. EJEMPLO: CONVERSOR DE NOTAS")
print("=" * 60)

calificaciones = [95, 87, 76, 65, 52]

print(f"{'Número':>8} {'Letra':>8} {'Estado':>15}")
print("-" * 35)

for nota in calificaciones:
    # Determinar letra
    if nota >= 90:
        letra_nota = "A"
    elif nota >= 80:
        letra_nota = "B"
    elif nota >= 70:
        letra_nota = "C"
    elif nota >= 60:
        letra_nota = "D"
    else:
        letra_nota = "F"
    
    # Determinar estado
    if nota >= 60:
        estado = "✓ Aprobado"
    else:
        estado = "✗ Reprobado"
    
    print(f"{nota:8d} {letra_nota:>8} {estado:>15}")

# ============================================
# 12. EJEMPLO: CALCULADORA SIMPLE
# ============================================
print("\n" + "=" * 60)
print("12. EJEMPLO: CALCULADORA SIMPLE")
print("=" * 60)

num1 = 10
num2 = 5
operacion = "+"

print(f"Operación: {num1} {operacion} {num2}")

if operacion == "+":
    resultado = num1 + num2
    nombre_operacion = "Suma"
elif operacion == "-":
    resultado = num1 - num2
    nombre_operacion = "Resta"
elif operacion == "*":
    resultado = num1 * num2
    nombre_operacion = "Multiplicación"
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        nombre_operacion = "División"
    else:
        resultado = "Error"
        nombre_operacion = "División por cero"
else:
    resultado = "Error"
    nombre_operacion = "Operación no válida"

print(f"{nombre_operacion}: {resultado}")

# ============================================
# 13. EJEMPLO: AÑO BISIESTO
# ============================================
print("\n" + "=" * 60)
print("13. EJEMPLO: VERIFICADOR DE AÑO BISIESTO")
print("=" * 60)

años = [2020, 1900, 2000, 2024]

for año in años:
    if año % 400 == 0:
        es_bisiesto = True
    elif año % 100 == 0:
        es_bisiesto = False
    elif año % 4 == 0:
        es_bisiesto = True
    else:
        es_bisiesto = False
    
    estado = "SÍ es bisiesto" if es_bisiesto else "NO es bisiesto"
    print(f"{año}: {estado}")

# ============================================
# 14. EJEMPLO: SISTEMA DE ACCESO
# ============================================
print("\n" + "=" * 60)
print("14. EJEMPLO: SISTEMA DE ACCESO")
print("=" * 60)

usuario = "admin"
contraseña_usuario = "1234"
usuario_correcto = "admin"
contraseña_correcta = "1234"

print(f"Usuario: {usuario}")
print(f"Contraseña: {'*' * len(contraseña_usuario)}")

if usuario != usuario_correcto:
    mensaje = "❌ Usuario incorrecto"
    acceso = False
elif contraseña_usuario != contraseña_correcta:
    mensaje = "❌ Contraseña incorrecta"
    acceso = False
else:
    mensaje = "✅ Acceso concedido"
    acceso = True

print(mensaje)

print("\n" + "=" * 60)
print("FIN DE LOS EJEMPLOS")
print("=" * 60)
