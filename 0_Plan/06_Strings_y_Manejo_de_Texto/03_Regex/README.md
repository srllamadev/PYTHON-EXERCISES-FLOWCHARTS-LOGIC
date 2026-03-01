# 03 - Expresiones Regulares (Regex)

## Objetivos de Aprendizaje
- Entender qué son las expresiones regulares y para qué sirven
- Manejar el módulo `re` de Python
- Construir patrones para buscar, validar y transformar texto
- Aplicar regex a problemas reales (emails, teléfonos, URLs, etc.)

---

## ¿Qué es una Expresión Regular?

Una **expresión regular** (regex / regexp) es un patrón de texto que describe un conjunto de strings. Permiten buscar, validar y transformar texto de forma poderosa y concisa.

```python
import re

# ¿Es un email válido?
patron = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email = "usuario@ejemplo.com"
if re.match(patron, email):
    print("Email válido")
```

---

## El Módulo `re`

```python
import re
```

### Funciones Principales

| Función | Descripción |
|---|---|
| `re.match(patron, texto)` | Busca el patrón solo al **inicio** del texto |
| `re.search(patron, texto)` | Busca el patrón en **cualquier parte** del texto |
| `re.findall(patron, texto)` | Retorna **todas** las coincidencias como lista |
| `re.finditer(patron, texto)` | Retorna **iterador** de objetos `Match` |
| `re.sub(patron, reemplazo, texto)` | **Reemplaza** coincidencias |
| `re.split(patron, texto)` | **Divide** el texto por el patrón |
| `re.compile(patron)` | **Compila** el patrón (más eficiente en loops) |
| `re.fullmatch(patron, texto)` | El patrón debe coincidir con el texto **completo** |

---

## Sintaxis de Patrones

### Caracteres Especiales (Metacaracteres)

| Símbolo | Significado | Ejemplo |
|---|---|---|
| `.` | Cualquier carácter (excepto `\n`) | `a.b` → "axb", "a1b" |
| `^` | Inicio del string | `^Hola` |
| `$` | Fin del string | `mundo$` |
| `*` | 0 o más veces | `ab*` → "a", "ab", "abb" |
| `+` | 1 o más veces | `ab+` → "ab", "abb" |
| `?` | 0 o 1 vez (opcional) | `colou?r` → "color", "colour" |
| `{n}` | Exactamente n veces | `\d{4}` → "2024" |
| `{n,m}` | Entre n y m veces | `\d{2,4}` |
| `\|` | Alternativa (OR) | `cat\|dog` |
| `()` | Grupo de captura | `(ab)+` |
| `[]` | Clase de caracteres | `[aeiou]` |
| `[^]` | Clase negada | `[^0-9]` |
| `\` | Escape | `\.` → punto literal |

---

### Secuencias Especiales

| Secuencia | Equivale a | Descripción |
|---|---|---|
| `\d` | `[0-9]` | Dígito |
| `\D` | `[^0-9]` | No dígito |
| `\w` | `[a-zA-Z0-9_]` | Carácter de palabra |
| `\W` | `[^a-zA-Z0-9_]` | No carácter de palabra |
| `\s` | `[ \t\n\r\f\v]` | Espacio en blanco |
| `\S` | `[^ \t\n\r\f\v]` | No espacio |
| `\b` | — | Límite de palabra |
| `\B` | — | No límite de palabra |

---

### Grupos y Capturas

```python
# Grupo simple
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Fecha: 2024-03-15")
if m:
    año, mes, dia = m.groups()
    print(f"Año={año}, Mes={mes}, Día={dia}")

# Grupo con nombre
m = re.search(r"(?P<año>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})", "2024-03-15")
if m:
    print(m.group("año"), m.group("mes"), m.group("dia"))

# Grupo no capturante
re.findall(r"(?:https?|ftp)://(\S+)", "http://python.org ftp://ejemplo.com")
```

---

### Flags (Modificadores)

| Flag | Descripción |
|---|---|
| `re.IGNORECASE` / `re.I` | No distingue mayúsculas/minúsculas |
| `re.MULTILINE` / `re.M` | `^` y `$` aplican a cada línea |
| `re.DOTALL` / `re.S` | `.` también coincide con `\n` |
| `re.VERBOSE` / `re.X` | Permite comentarios en el patrón |

```python
# Verbose: patrón legible con comentarios
patron_email = re.compile(r"""
    [a-zA-Z0-9._%+-]+   # parte local
    @                    # arroba
    [a-zA-Z0-9.-]+      # dominio
    \.                   # punto
    [a-zA-Z]{2,}         # TLD
""", re.VERBOSE)
```

---

## Patrones Comunes

```python
# Email
r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Teléfono español
r"\+?34[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}"

# URL
r"https?://[^\s]+"

# Fecha (DD/MM/YYYY o DD-MM-YYYY)
r"\d{2}[/-]\d{2}[/-]\d{4}"

# Código postal español
r"\b[0-9]{5}\b"

# IP v4
r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
```

---

## Archivos del Módulo

- [`ejemplo.py`](ejemplo.py) — Demostraciones ejecutables
- [`ejercicios.py`](ejercicios.py) — Ejercicios para practicar

## Recurso Externo
- [regex101.com](https://regex101.com/) — Prueba y depura tus patrones interactivamente (selecciona Python)
