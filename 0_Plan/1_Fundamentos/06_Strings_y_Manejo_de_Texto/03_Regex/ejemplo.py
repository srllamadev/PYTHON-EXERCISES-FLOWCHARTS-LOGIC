"""
Expresiones Regulares (Regex) en Python
=========================================

Ejemplos ejecutables del módulo 're'.
"""

import re

# ============================================
# 1. FUNCIONES BÁSICAS: match, search, findall
# ============================================
print("=" * 55)
print("1. FUNCIONES BÁSICAS")
print("=" * 55)

texto = "El año 2024 tiene 366 días; el 2023 tuvo 365."

# re.search — encuentra la primera coincidencia en cualquier posición
m = re.search(r"\d+", texto)
print(f"search(primer número): '{m.group()}' en posición {m.start()}")

# re.findall — todas las coincidencias como lista de strings
numeros = re.findall(r"\d+", texto)
print(f"findall(todos los números): {numeros}")

# re.match — solo comprueba el INICIO
texto2 = "2024 es un año bisiesto"
m_match = re.match(r"\d+", texto2)
m_fail  = re.match(r"\d+", texto)  # falla porque no empieza con dígito
print(f"match al inicio: '{m_match.group()}'")
print(f"match falla:     {m_fail}")

# ============================================
# 2. GRUPOS DE CAPTURA
# ============================================
print("\n" + "=" * 55)
print("2. GRUPOS DE CAPTURA")
print("=" * 55)

# Extraer partes de una fecha
fechas = ["2024-03-15", "1999-12-31", "2000-01-01"]
patron_fecha = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

for fecha in fechas:
    m = patron_fecha.match(fecha)
    if m:
        año, mes, dia = m.groups()
        print(f"Fecha: {fecha} → Año={año}, Mes={mes}, Día={dia}")

# Grupos con nombre (más legible)
print()
patron_fecha_n = re.compile(r"(?P<año>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})")
m = patron_fecha_n.match("2024-03-15")
print(f"Año: {m.group('año')}, Mes: {m.group('mes')}, Día: {m.group('dia')}")

# ============================================
# 3. RE.SUB — REEMPLAZAR
# ============================================
print("\n" + "=" * 55)
print("3. RE.SUB — REEMPLAZAR")
print("=" * 55)

# Ocultar número de tarjeta de crédito
tarjeta = "Mi tarjeta es 4532-1234-5678-9012 y la otra 4111-1111-1111-1111"
oculta = re.sub(r"\d{4}-\d{4}-\d{4}-(\d{4})", r"****-****-****-\1", tarjeta)
print(f"Original: {tarjeta}")
print(f"Oculta:   {oculta}")

# Normalizar espacios
texto_sucio = "Este  texto   tiene    espacios   irregulares"
texto_limpio = re.sub(r"\s+", " ", texto_sucio).strip()
print(f"\nOriginal: '{texto_sucio}'")
print(f"Limpio:   '{texto_limpio}'")

# Usar función como reemplazador
def doblar_numero(m):
    return str(int(m.group()) * 2)

resultado = re.sub(r"\d+", doblar_numero, "Hay 5 gatos y 3 perros")
print(f"\nDoblar números: '{resultado}'")

# ============================================
# 4. RE.SPLIT — DIVIDIR
# ============================================
print("\n" + "=" * 55)
print("4. RE.SPLIT — DIVIDIR")
print("=" * 55)

# Dividir por cualquier signo de puntuación
frase = "Hola, mundo; esto es Python. ¿Qué tal?"
partes = re.split(r"[;,.\s!¿?]+", frase)
partes = [p for p in partes if p]  # eliminar vacíos
print(f"Frase: '{frase}'")
print(f"Partes: {partes}")

# Dividir CSV con espacios variables
linea = "Ana  ,  28,  Madrid  ,  Ingeniería"
campos = [c.strip() for c in re.split(r"\s*,\s*", linea.strip())]
print(f"\nCSV messy: '{linea}'")
print(f"Campos:    {campos}")

# ============================================
# 5. FLAGS
# ============================================
print("\n" + "=" * 55)
print("5. FLAGS")
print("=" * 55)

texto_multi = """Primera línea con Python
segunda línea con PYTHON
tercera línea con python"""

# re.IGNORECASE
coincidencias = re.findall(r"python", texto_multi, re.IGNORECASE)
print(f"IGNORECASE: {coincidencias}")

# re.MULTILINE — ^ aplica a cada línea
lineas_que_empiezan = re.findall(r"^segunda.*$", texto_multi, re.MULTILINE)
print(f"MULTILINE (^segunda): {lineas_que_empiezan}")

# re.DOTALL — . incluye \n
bloque = "Inicio...\ncontenido intermedio\n...Fin"
m = re.search(r"Inicio(.+)Fin", bloque, re.DOTALL)
if m:
    print(f"DOTALL capturado: '{m.group(1).strip()}'")

# ============================================
# 6. LOOKAHEAD Y LOOKBEHIND
# ============================================
print("\n" + "=" * 55)
print("6. LOOKAHEAD Y LOOKBEHIND")
print("=" * 55)

precios = "Ebook: 9.99€, Curso: 49.99€, Libro: 25.00€"

# Lookahead positivo (?=...): precio seguido de €
numeros_con_euro = re.findall(r"\d+\.\d+(?=€)", precios)
print(f"Precios (lookahead €): {numeros_con_euro}")

# Lookbehind positivo (?<=...): número precedido de "Ebook: "
m = re.search(r"(?<=Ebook: )\d+\.\d+", precios)
print(f"Precio de Ebook: {m.group()}")

# ============================================
# 7. CASOS REALES: VALIDACIONES
# ============================================
print("\n" + "=" * 55)
print("7. CASOS REALES: VALIDACIONES")
print("=" * 55)

# --- Email ---
patron_email = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

emails = ["usuario@gmail.com", "invalido@", "@sinusuario.com",
          "nombre.apellido@empresa.es", "correo+tag@dominio.org"]

print("Validación de emails:")
for email in emails:
    valido = "✅" if patron_email.fullmatch(email) else "❌"
    print(f"  {valido} {email}")

# --- Teléfono ---
print("\nValidación de teléfonos:")
patron_tel = re.compile(r"(\+34[\s-]?)?\d{3}[\s.-]?\d{3}[\s.-]?\d{3}")
telefonos = ["612345678", "+34 612 345 678", "91-234-56-78", "1234", "abcdefghi"]
for tel in telefonos:
    valido = "✅" if patron_tel.fullmatch(tel) else "❌"
    print(f"  {valido} {tel}")

# --- Extraer URLs ---
print("\nExtracción de URLs:")
html = 'Visita <a href="https://python.org">Python</a> o <a href="http://docs.python.org/3/">Docs</a>'
urls = re.findall(r'href="(https?://[^"]+)"', html)
for url in urls:
    print(f"  URL encontrada: {url}")

# ============================================
# 8. RE.COMPILE — REUTILIZAR PATRONES
# ============================================
print("\n" + "=" * 55)
print("8. RE.COMPILE — REUTILIZAR PATRONES")
print("=" * 55)

# Compilar una vez, usar muchas veces (más eficiente)
patron_ip = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")

logs = [
    "Conexión desde 192.168.1.100 rechazada",
    "Acceso ok desde 10.0.0.1",
    "Sin IP aquí",
    "Múltiples: 172.16.0.1 y 8.8.8.8",
]

print("IPs encontradas en logs:")
for log in logs:
    ips = patron_ip.findall(log)
    if ips:
        print(f"  '{log}' → {ips}")
    else:
        print(f"  '{log}' → sin IP")
