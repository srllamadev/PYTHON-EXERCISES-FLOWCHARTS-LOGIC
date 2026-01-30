"""
Ejemplos de Expresiones Booleanas en Python
===========================================

Este archivo contiene ejemplos de truthy/falsy, comparaciones
y simplificación de expresiones booleanas.
"""

# ============================================
# 1. VALORES TRUTHY Y FALSY
# ============================================
print("=" * 60)
print("1. VALORES TRUTHY Y FALSY")
print("=" * 60)

# Valores que son False (Falsy)
valores_falsy = [
    False,
    None,
    0,
    0.0,
    0j,
    '',
    [],
    (),
    {},
    set(),
    range(0)
]

print("VALORES FALSY (se evalúan como False):")
for valor in valores_falsy:
    print(f"  bool({repr(valor):20}) = {bool(valor)}")

# Valores que son True (Truthy)
valores_truthy = [
    True,
    1,
    -1,
    3.14,
    "texto",
    "0",        # String "0" es truthy!
    " ",        # Espacio es truthy!
    [0],        # Lista con 0 es truthy!
    [False],    # Lista con False es truthy!
    (1,),
    {'key': None},
]

print("\nVALORES TRUTHY (se evalúan como True):")
for valor in valores_truthy[:6]:  # Primeros 6 para no saturar
    print(f"  bool({repr(valor):20}) = {bool(valor)}")

# ============================================
# 2. USO PRÁCTICO DE TRUTHY/FALSY
# ============================================
print("\n" + "=" * 60)
print("2. USO PRÁCTICO DE TRUTHY/FALSY")
print("=" * 60)

# Verificar lista vacía
items = []
print(f"Lista: {items}")

if not items:  # Forma pythónica
    print("  ✓ Lista vacía (usando truthy/falsy)")

if len(items) == 0:  # Menos pythónico
    print("  ✓ Lista vacía (usando len)")

# Verificar string vacío
nombre = ""
print(f"\nNombre: '{nombre}'")

if not nombre:
    print("  ✗ Nombre vacío")

# Con contenido
nombre = "Juan"
print(f"\nNombre: '{nombre}'")

if nombre:
    print(f"  ✓ Nombre válido: {nombre}")

# ============================================
# 3. VALORES POR DEFECTO CON OR
# ============================================
print("\n" + "=" * 60)
print("3. VALORES POR DEFECTO CON OR")
print("=" * 60)

# Simular input vacío
entrada_nombre = ""
entrada_edad = ""

# Usar or para valores por defecto
nombre_final = entrada_nombre or "Anónimo"
edad_final = entrada_edad or "No especificada"

print(f"Entrada nombre: '{entrada_nombre}' → Resultado: '{nombre_final}'")
print(f"Entrada edad: '{entrada_edad}' → Resultado: '{edad_final}'")

# Con valores
entrada_nombre2 = "María"
nombre_final2 = entrada_nombre2 or "Anónimo"
print(f"\nEntrada nombre: '{entrada_nombre2}' → Resultado: '{nombre_final2}'")

# ============================================
# 4. COMPARACIONES ENCADENADAS
# ============================================
print("\n" + "=" * 60)
print("4. COMPARACIONES ENCADENADAS")
print("=" * 60)

edades = [15, 25, 35, 70]

print("Clasificación por edad:")
for edad in edades:
    if edad < 18:
        categoria = "Menor de edad"
    elif 18 <= edad < 65:  # Comparación encadenada
        categoria = "Adulto"
    else:
        categoria = "Adulto mayor"
    
    print(f"  Edad {edad:2d} → {categoria}")

# Verificar rango
print("\nVerificación de rango:")
numeros = [5, 15, 25, 35]

for num in numeros:
    en_rango = 10 <= num <= 30  # Comparación encadenada
    estado = "Dentro del rango" if en_rango else "Fuera del rango"
    print(f"  {num:2d} → {estado}")

# Múltiples comparaciones
print("\nOrden ascendente:")
a, b, c, d = 1, 5, 10, 15
if a < b < c < d:
    print(f"  ✓ {a} < {b} < {c} < {d} (orden ascendente)")

# ============================================
# 5. OPERADORES DE IDENTIDAD (is vs ==)
# ============================================
print("\n" + "=" * 60)
print("5. OPERADORES DE IDENTIDAD (is vs ==)")
print("=" * 60)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")

print(f"\na == b: {a == b}  (mismo contenido)")
print(f"a is b: {a is b}  (mismo objeto? No)")
print(f"a is c: {a is c}  (mismo objeto? Sí)")

# Uso con None
valor = None
print(f"\nvalor = {valor}")
print(f"valor is None: {valor is None}  (✓ Correcto)")
print(f"valor == None: {valor == None}  (Funciona pero no recomendado)")

# ============================================
# 6. OPERADORES DE PERTENENCIA (in)
# ============================================
print("\n" + "=" * 60)
print("6. OPERADORES DE PERTENENCIA (in)")
print("=" * 60)

# En strings
texto = "Python es genial"
print(f"Texto: '{texto}'")
print(f"'Python' in texto: {'Python' in texto}")
print(f"'Java' in texto: {'Java' in texto}")
print(f"'python' in texto: {'python' in texto}  (case-sensitive)")
print(f"'python' in texto.lower(): {'python' in texto.lower()}  (con lower)")

# En listas
frutas = ["manzana", "banana", "naranja"]
print(f"\nFrutas: {frutas}")
print(f"'banana' in frutas: {'banana' in frutas}")
print(f"'uva' not in frutas: {'uva' not in frutas}")

# En diccionarios (verifica claves)
persona = {"nombre": "Juan", "edad": 30}
print(f"\nPersona: {persona}")
print(f"'nombre' in persona: {'nombre' in persona}")
print(f"'apellido' in persona: {'apellido' in persona}")

# ============================================
# 7. SIMPLIFICACIÓN DE EXPRESIONES
# ============================================
print("\n" + "=" * 60)
print("7. SIMPLIFICACIÓN DE EXPRESIONES")
print("=" * 60)

es_adulto = True

print("❌ MAL (redundante):")
print("   if es_adulto == True:")

print("\n✅ BIEN (simplificado):")
print("   if es_adulto:")

if es_adulto:
    print("   → Adulto verificado")

# Verificación de lista
lista = [1, 2, 3]

print(f"\nLista: {lista}")
print("❌ MAL: if len(lista) > 0:")
print("✅ BIEN: if lista:")

if lista:
    print("   → Lista tiene elementos")

# ============================================
# 8. EJEMPLO: VALIDADOR DE DATOS
# ============================================
print("\n" + "=" * 60)
print("8. EJEMPLO: VALIDADOR DE DATOS")
print("=" * 60)

def validar_usuario(usuario, edad, email):
    """Valida los datos de un usuario."""
    
    usuario_valido = (
        usuario and                    # No vacío
        len(usuario) >= 3 and         # Longitud mínima
        usuario.replace("_", "").isalnum() and  # Alfanumérico (permite _)
        edad is not None and          # Edad proporcionada
        isinstance(edad, int) and     # Es entero
        18 <= edad <= 120 and         # Rango válido
        email and                      # Email proporcionado
        "@" in email and              # Tiene @
        len(email.split("@")) == 2    # Solo un @
    )
    
    return usuario_valido

# Probar validación
usuarios_prueba = [
    ("juan123", 25, "juan@email.com"),
    ("ab", 30, "maria@email.com"),
    ("pedro", 15, "pedro@email.com"),
    ("ana", 30, "invalido.com"),
    ("", 25, "test@email.com"),
]

for usuario, edad, email in usuarios_prueba:
    valido = validar_usuario(usuario, edad, email)
    estado = "✅ Válido" if valido else "❌ Inválido"
    print(f"{estado} → Usuario: '{usuario}', Edad: {edad}, Email: '{email}'")

# ============================================
# 9. EJEMPLO: FILTRADO DE VALORES FALSY
# ============================================
print("\n" + "=" * 60)
print("9. EJEMPLO: FILTRADO DE VALORES FALSY")
print("=" * 60)

# Lista mixta con valores truthy y falsy
lista_mixta = [0, 1, "", "texto", None, False, True, [], [1], {}, {"a": 1}]

print(f"Lista original:")
print(f"  {lista_mixta}")

# Filtrar valores truthy (remover falsy)
lista_filtrada = [item for item in lista_mixta if item]

print(f"\nLista filtrada (solo truthy):")
print(f"  {lista_filtrada}")

# Contar truthy vs falsy
truthy_count = sum(1 for item in lista_mixta if item)
falsy_count = sum(1 for item in lista_mixta if not item)

print(f"\nEstadísticas:")
print(f"  Truthy: {truthy_count}")
print(f"  Falsy: {falsy_count}")

# ============================================
# 10. EJEMPLO: VALIDADOR DE EMAIL
# ============================================
print("\n" + "=" * 60)
print("10. EJEMPLO: VALIDADOR DE EMAIL")
print("=" * 60)

def validar_email(email):
    """Valida formato básico de email."""
    
    if not email:
        return False, "Email vacío"
    
    if "@" not in email:
        return False, "Falta el símbolo @"
    
    partes = email.split("@")
    
    if len(partes) != 2:
        return False, "Debe tener exactamente un @"
    
    usuario, dominio = partes
    
    if not usuario:
        return False, "Falta el nombre de usuario"
    
    if not dominio:
        return False, "Falta el dominio"
    
    if "." not in dominio:
        return False, "El dominio debe tener un punto"
    
    return True, "Email válido"

# Probar emails
emails_prueba = [
    "juan@email.com",
    "maria@@email.com",
    "@email.com",
    "pedro@",
    "ana@emailcom",
    "",
]

for email in emails_prueba:
    valido, mensaje = validar_email(email)
    emoji = "✅" if valido else "❌"
    print(f"{emoji} '{email:20}' → {mensaje}")

# ============================================
# 11. EJEMPLO: COMPARACIONES MÚLTIPLES
# ============================================
print("\n" + "=" * 60)
print("11. EJEMPLO: COMPARADOR DE NÚMEROS")
print("=" * 60)

numeros_conjuntos = [
    (5, 10, 15),
    (10, 10, 10),
    (15, 10, 5),
    (5, 15, 10),
]

for a, b, c in numeros_conjuntos:
    # Comparaciones encadenadas
    ascendente = a < b < c
    descendente = a > b > c
    todos_iguales = a == b == c
    
    print(f"\n({a}, {b}, {c}):")
    print(f"  Ascendente: {ascendente}")
    print(f"  Descendente: {descendente}")
    print(f"  Todos iguales: {todos_iguales}")

# ============================================
# 12. EJEMPLO: VERIFICACIÓN DE STRINGS
# ============================================
print("\n" + "=" * 60)
print("12. EJEMPLO: VERIFICADOR DE STRINGS")
print("=" * 60)

strings_prueba = ["", " ", "  ", "texto", "0", "False"]

for s in strings_prueba:
    vacio = not s
    solo_espacios = s and s.isspace()
    tiene_contenido = s and not s.isspace()
    
    print(f"\nString: '{s}'")
    print(f"  bool(s): {bool(s)}")
    print(f"  Vacío: {vacio}")
    print(f"  Solo espacios: {solo_espacios}")
    print(f"  Tiene contenido: {tiene_contenido}")

# ============================================
# 13. EJEMPLO: CONFIGURACIÓN CON DEFAULTS
# ============================================
print("\n" + "=" * 60)
print("13. EJEMPLO: CONFIGURACIÓN CON VALORES POR DEFECTO")
print("=" * 60)

# Simular configuración parcial
config = {
    "debug": True,
    "timeout": 30,
    # "max_retries" no está definido
}

# Obtener valores con defaults
debug_mode = config.get("debug", False)
timeout = config.get("timeout", 60)
max_retries = config.get("max_retries", 3)
port = config.get("port", 8080)

print("Configuración:")
print(f"  debug: {debug_mode}")
print(f"  timeout: {timeout}")
print(f"  max_retries: {max_retries} (default)")
print(f"  port: {port} (default)")

# ============================================
# 14. TRUCOS CON EXPRESIONES BOOLEANAS
# ============================================
print("\n" + "=" * 60)
print("14. TRUCOS CON EXPRESIONES BOOLEANAS")
print("=" * 60)

# Retornar primer valor truthy
valores = [0, "", None, "primero", "segundo"]
primer_truthy = next((v for v in valores if v), None)
print(f"Primer valor truthy: '{primer_truthy}'")

# Usando any() y all()
numeros = [2, 4, 6, 8]
print(f"\nNúmeros: {numeros}")
print(f"¿Todos pares? {all(n % 2 == 0 for n in numeros)}")
print(f"¿Alguno > 5? {any(n > 5 for n in numeros)}")

print("\n" + "=" * 60)
print("FIN DE LOS EJEMPLOS")
print("=" * 60)
