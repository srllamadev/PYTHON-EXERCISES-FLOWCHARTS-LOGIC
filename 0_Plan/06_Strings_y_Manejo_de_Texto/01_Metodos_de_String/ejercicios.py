"""
Ejercicios - Métodos de String
================================

Completa cada ejercicio usando los métodos de string de Python.
Las pistas y soluciones están al final del archivo.
"""

print("=" * 60)
print("EJERCICIOS - MÉTODOS DE STRING")
print("=" * 60)

# ============================================
# EJERCICIO 1: Normalizar datos de usuario
# ============================================
print("\nEJERCICIO 1: Normalizar datos de usuario")
print("-" * 60)
print("""
Tienes los siguientes nombres ingresados por usuarios:
nombres_raw = ["  alice SMITH  ", "BOB JONES", "  CHARLIE brown  "]

Normalízalos para que queden: "Alice Smith", "Bob Jones", "Charlie Brown"
Usa: strip() y title()
""")

nombres_raw = ["  alice SMITH  ", "BOB JONES", "  CHARLIE brown  "]

# TODO: Escribe tu código aquí

# RESULTADO ESPERADO: ['Alice Smith', 'Bob Jones', 'Charlie Brown']


# ============================================
# EJERCICIO 2: Analizador de contraseñas
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Analizador de contraseñas")
print("-" * 60)
print("""
Crea una función analizar_contrasena(password) que devuelva
un diccionario con:
  - 'longitud': número de caracteres
  - 'tiene_mayuscula': True si tiene al menos una mayúscula
  - 'tiene_digito': True si tiene al menos un dígito
  - 'es_fuerte': True si longitud >= 8 Y tiene_mayuscula Y tiene_digito

Pista: usa any(), isupper(), isdigit() en un loop, o
       métodos como .lower() != .upper() para detectar mayúsculas.
""")

def analizar_contrasena(password):
    # TODO: Escribe tu código aquí
    pass

# Pruebas:
# print(analizar_contrasena("abc"))        # débil
# print(analizar_contrasena("AbCdEf12"))   # fuerte


# ============================================
# EJERCICIO 3: Procesador de CSV simple
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Procesador de CSV simple")
print("-" * 60)
print("""
Dado el siguiente string CSV:
datos_csv = "nombre,edad,ciudad\\nAna,28,Madrid\\nLuis,35,Barcelona\\nMart,22,Valencia"

1. Divide en filas usando splitlines()
2. La primera fila son los encabezados, divídela por ','
3. Crea una lista de diccionarios con los datos de cada persona
4. Imprime cada persona con formato: "Nombre: X | Edad: Y | Ciudad: Z"
""")

datos_csv = "nombre,edad,ciudad\nAna,28,Madrid\nLuis,35,Barcelona\nMarta,22,Valencia"

# TODO: Escribe tu código aquí


# ============================================
# EJERCICIO 4: Contador de palabras
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Contador de palabras")
print("-" * 60)
print("""
Dado el texto:
texto = "el gato y el perro y el pez y el gato y el pez"

Crea un diccionario que cuente cuántas veces aparece cada palabra.
Ordena el resultado de mayor a menor frecuencia e imprímelo.

Pista: usa split(), un diccionario, y sorted() con key=lambda.
""")

texto = "el gato y el perro y el pez y el gato y el pez"

# TODO: Escribe tu código aquí


# ============================================
# EJERCICIO 5: Formatear tabla de resultados
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 5: Formatear tabla de resultados")
print("-" * 60)
print("""
Formatea la siguiente información como una tabla alineada:

estudiantes = [
    ("Ana García", 9.5),
    ("Luis Rodríguez", 7.2),
    ("Marta Sánchez López", 8.8),
    ("Pedro", 6.0),
]

Resultado esperado (ejemplo):
╔════════════════════════╦═══════╗
║ Estudiante             ║ Nota  ║
╠════════════════════════╬═══════╣
║ Ana García             ║  9.50 ║
║ Luis Rodríguez         ║  7.20 ║
║ Marta Sánchez López    ║  8.80 ║
║ Pedro                  ║  6.00 ║
╚════════════════════════╩═══════╝

Pista: usa ljust(), rjust() o f-strings con especificadores de ancho.
""")

estudiantes = [
    ("Ana García", 9.5),
    ("Luis Rodríguez", 7.2),
    ("Marta Sánchez López", 8.8),
    ("Pedro", 6.0),
]

# TODO: Escribe tu código aquí


# ============================================
# EJERCICIO 6 (DESAFÍO): Slugify
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 6 (DESAFÍO): Slugify")
print("-" * 60)
print("""
Crea una función slugify(texto) que convierta un título
en un 'slug' apto para URLs:

slugify("Hola Mundo Python!")   -> "hola-mundo-python"
slugify("  Título del Artículo  ") -> "titulo-del-articulo"
slugify("Python 3.12 es genial!!") -> "python-3-12-es-genial"

Reglas:
 1. Todo a minúsculas
 2. Eliminar caracteres no alfanuméricos (excepto espacios)
 3. Reemplazar espacios (y múltiples espacios) por guiones
 4. Eliminar guiones al inicio y al final

Pista: puedes usar replace() en un loop o join/split.
       Para acentos: considera usar str.maketrans() o simplemente
       reemplazar letras acentuadas manualmente.
""")

def slugify(texto):
    # TODO: Escribe tu código aquí
    pass

# Pruebas:
# print(slugify("Hola Mundo Python!"))
# print(slugify("  Título del Artículo  "))
# print(slugify("Python 3.12 es genial!!"))


# ============================================
# SOLUCIONES (descomenta para ver)
# ============================================

"""
# SOLUCIÓN 1:
nombres_normalizados = [n.strip().title() for n in nombres_raw]
print(nombres_normalizados)

# SOLUCIÓN 2:
def analizar_contrasena(password):
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_digito = any(c.isdigit() for c in password)
    longitud = len(password)
    return {
        'longitud': longitud,
        'tiene_mayuscula': tiene_mayuscula,
        'tiene_digito': tiene_digito,
        'es_fuerte': longitud >= 8 and tiene_mayuscula and tiene_digito
    }

# SOLUCIÓN 3:
filas = datos_csv.splitlines()
encabezados = filas[0].split(',')
personas = []
for fila in filas[1:]:
    valores = fila.split(',')
    personas.append(dict(zip(encabezados, valores)))
for p in personas:
    print(f"Nombre: {p['nombre']} | Edad: {p['edad']} | Ciudad: {p['ciudad']}")

# SOLUCIÓN 4:
conteo = {}
for palabra in texto.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
for palabra, n in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
    print(f"{palabra}: {n}")

# SOLUCIÓN 5:
ancho_nombre = 22
print(f"╔{'═'*(ancho_nombre+2)}╦{'═'*7}╗")
print(f"║ {'Estudiante'.ljust(ancho_nombre)} ║ {'Nota':>5} ║")
print(f"╠{'═'*(ancho_nombre+2)}╬{'═'*7}╣")
for nombre, nota in estudiantes:
    print(f"║ {nombre.ljust(ancho_nombre)} ║ {nota:>5.2f} ║")
print(f"╚{'═'*(ancho_nombre+2)}╩{'═'*7}╝")

# SOLUCIÓN 6:
def slugify(texto):
    texto = texto.strip().lower()
    resultado = []
    for c in texto:
        if c.isalnum():
            resultado.append(c)
        elif c in (' ', '-', '_'):
            resultado.append(' ')
        # ignorar resto
    slug = '-'.join(resultado)
    # Limpiar guiones múltiples
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug.strip('-')
"""
