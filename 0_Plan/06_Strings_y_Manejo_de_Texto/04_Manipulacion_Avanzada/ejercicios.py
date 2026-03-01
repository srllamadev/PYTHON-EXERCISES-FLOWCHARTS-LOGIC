"""
Ejercicios - Manipulación Avanzada de Strings
==============================================

Ejercicios que combinan slicing, codificación, módulos
string/textwrap y algoritmos sobre texto.
"""

import string
import textwrap
import re

print("=" * 60)
print("EJERCICIOS - MANIPULACIÓN AVANZADA DE STRINGS")
print("=" * 60)

# ============================================
# EJERCICIO 1: Operaciones con slicing
# ============================================
print("\nEJERCICIO 1: Operaciones con slicing")
print("-" * 60)
print("""
Dado el string: texto = "Python es el mejor lenguaje"

Sin usar ningún método de string (solo slicing e índices), obtén:
  a) Las últimas 8 letras
  b) Las letras en posiciones pares (índice 0, 2, 4, ...)
  c) El string al revés
  d) Las letras de la posición 7 a la 18 (inclusive), de atrás hacia adelante

Imprime cada resultado.
""")

texto = "Python es el mejor lenguaje"

# TODO a)
# TODO b)
# TODO c)
# TODO d)


# ============================================
# EJERCICIO 2: Generador de contraseñas seguras
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Generador de contraseñas seguras")
print("-" * 60)
print("""
Crea una función generar_contrasena(longitud, usar_mayus=True,
  usar_digitos=True, usar_especiales=True) que genere una
contraseña aleatoria cumpliendo los requisitos solicitados.

Además, la contraseña DEBE contener al menos:
  - 1 mayúscula (si usar_mayus=True)
  - 1 dígito (si usar_digitos=True)
  - 1 carácter especial (si usar_especiales=True)

Pista: usa string.ascii_letters, string.digits, string.punctuation
       y random.shuffle() para garantizar la distribución.

Pruébala generando 5 contraseñas de 16 caracteres.
""")

import random

def generar_contrasena(longitud=12, usar_mayus=True, usar_digitos=True, usar_especiales=True):
    # TODO: Escribe tu código aquí
    pass

# for _ in range(5):
#     print(generar_contrasena(16))


# ============================================
# EJERCICIO 3: Formateador de texto para terminal
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Formateador de texto para terminal")
print("-" * 60)
print("""
Crea una función caja_texto(titulo, contenido, ancho=60) que
genere un bloque de texto enmarcado:

╔════════════════════════════════════════════════════════════╗
║                    TÍTULO DEL CUADRO                       ║
╠════════════════════════════════════════════════════════════╣
║  El contenido se ajusta automáticamente al ancho dado,     ║
║  usando textwrap para partir las líneas largas. Cada       ║
║  línea queda alineada a la izquierda con margen.           ║
╚════════════════════════════════════════════════════════════╝

Usa textwrap.wrap() para ajustar el contenido.
""")

def caja_texto(titulo, contenido, ancho=60):
    # TODO: Escribe tu código aquí
    pass

# caja_texto(
#     "Python",
#     "Python es un lenguaje de programación de alto nivel, interpretado y de propósito general.",
#     ancho=50
# )


# ============================================
# EJERCICIO 4: Detector de palíndromos y anagramas
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Detector de palíndromos y anagramas")
print("-" * 60)
print("""
Dada una lista de palabras, encuentra:
  a) Todos los palíndromos
  b) Todos los grupos de anagramas (palabras que son anagramas entre sí)

palabras = ["amor", "roma", "arma", "mara", "nivel", "levin", "python",
            "ana", "oto", "mar", "ram", "reconocer", "roto", "toro"]
""")

palabras = ["amor", "roma", "arma", "mara", "nivel", "levin", "python",
            "ana", "oto", "mar", "ram", "reconocer", "roto", "toro"]

# TODO a) Palíndromos
# palindromos = [...]

# TODO b) Grupos de anagramas
# Pista: usa un diccionario donde la clave sea la firma (sorted letters)
# grupos = {}
# for p in palabras:
#     clave = ''.join(sorted(p.lower()))
#     ...


# ============================================
# EJERCICIO 5: Compresor RLE (Run-Length Encoding)
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 5: Compresor RLE")
print("-" * 60)
print("""
Run-Length Encoding (RLE) es una compresión simple que agrupa
caracteres consecutivos iguales:

  "aaabbbccddddee"  →  "3a3b2c4d2e"
  "abcd"            →  "1a1b1c1d"  (sin compresión si todo es distinto)

Implementa:
  comprimir_rle(texto)   → versión comprimida
  descomprimir_rle(dato) → texto original

Prueba con:
  s1 = "aaabbbccddddee"
  s2 = "AABBBCCCCDDDDDEEEEEEE"
  s3 = "Python"
""")

def comprimir_rle(texto):
    # TODO: Escribe tu código aquí
    pass

def descomprimir_rle(dato):
    # TODO: Escribe tu código aquí (pista: usa re.findall(r"(\d+)(\w)", dato))
    pass

# s1 = "aaabbbccddddee"
# s2 = "AABBBCCCCDDDDDEEEEEEE"
# s3 = "Python"
# for s in [s1, s2, s3]:
#     comp = comprimir_rle(s)
#     decomp = descomprimir_rle(comp)
#     print(f"'{s}' → '{comp}' → '{decomp}' | OK: {s == decomp}")


# ============================================
# EJERCICIO 6 (DESAFÍO): Intérprete de plantillas simple
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 6 (DESAFÍO): Intérprete de plantillas")
print("-" * 60)
print("""
Crea una función renderizar(plantilla, variables) que reemplace
tokens del tipo {{nombre}} por los valores del diccionario variables.

Si una variable no existe en el diccionario, deja el token sin cambiar.

Ejemplo:
  plantilla = "Hola, {{nombre}}! Tienes {{mensajes}} mensajes nuevos."
  variables = {"nombre": "Ana", "mensajes": "3"}
  # Resultado: "Hola, Ana! Tienes 3 mensajes nuevos."

  plantilla2 = "Hola {{nombre}}, tu código es {{codigo}}."
  variables2 = {"nombre": "Luis"}
  # Resultado: "Hola Luis, tu código es {{codigo}}."

Pista: usa re.sub() con una función como reemplazador.
""")

def renderizar(plantilla, variables):
    # TODO: Escribe tu código aquí
    pass

# plantilla = "Hola, {{nombre}}! Tienes {{mensajes}} mensajes nuevos."
# print(renderizar(plantilla, {"nombre": "Ana", "mensajes": "3"}))
# plantilla2 = "Hola {{nombre}}, tu código es {{codigo}}."
# print(renderizar(plantilla2, {"nombre": "Luis"}))


# ============================================
# SOLUCIONES (descomenta para ver)
# ============================================
"""
# SOLUCIÓN 1:
texto = "Python es el mejor lenguaje"
print(texto[-8:])            # a)
print(texto[::2])            # b)
print(texto[::-1])           # c)
print(texto[7:19][::-1])     # d)

# SOLUCIÓN 2:
def generar_contrasena(longitud=12, usar_mayus=True, usar_digitos=True, usar_especiales=True):
    pool = string.ascii_lowercase
    obligatorios = []
    if usar_mayus:
        pool += string.ascii_uppercase
        obligatorios.append(random.choice(string.ascii_uppercase))
    if usar_digitos:
        pool += string.digits
        obligatorios.append(random.choice(string.digits))
    if usar_especiales:
        pool += string.punctuation
        obligatorios.append(random.choice(string.punctuation))
    relleno = random.choices(pool, k=longitud - len(obligatorios))
    todos = obligatorios + relleno
    random.shuffle(todos)
    return ''.join(todos)

# SOLUCIÓN 3:
def caja_texto(titulo, contenido, ancho=60):
    interior = ancho - 4
    lineas_contenido = textwrap.wrap(contenido, width=interior)
    print(f"╔{'═'*(ancho-2)}╗")
    print(f"║{titulo.upper().center(ancho-2)}║")
    print(f"╠{'═'*(ancho-2)}╣")
    for linea in lineas_contenido:
        print(f"║  {linea.ljust(interior)}  ║")
    print(f"╚{'═'*(ancho-2)}╝")

# SOLUCIÓN 4:
def es_palindromo(s):
    s = re.sub(r"[^a-záéíóúñ]", "", s.lower())
    return s == s[::-1]
palindromos = [p for p in palabras if es_palindromo(p)]
print(f"Palíndromos: {palindromos}")

grupos = {}
for p in palabras:
    clave = ''.join(sorted(p.lower()))
    grupos.setdefault(clave, []).append(p)
grupos_anagramas = [v for v in grupos.values() if len(v) > 1]
print(f"Grupos anagramas: {grupos_anagramas}")

# SOLUCIÓN 5:
def comprimir_rle(texto):
    if not texto:
        return ""
    resultado = []
    count = 1
    for i in range(1, len(texto)):
        if texto[i] == texto[i-1]:
            count += 1
        else:
            resultado.append(f"{count}{texto[i-1]}")
            count = 1
    resultado.append(f"{count}{texto[-1]}")
    return ''.join(resultado)

def descomprimir_rle(dato):
    return ''.join(c * int(n) for n, c in re.findall(r"(\d+)(.)", dato))

# SOLUCIÓN 6:
def renderizar(plantilla, variables):
    def reemplazar(m):
        clave = m.group(1)
        return variables.get(clave, m.group(0))
    return re.sub(r"\{\{(\w+)\}\}", reemplazar, plantilla)
"""
