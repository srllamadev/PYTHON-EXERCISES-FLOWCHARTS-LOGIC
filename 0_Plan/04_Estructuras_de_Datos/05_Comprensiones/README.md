# Comprensiones (Comprehensions)

## ¿Qué son las Comprensiones?

Las comprensiones son una forma **concisa** y **elegante** de crear listas, diccionarios y conjuntos en Python. Permiten generar estructuras de datos en una sola línea, aplicando transformaciones y filtros de manera eficiente.

## Tipos de Comprensiones

- 📋 **List Comprehensions** - Crear listas
- 📚 **Dict Comprehensions** - Crear diccionarios
- 🎯 **Set Comprehensions** - Crear conjuntos
- ⚡ **Generator Expressions** - Crear generadores (lazy evaluation)

## Sintaxis General

```python
# Sintaxis básica
[expresion for item in iterable]

# Con condicional
[expresion for item in iterable if condicion]

# Con if-else
[expresion_si for item in iterable if condicion else expresion_no]

# Anidada
[expresion for item1 in iterable1 for item2 in iterable2]
```

---

## 1. LIST COMPREHENSIONS

### Sintaxis

```python
# Básica
nueva_lista = [expresion for item in iterable]

# Con filtro
nueva_lista = [expresion for item in iterable if condicion]

# Con if-else
nueva_lista = [valor_si if condicion else valor_no for item in iterable]
```

### Ejemplos

```python
# Cuadrados del 0 al 9
cuadrados = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Solo números pares
pares = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Cuadrados de números pares
cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Conversión de temperaturas
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(9/5) * temp + 32 for temp in celsius]
# [32.0, 50.0, 68.0, 86.0, 104.0]

# Con if-else
numeros = [1, 2, 3, 4, 5, 6]
clasificacion = ["par" if x % 2 == 0 else "impar" for x in numeros]
# ["impar", "par", "impar", "par", "impar", "par"]

# Aplanar lista anidada
matriz = [[1, 2], [3, 4], [5, 6]]
aplanada = [num for fila in matriz for num in fila]
# [1, 2, 3, 4, 5, 6]

# Strings
palabras = ["Hola", "Mundo", "Python"]
mayusculas = [palabra.upper() for palabra in palabras]
# ["HOLA", "MUNDO", "PYTHON"]

longitudes = [len(palabra) for palabra in palabras]
# [4, 5, 6]
```

### Equivalente con bucle tradicional

```python
# Con comprehension
cuadrados = [x**2 for x in range(5)]

# Equivalente tradicional
cuadrados = []
for x in range(5):
    cuadrados.append(x**2)
```

---

## 2. DICT COMPREHENSIONS

### Sintaxis

```python
# Básica
nuevo_dict = {clave_expr: valor_expr for item in iterable}

# Con filtro
nuevo_dict = {clave_expr: valor_expr for item in iterable if condicion}
```

### Ejemplos

```python
# Cuadrados como diccionario
cuadrados = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# Filtrar diccionario
precios = {"laptop": 1000, "mouse": 25, "teclado": 75, "monitor": 300}
caros = {k: v for k, v in precios.items() if v > 50}
# {"laptop": 1000, "teclado": 75, "monitor": 300}

# Desde dos listas
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 25, "Madrid"]
persona = {k: v for k, v in zip(claves, valores)}
# {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Transformar valores
productos = {"laptop": 100, "mouse": 25, "teclado": 75}
con_iva = {prod: precio * 1.16 for prod, precio in productos.items()}
# {"laptop": 116.0, "mouse": 29.0, "teclado": 87.0}

# Contar caracteres
texto = "python"
frecuencia = {char: texto.count(char) for char in texto}
# {"p": 1, "y": 1, "t": 1, "h": 1, "o": 1, "n": 1}
```

### Equivalente con bucle tradicional

```python
# Con comprehension
cuadrados = {x: x**2 for x in range(5)}

# Equivalente tradicional
cuadrados = {}
for x in range(5):
    cuadrados[x] = x**2
```

---

## 3. SET COMPREHENSIONS

### Sintaxis

```python
# Básica
nuevo_set = {expresion for item in iterable}

# Con filtro
nuevo_set = {expresion for item in iterable if condicion}
```

### Ejemplos

```python
# Cuadrados únicos
cuadrados = {x**2 for x in range(-5, 6)}
# {0, 1, 4, 9, 16, 25}

# Vocales en texto
texto = "Hola Mundo"
vocales = {c.lower() for c in texto if c.lower() in "aeiou"}
# {"o", "a", "u"}

# Longitudes únicas
palabras = ["hola", "hola", "mundo", "python", "go"]
longitudes = {len(palabra) for palabra in palabras}
# {2, 4, 5, 6}

# Caracteres únicos
texto = "programming"
unicos = {char for char in texto}
# {"p", "r", "o", "g", "a", "m", "i", "n"}
```

---

## 4. GENERATOR EXPRESSIONS

### Sintaxis

```python
# Similar a list comprehension pero con paréntesis
generador = (expresion for item in iterable)
```

### Características

- 🚀 **Lazy evaluation** - No calcula todos los valores inmediatamente
- 💾 **Eficiente en memoria** - No almacena toda la secuencia
- ⚡ **Más rápido** para grandes datasets
- 🔁 **Iterable una sola vez** - Se consume al iterar

### Ejemplos

```python
# Generator expression
cuadrados_gen = (x**2 for x in range(1000000))
# No ocupa mucha memoria, calcula valores bajo demanda

# Usar con sum(), max(), min(), etc.
suma = sum(x**2 for x in range(100))
# 328350

maximo = max(x**2 for x in range(10))
# 81

# Convertir a lista si se necesita
cuadrados = list(x**2 for x in range(10))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Comparación de Rendimiento

```python
import sys

# List comprehension
lista = [x**2 for x in range(1000000)]
print(sys.getsizeof(lista))  # ~8 MB

# Generator expression
generador = (x**2 for x in range(1000000))
print(sys.getsizeof(generador))  # ~128 bytes
```

---

## Comprensiones Anidadas

### Listas Anidadas

```python
# Matriz 3x3
matriz = [[i*3 + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Producto cartesiano
pares = [(x, y) for x in [1, 2, 3] for y in ["a", "b", "c"]]
# [(1, "a"), (1, "b"), (1, "c"), (2, "a"), ...]

# Aplanar matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [num for fila in matriz for num in fila]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Diccionarios Anidados

```python
# Tabla de multiplicar
tabla = {i: {j: i*j for j in range(1, 6)} for i in range(1, 6)}
# {1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 2: {1: 2, 2: 4, ...}, ...}
```

---

## Comparación: Comprehension vs Bucle

| Aspecto | Comprehension | Bucle Tradicional |
|---------|---------------|-------------------|
| Sintaxis | Concisa (1 línea) | Verbosa (3-4 líneas) |
| Legibilidad | Alta para casos simples | Mejor para lógica compleja |
| Rendimiento | Generalmente más rápido | Ligeramente más lento |
| Flexibilidad | Limitada | Total |
| Uso de memoria | Crea estructura completa | Misma |

---

## Cuándo Usar Comprehensions

### ✅ Usar cuando:
- Transformar colecciones simples
- Filtrar elementos con criterio simple
- Crear nuevas estructuras desde iterables
- El código cabe cómodamente en 1-2 líneas
- La lógica es clara y directa

### ❌ NO usar cuando:
- La lógica es compleja (múltiples condiciones)
- Necesitas múltiples operaciones por elemento
- Requieres manejo de errores
- El código se vuelve ilegible
- Necesitas efectos secundarios (print, modificar variables externas)

---

## Ejemplos Prácticos Avanzados

### Filtrado Complejo

```python
# Números pares mayores a 10
numeros = range(30)
resultado = [x for x in numeros if x % 2 == 0 and x > 10]
# [12, 14, 16, 18, 20, 22, 24, 26, 28]
```

### Procesamiento de Strings

```python
# Palabras que empiezan con mayúscula
texto = "Hola mundo Python es Genial"
palabras_caps = [p for p in texto.split() if p[0].isupper()]
# ["Hola", "Python", "Genial"]
```

### Diccionario de Frecuencias

```python
texto = "hello world"
freq = {char: texto.count(char) for char in set(texto) if char != " "}
# {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
```

### Transposición de Matriz

```python
matriz = [[1, 2, 3], [4, 5, 6]]
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
# [[1, 4], [2, 5], [3, 6]]
```

---

## Buenas Prácticas

✅ Mantener comprensiones simples y legibles  
✅ Usar nombres de variables descriptivos  
✅ Limitar a 1-2 niveles de anidación  
✅ Preferir generator expressions para grandes datasets  
✅ Dividir comprensiones complejas en pasos  
✅ Comentar comprensiones no obvias  

❌ No sacrificar legibilidad por brevedad  
❌ Evitar efectos secundarios  
❌ No anidar más de 2 niveles  
❌ No usar para lógica compleja  
❌ No ignorar el rendimiento en datasets grandes  

---

## Trucos y Patrones

### Filtrar None values
```python
lista = [1, None, 3, None, 5]
sin_none = [x for x in lista if x is not None]
# [1, 3, 5]
```

### Agrupar elementos
```python
numeros = range(10)
grupos = [(x, x+1, x+2) for x in numeros if x % 3 == 0]
# [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
```

### Combinar múltiples listas
```python
nom = ["Ana", "Luis"]
edad = [25, 30]
ciudad = ["Madrid", "Barcelona"]
personas = [{"nombre": n, "edad": e, "ciudad": c} 
            for n, e, c in zip(nom, edad, ciudad)]
```
