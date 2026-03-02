# 01 - Métodos de String

## Objetivos de Aprendizaje
- Conocer y usar los métodos integrados de las cadenas de texto en Python
- Entender cuándo aplicar cada método
- Combinar métodos para resolver problemas reales

## Conceptos Teóricos

### Los Strings son Inmutables

En Python, los strings **no se modifican en su lugar**. Cada método devuelve un **nuevo string**:

```python
texto = "hola"
resultado = texto.upper()
print(texto)     # "hola"   <- no cambia
print(resultado) # "HOLA"   <- nuevo string
```

---

## Métodos por Categoría

### 🔠 Transformación de Caso

| Método | Descripción | Ejemplo |
|---|---|---|
| `upper()` | Todo a mayúsculas | `"hola".upper()` → `"HOLA"` |
| `lower()` | Todo a minúsculas | `"HOLA".lower()` → `"hola"` |
| `title()` | Primera letra de cada palabra en mayúscula | `"hola mundo".title()` → `"Hola Mundo"` |
| `capitalize()` | Primera letra en mayúscula | `"hola mundo".capitalize()` → `"Hola mundo"` |
| `swapcase()` | Invierte mayúsculas/minúsculas | `"Hola".swapcase()` → `"hOLA"` |

---

### 🔍 Búsqueda y Verificación

| Método | Descripción | Ejemplo |
|---|---|---|
| `find(sub)` | Retorna el índice de la primera aparición (-1 si no existe) | `"hola".find("o")` → `1` |
| `index(sub)` | Como `find()` pero lanza error si no encuentra | `"hola".index("o")` → `1` |
| `count(sub)` | Cuenta las apariciones de una subcadena | `"banana".count("a")` → `3` |
| `startswith(prefix)` | ¿Empieza con...? | `"Python".startswith("Py")` → `True` |
| `endswith(suffix)` | ¿Termina con...? | `"archivo.py".endswith(".py")` → `True` |
| `in` (operador) | ¿Contiene la subcadena? | `"hola" in "hola mundo"` → `True` |

---

### ✂️ División y Unión

| Método | Descripción | Ejemplo |
|---|---|---|
| `split(sep)` | Divide en lista por separador | `"a,b,c".split(",")` → `["a","b","c"]` |
| `rsplit(sep)` | Divide desde la derecha | `"a.b.c".rsplit(".", 1)` → `["a.b","c"]` |
| `join(iterable)` | Une una lista con el string como separador | `" ".join(["Hola","Mundo"])` → `"Hola Mundo"` |
| `partition(sep)` | Divide en 3 partes: antes, sep, después | `"a:b".partition(":")` → `("a",":",  "b")` |
| `splitlines()` | Divide por saltos de línea | `"a\nb".splitlines()` → `["a","b"]` |

---

### 🧹 Limpieza

| Método | Descripción | Ejemplo |
|---|---|---|
| `strip()` | Elimina espacios (o chars) de ambos lados | `"  hola  ".strip()` → `"hola"` |
| `lstrip()` | Elimina del lado izquierdo | `"  hola  ".lstrip()` → `"hola  "` |
| `rstrip()` | Elimina del lado derecho | `"  hola  ".rstrip()` → `"  hola"` |
| `replace(old, new)` | Reemplaza todas las apariciones | `"aabbcc".replace("b","X")` → `"aaXXcc"` |
| `removeprefix(p)` | Elimina prefijo (Python 3.9+) | `"Mr. Smith".removeprefix("Mr. ")` → `"Smith"` |
| `removesuffix(s)` | Elimina sufijo (Python 3.9+) | `"archivo.py".removesuffix(".py")` → `"archivo"` |

---

### 🔢 Verificación de Contenido

| Método | Retorna `True` si... |
|---|---|
| `isalpha()` | Solo letras |
| `isdigit()` | Solo dígitos |
| `isalnum()` | Solo letras y dígitos |
| `isspace()` | Solo espacios en blanco |
| `isupper()` | Todas las letras son mayúsculas |
| `islower()` | Todas las letras son minúsculas |
| `istitle()` | Formato Title Case |

---

### 📐 Alineación y Relleno

| Método | Descripción | Ejemplo |
|---|---|---|
| `center(width, char)` | Centra en un ancho dato | `"hi".center(10, "-")` → `"----hi----"` |
| `ljust(width, char)` | Alinea a la izquierda | `"hi".ljust(10, ".")` → `"hi........"` |
| `rjust(width, char)` | Alinea a la derecha | `"hi".rjust(10, ".")` → `"........hi"` |
| `zfill(width)` | Rellena con ceros a la izquierda | `"42".zfill(6)` → `"000042"` |

---

## Buenas Prácticas

✅ Encadena métodos cuando tiene sentido: `texto.strip().lower()`  
✅ Usa `in` para comprobar contenido antes de `find()`  
✅ Prefiere `split()` + `join()` para transformar separadores  
❌ No uses `index()` sin manejar `ValueError`

## Archivos del Módulo

- [`ejemplo.py`](ejemplo.py) — Demostraciones ejecutables
- [`ejercicios.py`](ejercicios.py) — Ejercicios para practicar
