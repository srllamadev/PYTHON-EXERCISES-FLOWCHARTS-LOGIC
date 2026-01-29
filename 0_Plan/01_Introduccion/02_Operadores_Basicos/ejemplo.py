"""
Ejemplos de Operadores Básicos en Python
========================================

Este archivo contiene ejemplos ejecutables de todos los
tipos de operadores en Python.
"""

# ============================================
# 1. OPERADORES ARITMÉTICOS
# ============================================
print("=" * 60)
print("1. OPERADORES ARITMÉTICOS")
print("=" * 60)

a = 17
b = 5

print(f"a = {a}, b = {b}\n")

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
potencia = a ** b

print(f"Suma:             {a} + {b} = {suma}")
print(f"Resta:            {a} - {b} = {resta}")
print(f"Multiplicación:   {a} × {b} = {multiplicacion}")
print(f"División:         {a} / {b} = {division:.2f}")
print(f"División entera:  {a} // {b} = {division_entera}")
print(f"Módulo (resto):   {a} % {b} = {modulo}")
print(f"Potencia:         {a} ** {b} = {potencia:,}")

# Caso práctico: dividir en grupos
print(f"\n📦 Ejemplo: {a} galletas en grupos de {b}")
print(f"   Grupos completos: {division_entera}")
print(f"   Galletas sobrantes: {modulo}")

# ============================================
# 2. OPERADORES DE COMPARACIÓN
# ============================================
print("\n" + "=" * 60)
print("2. OPERADORES DE COMPARACIÓN")
print("=" * 60)

x = 10
y = 20
z = 10

print(f"x = {x}, y = {y}, z = {z}\n")

print(f"x == y  → {x} == {y}  = {x == y}  (¿son iguales?)")
print(f"x != y  → {x} != {y}  = {x != y}  (¿son diferentes?)")
print(f"x > y   → {x} > {y}   = {x > y}   (¿x es mayor que y?)")
print(f"x < y   → {x} < {y}   = {x < y}   (¿x es menor que y?)")
print(f"x >= z  → {x} >= {z}  = {x >= z}  (¿x es mayor o igual a z?)")
print(f"x <= y  → {x} <= {y}  = {x <= y}  (¿x es menor o igual a y?)")

# Comparaciones encadenadas (característica pythónica)
print(f"\nComparaciones encadenadas:")
print(f"5 < 10 < 15  = {5 < 10 < 15}")
print(f"5 < 10 > 8   = {5 < 10 > 8}")

# ============================================
# 3. OPERADORES LÓGICOS
# ============================================
print("\n" + "=" * 60)
print("3. OPERADORES LÓGICOS")
print("=" * 60)

edad = 25
tiene_licencia = True
tiene_auto = False

print(f"edad = {edad}")
print(f"tiene_licencia = {tiene_licencia}")
print(f"tiene_auto = {tiene_auto}\n")

# AND - Todas las condiciones deben ser True
puede_conducir = edad >= 18 and tiene_licencia
print(f"AND: ¿Puede conducir?")
print(f"     (edad >= 18) and tiene_licencia")
print(f"     ({edad >= 18}) and {tiene_licencia} = {puede_conducir}\n")

# OR - Al menos una condición debe ser True
tiene_transporte = tiene_auto or tiene_licencia
print(f"OR:  ¿Tiene transporte?")
print(f"     tiene_auto or tiene_licencia")
print(f"     {tiene_auto} or {tiene_licencia} = {tiene_transporte}\n")

# NOT - Invierte el valor booleano
no_tiene_auto = not tiene_auto
print(f"NOT: ¿No tiene auto?")
print(f"     not tiene_auto")
print(f"     not {tiene_auto} = {no_tiene_auto}")

# Tabla de verdad
print("\n📋 Tabla de verdad AND:")
print(f"   True  and True  = {True and True}")
print(f"   True  and False = {True and False}")
print(f"   False and True  = {False and True}")
print(f"   False and False = {False and False}")

print("\n📋 Tabla de verdad OR:")
print(f"   True  or True  = {True or True}")
print(f"   True  or False = {True or False}")
print(f"   False or True  = {False or True}")
print(f"   False or False = {False or False}")

# ============================================
# 4. OPERADORES DE ASIGNACIÓN
# ============================================
print("\n" + "=" * 60)
print("4. OPERADORES DE ASIGNACIÓN")
print("=" * 60)

puntos = 100
print(f"Puntos iniciales: {puntos}")

puntos += 50  # puntos = puntos + 50
print(f"Después de += 50: {puntos}")

puntos -= 20  # puntos = puntos - 20
print(f"Después de -= 20: {puntos}")

puntos *= 2   # puntos = puntos * 2
print(f"Después de *= 2:  {puntos}")

puntos //= 3  # puntos = puntos // 3
print(f"Después de //= 3: {puntos}")

# ============================================
# 5. OPERADORES DE PERTENENCIA
# ============================================
print("\n" + "=" * 60)
print("5. OPERADORES DE PERTENENCIA")
print("=" * 60)

frase = "Python es genial"
palabra = "Python"
palabra_no = "Java"

print(f"Frase: '{frase}'\n")
print(f"'{palabra}' in frase     = {palabra in frase}")
print(f"'{palabra_no}' in frase  = {palabra_no in frase}")
print(f"'{palabra_no}' not in frase = {palabra_no not in frase}")

# Con listas
numeros = [1, 2, 3, 4, 5]
print(f"\nLista: {numeros}")
print(f"3 in numeros     = {3 in numeros}")
print(f"10 in numeros    = {10 in numeros}")
print(f"10 not in numeros = {10 not in numeros}")

# ============================================
# 6. PRECEDENCIA DE OPERADORES
# ============================================
print("\n" + "=" * 60)
print("6. PRECEDENCIA DE OPERADORES")
print("=" * 60)

# Sin paréntesis
resultado1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {resultado1} (multiplicación primero)")

# Con paréntesis
resultado2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {resultado2} (suma primero)")

# Expresión compleja
resultado3 = 2 ** 3 + 4 * 5 - 6 / 2
print(f"2**3 + 4*5 - 6/2 = {resultado3}")
print(f"  → 8 + 20 - 3 = {resultado3}")

# Comparación con precedencia
resultado4 = 5 + 3 > 2 * 4
print(f"\n5 + 3 > 2 * 4 = {resultado4}")
print(f"  → 8 > 8 = {resultado4}")

# ============================================
# 7. EJEMPLO PRÁCTICO: CALCULADORA BÁSICA
# ============================================
print("\n" + "=" * 60)
print("7. EJEMPLO PRÁCTICO: CALCULADORA")
print("=" * 60)

num1 = 15
num2 = 4

print(f"Número 1: {num1}")
print(f"Número 2: {num2}")
print("-" * 40)
print(f"Suma:              {num1 + num2}")
print(f"Resta:             {num1 - num2}")
print(f"Multiplicación:    {num1 * num2}")
print(f"División:          {num1 / num2:.2f}")
print(f"División entera:   {num1 // num2}")
print(f"Resto:             {num1 % num2}")
print(f"Potencia:          {num1 ** num2:,}")

# ============================================
# 8. EJEMPLO PRÁCTICO: VERIFICADOR DE EDAD
# ============================================
print("\n" + "=" * 60)
print("8. EJEMPLO PRÁCTICO: VERIFICADOR DE EDAD")
print("=" * 60)

año_nacimiento = 1998
año_actual = 2024
edad_calculada = año_actual - año_nacimiento

print(f"Año de nacimiento: {año_nacimiento}")
print(f"Año actual: {año_actual}")
print(f"Edad: {edad_calculada} años")

es_mayor = edad_calculada >= 18
es_adulto_joven = 18 <= edad_calculada < 30
es_senior = edad_calculada >= 65

print(f"\n¿Es mayor de edad? {es_mayor}")
print(f"¿Es adulto joven (18-29)? {es_adulto_joven}")
print(f"¿Es senior (65+)? {es_senior}")

# ============================================
# 9. EJEMPLO PRÁCTICO: CALCULADORA DE DESCUENTO
# ============================================
print("\n" + "=" * 60)
print("9. EJEMPLO PRÁCTICO: CALCULADORA DE DESCUENTO")
print("=" * 60)

precio_original = 150.00
descuento_porcentaje = 20

descuento_monto = precio_original * descuento_porcentaje / 100
precio_final = precio_original - descuento_monto
ahorro = descuento_monto

print(f"Precio original:    ${precio_original:.2f}")
print(f"Descuento:          {descuento_porcentaje}%")
print(f"Monto descontado:   ${descuento_monto:.2f}")
print(f"Precio final:       ${precio_final:.2f}")
print(f"Ahorras:            ${ahorro:.2f}")

# ============================================
# 10. EJEMPLO PRÁCTICO: PAR O IMPAR
# ============================================
print("\n" + "=" * 60)
print("10. EJEMPLO PRÁCTICO: NÚMERO PAR O IMPAR")
print("=" * 60)

numero = 17
es_par = numero % 2 == 0
es_impar = numero % 2 != 0

print(f"Número: {numero}")
print(f"¿Es par? {es_par}")
print(f"¿Es impar? {es_impar}")

# Varios números
print("\nVerificación de varios números:")
for num in [10, 15, 22, 33, 100]:
    tipo = "PAR" if num % 2 == 0 else "IMPAR"
    print(f"{num:3d} → {tipo}")

# ============================================
# 11. TRUCOS Y CASOS ESPECIALES
# ============================================
print("\n" + "=" * 60)
print("11. TRUCOS Y CASOS ESPECIALES")
print("=" * 60)

# Swap pythónico
a, b = 10, 20
print(f"Antes del swap: a={a}, b={b}")
a, b = b, a
print(f"Después del swap: a={a}, b={b}")

# Evaluación de cortocircuito
print(f"\nCortocircuito AND: False and (1/0)")
print(f"Resultado: {False and print('Esto no se ejecuta')}")

print(f"\nCortocircuito OR: True or (1/0)")
print(f"Resultado: {True or print('Esto no se ejecuta')}")

# Comparación de cadenas
print(f"\nComparación de strings:")
print(f"'abc' < 'abd' = {'abc' < 'abd'} (orden alfabético)")
print(f"'Python' > 'Java' = {'Python' > 'Java'}")

print("\n" + "=" * 60)
print("FIN DE LOS EJEMPLOS")
print("=" * 60)
