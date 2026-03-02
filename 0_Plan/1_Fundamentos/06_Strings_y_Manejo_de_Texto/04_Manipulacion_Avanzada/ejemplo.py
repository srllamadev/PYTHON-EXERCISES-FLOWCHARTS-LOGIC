"""
Manipulación Avanzada de Strings en Python
============================================

Ejemplos ejecutables de técnicas avanzadas de manejo de texto:
  - Slicing avanzado
  - Raw strings y multilínea
  - Codificación/decodificación
  - Módulos string y textwrap
  - Algoritmos sobre strings
  - str.maketrans / translate
"""

import string
import textwrap

# ============================================
# 1. SLICING AVANZADO
# ============================================
print("=" * 55)
print("1. SLICING AVANZADO")
print("=" * 55)

s = "Python Programming"
print(f"String: '{s}'")
print(f"s[0:6]:    '{s[0:6]}'     — 'Python'")
print(f"s[7:]:     '{s[7:]}'  — 'Programming'")
print(f"s[:6]:     '{s[:6]}'     — 'Python'")
print(f"s[-11:]:   '{s[-11:]}' — 'Programming'")
print(f"s[::2]:    '{s[::2]}'   — cada 2 chars")
print(f"s[::-1]:   '{s[::-1]}' — invertido")
print(f"s[7:18:2]: '{s[7:18:2]}'   — Programming cada 2")

# Trucos útiles con slicing
print("\n--- Trucos ---")
texto = "¡Hola, Mundo!"
print(f"Sin primer y último char: '{texto[1:-1]}'")
print(f"Últimos 5 chars: '{texto[-5:]}'")
print(f"Invertir palabras: {texto.split()[::-1]}")

# ============================================
# 2. RAW STRINGS
# ============================================
print("\n" + "=" * 55)
print("2. RAW STRINGS")
print("=" * 55)

# Problema con backslashes
print("Ruta CON problema:  C:\\Users\\nombre\\Desktop")
print(r"Ruta SIN problema: C:\Users\nombre\Desktop")

# Raw string en regex
import re
texto = "precio: 3.14 y tasa: 0.05"
# Sin raw: \\d+ (doble backslash necesario)
numeros_sin_raw = re.findall("\\d+\\.\\d+", texto)
# Con raw: \d+ (más limpio y legible)
numeros_con_raw = re.findall(r"\d+\.\d+", texto)
print(f"findall sin raw: {numeros_sin_raw}")
print(f"findall con raw: {numeros_con_raw}")

# ============================================
# 3. STRINGS MULTILÍNEA
# ============================================
print("\n" + "=" * 55)
print("3. STRINGS MULTILÍNEA")
print("=" * 55)

# Triple comillas
poema = """Caminante, son tus huellas
el camino y nada más;
caminante, no hay camino,
se hace camino al andar."""
print(poema)

# Número de líneas
lineas = poema.splitlines()
print(f"Número de líneas: {len(lineas)}")

# Concatenación implícita (sin + ni \)
query = (
    "SELECT id, nombre, email "
    "FROM usuarios "
    "WHERE activo = 1 "
    "ORDER BY nombre ASC"
)
print(f"\nSQL en una línea:\n{query}")

# ============================================
# 4. CODIFICACIÓN Y DECODIFICACIÓN
# ============================================
print("\n" + "=" * 55)
print("4. CODIFICACIÓN Y DECODIFICACIÓN")
print("=" * 55)

texto_unicode = "Hola, ñoño 🐍"
print(f"Texto original: '{texto_unicode}'")

encodings = ["utf-8", "utf-16", "latin-1"]
for enc in encodings:
    try:
        encoded = texto_unicode.encode(enc)
        decoded = encoded.decode(enc)
        print(f"  {enc:10}: {len(encoded):3} bytes → '{decoded}'")
    except (UnicodeEncodeError, UnicodeDecodeError) as e:
        print(f"  {enc:10}: ERROR - {e}")

# Estrategias de manejo de errores
print("\nEstrategias de encode con ASCII:")
for strategy in ["strict", "ignore", "replace", "xmlcharrefreplace"]:
    try:
        result = texto_unicode.encode("ascii", errors=strategy)
        print(f"  {strategy:20}: {result}")
    except UnicodeEncodeError as e:
        print(f"  {strategy:20}: UnicodeEncodeError")

# ============================================
# 5. MÓDULO STRING — CONSTANTES
# ============================================
print("\n" + "=" * 55)
print("5. MÓDULO STRING — CONSTANTES Y UTILIDADES")
print("=" * 55)

print(f"ascii_lowercase: '{string.ascii_lowercase}'")
print(f"ascii_uppercase: '{string.ascii_uppercase}'")
print(f"digits:          '{string.digits}'")
print(f"hexdigits:       '{string.hexdigits}'")
print(f"punctuation:     '{string.punctuation}'")

# Aplicación: generar contraseña segura aleatoria
import random

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(caracteres, k=longitud))

print(f"\nContraseñas generadas:")
for _ in range(3):
    print(f"  {generar_contrasena()}")

# Verificar si un string tiene solo caracteres válidos
nombre_usuario = "usuario_123"
validos = string.ascii_letters + string.digits + "_"
print(f"\n'{nombre_usuario}' es válido: {all(c in validos for c in nombre_usuario)}")
print(f"'usuario 123' es válido: {all(c in validos for c in 'usuario 123')}")

# ============================================
# 6. MÓDULO TEXTWRAP
# ============================================
print("\n" + "=" * 55)
print("6. MÓDULO TEXTWRAP")
print("=" * 55)

parrafo = ("Python es un lenguaje de programación de alto nivel, "
           "de propósito general, que prioriza la legibilidad del código. "
           "Fue creado por Guido van Rossum y su primera versión fue lanzada en 1991.")

print("--- textwrap.fill (ancho=50) ---")
print(textwrap.fill(parrafo, width=50))

print("\n--- textwrap.fill con indent ---")
print(textwrap.fill(parrafo, width=50, initial_indent="  >> ", subsequent_indent="     "))

print("\n--- textwrap.indent ---")
codigo = "def saludar():\n    print('Hola')\n\nsaludar()"
indentado = textwrap.indent(codigo, "    ")
print(indentado)

# ============================================
# 7. STR.MAKETRANS Y TRANSLATE
# ============================================
print("\n" + "=" * 55)
print("7. STR.MAKETRANS Y TRANSLATE")
print("=" * 55)

texto = "Héllo, Múndo! ¿Cómo estás?"

# 1. Eliminar caracteres completamente
sin_puntuacion = texto.translate(str.maketrans("", "", string.punctuation + "¿¡"))
print(f"Sin puntuación: '{sin_puntuacion}'")

# 2. Remover acentos (mapeo manual)
tabla_acentos = str.maketrans(
    "áéíóúüñÁÉÍÓÚÜÑ",
    "aeiouunAEIOUUN"
)
sin_acentos = texto.translate(tabla_acentos)
print(f"Sin acentos:    '{sin_acentos}'")

# 3. Cifrado ROT13 con translate
abecedario = string.ascii_lowercase + string.ascii_uppercase
rot13 = abecedario[13:26] + abecedario[:13] + abecedario[39:] + abecedario[26:39]
tabla_rot13 = str.maketrans(abecedario, rot13)
mensaje = "Hola Python"
cifrado = mensaje.translate(tabla_rot13)
descifrado = cifrado.translate(tabla_rot13)
print(f"\nROT13:")
print(f"  Original:  '{mensaje}'")
print(f"  Cifrado:   '{cifrado}'")
print(f"  Descifrado:'{descifrado}'")

# ============================================
# 8. ALGORITMOS CLÁSICOS
# ============================================
print("\n" + "=" * 55)
print("8. ALGORITMOS CLÁSICOS")
print("=" * 55)

# --- Palíndromo ---
def es_palindromo(s):
    limpio = re.sub(r"[^a-zA-Z0-9áéíóúüñÁÉÍÓÚÜÑ]", "", s).lower()
    return limpio == limpio[::-1]

pruebas_palindromo = [
    "Ana", "A man a plan a canal Panama",
    "Reconocer", "Python", "Yo soy", "Anita lava la tina"
]
print("Palíndromos:")
for p in pruebas_palindromo:
    resultado = "✅ Sí" if es_palindromo(p) else "❌ No"
    print(f"  {resultado}: '{p}'")

# --- Anagrama ---
def es_anagrama(a, b):
    normalizar = lambda s: sorted(s.lower().replace(" ", ""))
    return normalizar(a) == normalizar(b)

pares = [("escuchar", "uchares"), ("Python", "typhon"), ("Hola", "Adios")]
print("\nAnagramas:")
for a, b in pares:
    resultado = "✅ Sí" if es_anagrama(a, b) else "❌ No"
    print(f"  {resultado}: '{a}' <-> '{b}'")

# --- Cifrado César ---
def cifrar_cesar(texto, n):
    resultado = []
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            c = chr((ord(c) - base + n) % 26 + base)
        resultado.append(c)
    return ''.join(resultado)

mensaje = "Hola Python!"
cifrado = cifrar_cesar(mensaje, 3)
descifrado = cifrar_cesar(cifrado, -3)
print(f"\nCifrado César (n=3):")
print(f"  Original:  '{mensaje}'")
print(f"  Cifrado:   '{cifrado}'")
print(f"  Descifrado:'{descifrado}'")
