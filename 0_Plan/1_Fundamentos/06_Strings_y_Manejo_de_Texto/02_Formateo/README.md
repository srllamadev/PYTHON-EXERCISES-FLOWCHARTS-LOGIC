# 02 - Formateo de Strings

## Objetivos de Aprendizaje
- Dominar las tres formas de formatear strings en Python
- Usar f-strings de forma idiomática y eficiente
- Controlar la presentación de números, texto y fechas con especificadores
- Elegir el método adecuado según el contexto

## Conceptos Teóricos

Python ofrece tres formas principales de formatear strings:

---

## 1. f-strings (Python 3.6+) — Recomendado ✅

La forma más moderna, legible y eficiente.

```python
nombre = "Ana"
edad = 28
print(f"Hola, {nombre}. Tienes {edad} años.")
# → "Hola, Ana. Tienes 28 años."
```

### Expresiones dentro de f-strings

```python
a, b = 3, 4
print(f"La suma de {a} + {b} = {a + b}")
print(f"Raíz cuadrada de 16: {16 ** 0.5}")
print(f"Nombre en mayúsculas: {'ana'.upper()}")
```

### Especificadores de formato en f-strings

La sintaxis es: `{valor:especificador}`

```python
pi = 3.14159265
print(f"{pi:.2f}")        # 2 decimales → "3.14"
print(f"{pi:10.3f}")      # ancho 10, 3 decimales → "     3.142"
print(f"{1000000:,}")     # separador de miles → "1,000,000"
print(f"{0.85:.1%}")      # porcentaje → "85.0%"

nombre = "Python"
print(f"{nombre:>20}")    # alineado a la derecha
print(f"{nombre:<20}")    # alineado a la izquierda
print(f"{nombre:^20}")    # centrado
print(f"{nombre:*^20}")   # centrado con relleno *
```

### f-strings multilínea

```python
producto = "Laptop"
precio = 999.99
descuento = 0.15

mensaje = (
    f"Producto: {producto}\n"
    f"Precio:   {precio:.2f}€\n"
    f"Descuento:{descuento:.0%}\n"
    f"Final:    {precio * (1 - descuento):.2f}€"
)
print(mensaje)
```

---

## 2. str.format() — Clásico

```python
print("Hola, {}. Tienes {} años.".format("Ana", 28))
print("Hola, {nombre}. Tienes {edad} años.".format(nombre="Ana", edad=28))
print("{0} + {1} = {2}".format(3, 4, 3+4))
```

Admite los mismos especificadores que f-strings:

```python
print("{:.2f}".format(3.14159))        # "3.14"
print("{:>10}".format("texto"))        # "     texto"
print("{:0>6}".format(42))             # "000042"
```

---

## 3. %-formatting — Estilo antiguo (C-like)

```python
nombre = "Ana"
edad = 28
print("Hola, %s. Tienes %d años." % (nombre, edad))
print("Pi es aproximadamente %.2f" % 3.14159)
```

| Especificador | Tipo |
|---|---|
| `%s` | string |
| `%d` | entero |
| `%f` | float |
| `%e` | notación científica |
| `%x` | hexadecimal |

> ⚠️ Este estilo es más difícil de leer. Úsalo solo si mantienes código antiguo.

---

## Tabla de Especificadores de Formato

| Especificador | Descripción | Ejemplo |
|---|---|---|
| `d` | Entero decimal | `f"{42:d}"` → `"42"` |
| `f` | Float | `f"{3.14:.2f}"` → `"3.14"` |
| `e` | Notación científica | `f"{1234:.2e}"` → `"1.23e+03"` |
| `%` | Porcentaje | `f"{0.85:.1%}"` → `"85.0%"` |
| `s` | String | `f"{'hi':>10s}"` → `"        hi"` |
| `b` | Binario | `f"{10:b}"` → `"1010"` |
| `x` | Hexadecimal | `f"{255:x}"` → `"ff"` |
| `o` | Octal | `f"{8:o}"` → `"10"` |
| `,` | Separador de miles | `f"{1000000:,}"` → `"1,000,000"` |

---

## Cuándo Usar Cada Uno

| Situación | Recomendación |
|---|---|
| Código nuevo Python 3.6+ | f-strings ✅ |
| Plantillas reutilizables (no ejecutables) | `str.format()` |
| Mantener código Python 2 / legacy | `%`-formatting |
| Logging con `%` internamente | `%`-formatting (el logger lo evalúa lazy) |

---

## Archivos del Módulo

- [`ejemplo.py`](ejemplo.py) — Demostraciones ejecutables
- [`ejercicios.py`](ejercicios.py) — Ejercicios para practicar
