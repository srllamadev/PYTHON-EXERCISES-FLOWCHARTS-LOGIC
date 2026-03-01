"""
Métodos de String en Python
============================

Este archivo contiene ejemplos ejecutables que demuestran
los principales métodos de las cadenas de texto en Python.
"""

# ============================================
# 1. TRANSFORMACIÓN DE CASO
# ============================================
print("=" * 55)
print("1. TRANSFORMACIÓN DE CASO")
print("=" * 55)

texto = "hola mundo desde python"

print(f"Original:    '{texto}'")
print(f"upper():     '{texto.upper()}'")
print(f"lower():     '{texto.lower()}'")
print(f"title():     '{texto.title()}'")
print(f"capitalize():'{texto.capitalize()}'")
print(f"swapcase():  '{texto.swapcase()}'")

# ============================================
# 2. BÚSQUEDA Y VERIFICACIÓN
# ============================================
print("\n" + "=" * 55)
print("2. BÚSQUEDA Y VERIFICACIÓN")
print("=" * 55)

frase = "El zorro marrón salta sobre el perro perezoso"

print(f"Texto: '{frase}'")
print(f"find('marrón'):       {frase.find('marrón')}")
print(f"find('gato'):         {frase.find('gato')}  <- -1 = no encontrado")
print(f"count('el'):          {frase.lower().count('el')}")
print(f"startswith('El'):     {frase.startswith('El')}")
print(f"endswith('perezoso'): {frase.endswith('perezoso')}")
print(f"'salta' in frase:     {'salta' in frase}")

# ============================================
# 3. DIVISIÓN Y UNIÓN
# ============================================
print("\n" + "=" * 55)
print("3. DIVISIÓN Y UNIÓN (split / join)")
print("=" * 55)

csv_line = "Ana,28,Madrid,Ingeniería"
partes = csv_line.split(",")
print(f"Cadena CSV: '{csv_line}'")
print(f"split(','):  {partes}")
print(f"Nombre: {partes[0]}, Edad: {partes[1]}, Ciudad: {partes[2]}")

# join: el separador llama a join con la lista
palabras = ["Hola", "mundo", "Python"]
print(f"\nLista: {palabras}")
print(f"join con espacio: '{' '.join(palabras)}'")
print(f"join con guiones: '{'-'.join(palabras)}'")
print(f"join sin sep:     '{''.join(palabras)}'")

# partition
ruta = "usuario:contraseña@servidor"
antes, sep, despues = ruta.partition("@")
print(f"\npartition('@') en '{ruta}':")
print(f"  antes='{antes}', sep='{sep}', después='{despues}'")

# ============================================
# 4. LIMPIEZA DE STRINGS
# ============================================
print("\n" + "=" * 55)
print("4. LIMPIEZA DE STRINGS")
print("=" * 55)

sucio = "   \t  texto con espacios  \n  "
print(f"Original repr: {repr(sucio)}")
print(f"strip():       '{sucio.strip()}'")
print(f"lstrip():      '{sucio.lstrip()}'")
print(f"rstrip():      repr={repr(sucio.rstrip())}")

# replace
codigo = "int main() { return 0; }"
print(f"\nOriginal: '{codigo}'")
print(f"replace('int', 'void'): '{codigo.replace('int', 'void')}'")

# Caso real: normalizar input del usuario
entrada_usuario = "   MADRID   "
ciudad_normalizada = entrada_usuario.strip().title()
print(f"\nInput usuario: '{entrada_usuario}'")
print(f"Normalizado:   '{ciudad_normalizada}'")

# ============================================
# 5. VERIFICACIÓN DE CONTENIDO
# ============================================
print("\n" + "=" * 55)
print("5. VERIFICACIÓN DE CONTENIDO")
print("=" * 55)

muestras = ["Hola", "12345", "Python3", "   ", "MAYUS", "título"]

for s in muestras:
    print(f"'{s:10}' -> isalpha={s.isalpha()!s:5} | isdigit={s.isdigit()!s:5} | "
          f"isalnum={s.isalnum()!s:5} | isspace={s.isspace()!s:5} | isupper={s.isupper()!s:5}")

# Uso práctico: validar un PIN numérico
def validar_pin(pin):
    if len(pin) == 4 and pin.isdigit():
        return "PIN válido"
    return "PIN inválido (debe ser 4 dígitos)"

print(f"\nvalidar_pin('1234'): {validar_pin('1234')}")
print(f"validar_pin('12ab'): {validar_pin('12ab')}")
print(f"validar_pin('123'):  {validar_pin('123')}")

# ============================================
# 6. ALINEACIÓN Y RELLENO
# ============================================
print("\n" + "=" * 55)
print("6. ALINEACIÓN Y RELLENO")
print("=" * 55)

# Crear una tabla simple
productos = [("Manzana", 1.20), ("Naranja", 0.85), ("Plátano", 0.60)]
print(f"{'Producto':<15} {'Precio':>8}")
print("-" * 25)
for nombre, precio in productos:
    print(f"{nombre:<15} {precio:>8.2f}€")

# center para títulos decorativos
titulo = "MENÚ"
print(f"\n{titulo.center(30, '=')}")

# zfill para números con ceros
for n in [1, 12, 123]:
    print(f"Número {n} con zfill(5): {str(n).zfill(5)}")

# ============================================
# 7. ENCADENAMIENTO DE MÉTODOS
# ============================================
print("\n" + "=" * 55)
print("7. ENCADENAMIENTO DE MÉTODOS")
print("=" * 55)

# Normalizar nombres de usuario
nombres_raw = ["  alice  ", "BOB", "  Charlie  ", "diana"]
nombres_limpios = [n.strip().title() for n in nombres_raw]
print(f"Nombres raw:    {nombres_raw}")
print(f"Nombres limpios:{nombres_limpios}")

# Procesar un bloque de texto: tokenizar y filtrar
texto_raw = "  Python es  genial,  aprende Python  hoy  "
palabras_unicas = set(texto_raw.strip().lower().replace(",", "").split())
print(f"\nTexto raw: '{texto_raw}'")
print(f"Palabras únicas: {sorted(palabras_unicas)}")
