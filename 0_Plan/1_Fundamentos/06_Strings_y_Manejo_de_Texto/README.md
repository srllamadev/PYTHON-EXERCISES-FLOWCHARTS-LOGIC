# 06 - Strings y Manejo de Texto

## Descripción General

Los strings (cadenas de texto) son uno de los tipos de datos más utilizados en Python. Este módulo cubre desde los métodos básicos hasta las expresiones regulares y técnicas avanzadas de manipulación de texto.

## Estructura del Módulo

### 📁 [01_Metodos_de_String](01_Metodos_de_String/)
Explora el amplio conjunto de métodos integrados que ofrece Python para trabajar con cadenas.

**Temas clave:**
- Métodos de búsqueda: `find()`, `index()`, `count()`, `startswith()`, `endswith()`
- Métodos de transformación: `upper()`, `lower()`, `title()`, `capitalize()`, `swapcase()`
- Métodos de limpieza: `strip()`, `lstrip()`, `rstrip()`, `replace()`
- Métodos de división/unión: `split()`, `rsplit()`, `join()`, `partition()`
- Métodos de verificación: `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`
- Alineación y relleno: `center()`, `ljust()`, `rjust()`, `zfill()`

---

### 📁 [02_Formateo](02_Formateo/)
Aprende todas las formas de formatear e interpolar valores dentro de cadenas de texto.

**Temas clave:**
- f-strings (Python 3.6+): la forma moderna y recomendada
- `str.format()`: forma clásica con `{}`
- `%`-formatting: estilo antiguo (aún válido)
- Especificadores de formato: ancho, precisión, alineación
- Expresiones dentro de f-strings
- Formato de números, fechas y valores especiales

---

### 📁 [03_Regex](03_Regex/)
Domina las expresiones regulares para buscar, validar y transformar texto complejo.

**Temas clave:**
- Módulo `re` de Python
- Patrones básicos: `.`, `*`, `+`, `?`, `^`, `$`
- Clases de caracteres: `\d`, `\w`, `\s`, `[abc]`, `[^abc]`
- Grupos y capturas: `()`, `(?:...)`, `(?P<name>...)`
- Funciones principales: `re.match()`, `re.search()`, `re.findall()`, `re.sub()`, `re.split()`
- Flags: `re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`
- Lookahead y lookbehind

---

### 📁 [04_Manipulacion_Avanzada](04_Manipulacion_Avanzada/)
Técnicas avanzadas para procesar y transformar texto en aplicaciones reales.

**Temas clave:**
- Slicing de strings: `s[inicio:fin:paso]`
- Strings multilínea y raw strings (`r"..."`)
- Codificación y decodificación: `encode()`, `decode()`, UTF-8
- `textwrap`: formateo de párrafos
- `string` module: constantes y utilitarios
- Palindromos, anagramas y algoritmos sobre strings
- Procesamiento de texto estructurado (CSV manual, parsing básico)

---

## Resumen de Contenidos

| Sección | Dificultad | Archivos |
|---|---|---|
| 01_Metodos_de_String | ⭐ Básico | README, ejemplo.py, ejercicios.py |
| 02_Formateo | ⭐⭐ Intermedio | README, ejemplo.py, ejercicios.py |
| 03_Regex | ⭐⭐⭐ Avanzado | README, ejemplo.py, ejercicios.py |
| 04_Manipulacion_Avanzada | ⭐⭐⭐ Avanzado | README, ejemplo.py, ejercicios.py |

## Conceptos Previos Necesarios
- Variables y tipos de datos (01_Introduccion)
- Estructuras condicionales (02_Estructuras_Condicionales)
- Bucles (03_Estructuras_Repetitivas)
- Funciones (05_Funciones)

## Recursos Adicionales
- [Documentación oficial - str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Documentación oficial - re](https://docs.python.org/3/library/re.html)
- [Documentación oficial - string](https://docs.python.org/3/library/string.html)
- [regex101.com](https://regex101.com/) — herramienta interactiva para regex
