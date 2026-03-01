"""
Ejercicios - Expresiones Regulares (Regex)
==========================================

Practica el uso del módulo 're' con problemas reales.
"""

import re

print("=" * 60)
print("EJERCICIOS - EXPRESIONES REGULARES")
print("=" * 60)

# ============================================
# EJERCICIO 1: Extraer información de un texto
# ============================================
print("\nEJERCICIO 1: Extraer información de un texto")
print("-" * 60)
print("""
Del siguiente texto, extrae:
  a) Todos los números (enteros y decimales)
  b) Todas las fechas en formato DD/MM/YYYY
  c) Todas las palabras que empiecen con mayúscula

texto = "El 15/03/2024 llegaron 42 paquetes. El coste fue 1250.99€.
         El 20/03/2024 se enviaron 18 más. Marta y Luis firmaron el albarán."
""")

texto = ("El 15/03/2024 llegaron 42 paquetes. El coste fue 1250.99€. "
         "El 20/03/2024 se enviaron 18 más. Marta y Luis firmaron el albarán.")

# TODO a) Todos los números (42, 1250.99, 18, etc.)
numeros = None  # re.findall(...)
# print(f"Números: {numeros}")

# TODO b) Fechas DD/MM/YYYY
fechas = None   # re.findall(...)
# print(f"Fechas: {fechas}")

# TODO c) Palabras que empiecen con mayúscula
mayusculas = None  # re.findall(...)
# print(f"Mayúsculas: {mayusculas}")


# ============================================
# EJERCICIO 2: Validador de formulario
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Validador de formulario")
print("-" * 60)
print("""
Crea una función validar_campo(tipo, valor) que retorne True/False:
  - tipo="email":    formato válido de email
  - tipo="telefono": número español (9 dígitos, puede empezar con +34)
  - tipo="cp":       código postal español (5 dígitos)
  - tipo="dni":      DNI español: 8 dígitos + 1 letra (ej: 12345678A)

Pruébala con valores válidos e inválidos.
""")

def validar_campo(tipo, valor):
    patrones = {
        "email":    r"",  # TODO: escribe el patrón
        "telefono": r"",  # TODO: escribe el patrón
        "cp":       r"",  # TODO: escribe el patrón
        "dni":      r"",  # TODO: escribe el patrón
    }
    patron = patrones.get(tipo)
    if not patron:
        return False
    return bool(re.fullmatch(patron, valor))

# Pruebas:
# print(validar_campo("email", "user@gmail.com"))      # True
# print(validar_campo("email", "invalido@"))            # False
# print(validar_campo("telefono", "+34 612 345 678"))   # True
# print(validar_campo("telefono", "1234"))              # False
# print(validar_campo("cp", "28001"))                   # True
# print(validar_campo("cp", "1234"))                    # False
# print(validar_campo("dni", "12345678A"))              # True
# print(validar_campo("dni", "1234A"))                  # False


# ============================================
# EJERCICIO 3: Parser de log
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Parser de log")
print("-" * 60)
print("""
Parsea el siguiente log de servidor web y extrae:
  - Fecha y hora
  - Método HTTP (GET, POST, etc.)
  - Ruta
  - Código de estado
  - Tamaño en bytes

Crea una lista de diccionarios, uno por línea de log.

FORMATO: [DD/Mon/YYYY:HH:MM:SS] "METODO /ruta HTTP/1.1" CODIGO BYTES
""")

log = """127.0.0.1 - - [15/Mar/2024:10:22:11] "GET /index.html HTTP/1.1" 200 1024
192.168.1.5 - - [15/Mar/2024:10:22:15] "POST /login HTTP/1.1" 302 0
10.0.0.1 - - [15/Mar/2024:10:22:20] "GET /static/style.css HTTP/1.1" 200 4096
8.8.8.8 - - [15/Mar/2024:10:22:25] "GET /no-existe HTTP/1.1" 404 512"""

# TODO: usa re.finditer o re.findall con grupos para parsear cada línea
# patron = re.compile(r"...")
# registros = []
# for m in patron.finditer(log):
#     registros.append({...})


# ============================================
# EJERCICIO 4: Limpiador de texto
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Limpiador de texto")
print("-" * 60)
print("""
Crea una función limpiar_texto(texto) que:
  1. Elimine etiquetas HTML (<p>, </b>, <a href="...">, etc.)
  2. Reemplace múltiples espacios/saltos de línea por un solo espacio
  3. Elimine caracteres especiales (excepto . , ! ? ¡ ¿ y letras/números)
  4. Aplique strip() al resultado

html_sucio = "<h1>Bienvenidos</h1><p>Este es un <b>texto</b> de ejemplo.</p>"
# Resultado esperado: "Bienvenidos Este es un texto de ejemplo."
""")

def limpiar_texto(texto):
    # TODO: Escribe tu código aquí
    pass

html_sucio = "<h1>Bienvenidos</h1><p>Este es un <b>texto</b> de ejemplo.</p>"
# print(limpiar_texto(html_sucio))


# ============================================
# EJERCICIO 5 (DESAFÍO): Extractor de datos estructurados
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 5 (DESAFÍO): Extractor de datos")
print("-" * 60)
print("""
Del siguiente texto de un perfil de usuario, extrae todos los
datos y devuélvelos en un diccionario:

perfil = '''
  Nombre: Juan García López
  Email: j.garcia@empresa.es
  Teléfono: +34 612 345 678
  Fecha de nacimiento: 15/08/1990
  Salario: 45.000,00€
  Departamento: Tecnología e Innovación
'''

Resultado esperado:
{
  "nombre": "Juan García López",
  "email": "j.garcia@empresa.es",
  "telefono": "+34 612 345 678",
  "fecha_nacimiento": "15/08/1990",
  "salario": "45.000,00",
  "departamento": "Tecnología e Innovación"
}

Pista: usa re.search con grupos nombrados (?P<nombre>...) 
       o re.findall para cada campo individualmente.
""")

perfil = """
  Nombre: Juan García López
  Email: j.garcia@empresa.es
  Teléfono: +34 612 345 678
  Fecha de nacimiento: 15/08/1990
  Salario: 45.000,00€
  Departamento: Tecnología e Innovación
"""

def extraer_perfil(texto):
    # TODO: Escribe tu código aquí
    pass

# print(extraer_perfil(perfil))


# ============================================
# SOLUCIONES (descomenta para ver)
# ============================================
"""
# SOLUCIÓN 1:
numeros = re.findall(r"\d+(?:\.\d+)?", texto)
fechas = re.findall(r"\d{2}/\d{2}/\d{4}", texto)
mayusculas = re.findall(r"\b[A-ZÁÉÍÓÚ][a-záéíóúñ]+", texto)

# SOLUCIÓN 2:
def validar_campo(tipo, valor):
    patrones = {
        "email":    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "telefono": r"(\+34[\s-]?)?\d{3}[\s.-]?\d{3}[\s.-]?\d{3}",
        "cp":       r"\d{5}",
        "dni":      r"\d{8}[A-Za-z]",
    }
    patron = patrones.get(tipo)
    if not patron:
        return False
    return bool(re.fullmatch(patron, valor))

# SOLUCIÓN 3:
patron = re.compile(
    r'\[(\d{2}/\w+/\d{4}:\d{2}:\d{2}:\d{2})\] '
    r'"(\w+) (/\S*) HTTP/\d\.\d" (\d{3}) (\d+)'
)
registros = []
for m in patron.finditer(log):
    registros.append({
        "fecha": m.group(1), "metodo": m.group(2),
        "ruta": m.group(3), "estado": int(m.group(4)),
        "bytes": int(m.group(5))
    })
for r in registros:
    print(r)

# SOLUCIÓN 4:
def limpiar_texto(texto):
    sin_html = re.sub(r"<[^>]+>", " ", texto)
    sin_extra = re.sub(r"\s+", " ", sin_html)
    limpio = re.sub(r"[^\w\s.,!?¡¿áéíóúüñÁÉÍÓÚÜÑ]", "", sin_extra)
    return limpio.strip()

# SOLUCIÓN 5:
def extraer_perfil(texto):
    campos = {
        "nombre":   r"Nombre:\s*(.+)",
        "email":    r"Email:\s*(\S+)",
        "telefono": r"Teléfono:\s*(.+)",
        "fecha_nacimiento": r"Fecha de nacimiento:\s*(\d{2}/\d{2}/\d{4})",
        "salario":  r"Salario:\s*([\d.,]+)€",
        "departamento": r"Departamento:\s*(.+)",
    }
    resultado = {}
    for clave, patron in campos.items():
        m = re.search(patron, texto)
        resultado[clave] = m.group(1).strip() if m else None
    return resultado
"""
