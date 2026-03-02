# 04 - Manipulación Avanzada de Strings

## Objetivos de Aprendizaje
- Dominar el slicing de strings con paso inverso
- Trabajar con raw strings, strings multilínea y codificaciones
- Usar el módulo `string` y `textwrap`
- Implementar algoritmos clásicos sobre strings
- Procesar texto estructurado sin librerías externas

---

## 1. Slicing de Strings

La sintaxis es `s[inicio:fin:paso]`. Los índices negativos cuentan desde el final.

```python
s = "Python"
#    0123456
#   -6-5-4-3-2-1

print(s[0:3])    # "Pyt"
print(s[2:])     # "thon"
print(s[:4])     # "Pyth"
print(s[-3:])    # "hon"
print(s[::2])    # "Pto"   — cada 2 caracteres
print(s[::-1])   # "nohtyP" — invertir
```

---

## 2. Raw Strings

Un **raw string** (`r"..."`) trata las barras invertidas `\` como literales:

```python
# Sin raw string — \n y \t son interpretados
path = "C:\nuevos\archivos\test.txt"
print(path)    # ¡Problema! \n y \a se interpretan

# Con raw string — seguro para rutas y regex
path = r"C:\nuevos\archivos\test.txt"
print(path)    # C:\nuevos\archivos\test.txt (correcto)

# En regex SIEMPRE usar raw strings
import re
re.search(r"\d+\.\d+", "3.14")   # correcto
```

---

## 3. Strings Multilínea

```python
# Con triple comillas """ o '''
texto = """Primera línea
Segunda línea
Tercera línea"""

# Con \ para continuar en la siguiente línea
sql = ("SELECT nombre, edad "
       "FROM usuarios "
       "WHERE edad > 18")
```

---

## 4. Codificación / Decodificación

```python
# str -> bytes
texto = "Hola, ñoño 🐍"
encoded = texto.encode("utf-8")
print(encoded)    # b'Hola, \xc3\xb1o\xc3\xb1o \xf0\x9f\x90\x8d'
print(type(encoded))  # <class 'bytes'>

# bytes -> str
decoded = encoded.decode("utf-8")
print(decoded)    # "Hola, ñoño 🐍"

# Encode/decode con manejo de errores
texto.encode("ascii", errors="ignore")   # ignora caracteres no ASCII
texto.encode("ascii", errors="replace")  # reemplaza con ?
```

---

## 5. Módulo `string`

```python
import string

print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)           # '0123456789'
print(string.punctuation)      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)       # ' \t\n\r\x0b\x0c'

# Útil para generar contraseñas o validar
caracteres_validos = string.ascii_letters + string.digits
```

---

## 6. Módulo `textwrap`

```python
import textwrap

parrafo = ("Python es un lenguaje de programación de alto nivel, "
           "interpretado y de propósito general que fue diseñado "
           "para ser fácil de leer y escribir.")

# Ajustar a 40 caracteres de ancho
print(textwrap.fill(parrafo, width=40))

# Obtener lista de líneas
lineas = textwrap.wrap(parrafo, width=40)

# Indentar texto
texto_indentado = textwrap.indent(parrafo, prefix="    ")

# Desindentar
textwrap.dedent(texto_con_sangria)
```

---

## 7. Algoritmos Clásicos sobre Strings

### Palíndromo
```python
def es_palindromo(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

### Anagrama
```python
def es_anagrama(a, b):
    return sorted(a.lower()) == sorted(b.lower())
```

### Cifrado César
```python
def cifrar_cesar(texto, desplazamiento):
    resultado = []
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            c = chr((ord(c) - base + desplazamiento) % 26 + base)
        resultado.append(c)
    return ''.join(resultado)
```

---

## 8. `str.maketrans()` y `translate()`

Reemplazos de caracteres a nivel de tabla (muy eficiente):

```python
# Eliminar vocales
tabla = str.maketrans("aeiouáéíóúAEIOU", "               ")
print("Hola Mundo".translate(tabla))   # "Hl  Mnd "

# O eliminar caracteres completamente
tabla = str.maketrans("", "", "aeiouáéíóú")
print("Hola Mundo".translate(tabla))   # "Hl Mnd"
```

---

## Archivos del Módulo

- [`ejemplo.py`](ejemplo.py) — Demostraciones ejecutables
- [`ejercicios.py`](ejercicios.py) — Ejercicios para practicar
