# Operadores Básicos

## Objetivos de Aprendizaje
- Conocer los diferentes tipos de operadores en Python
- Aprender a usar operadores aritméticos, de comparación y lógicos
- Comprender la precedencia de operadores
- Aplicar operadores en expresiones complejas

## Conceptos Teóricos

### 1. Operadores Aritméticos

| Operador | Descripción | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `+` | Suma | `5 + 3` | `8` |
| `-` | Resta | `5 - 3` | `2` |
| `*` | Multiplicación | `5 * 3` | `15` |
| `/` | División | `5 / 2` | `2.5` |
| `//` | División entera | `5 // 2` | `2` |
| `%` | Módulo (resto) | `5 % 2` | `1` |
| `**` | Potencia | `5 ** 2` | `25` |

### 2. Operadores de Comparación

| Operador | Descripción | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `5 <= 3` | `False` |

### 3. Operadores Lógicos

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `and` | Y lógico | `True and False` → `False` |
| `or` | O lógico | `True or False` → `True` |
| `not` | Negación | `not True` → `False` |

### 4. Operadores de Asignación

| Operador | Equivalente | Ejemplo |
|----------|-------------|---------|
| `=` | Asignación | `x = 5` |
| `+=` | `x = x + 3` | `x += 3` |
| `-=` | `x = x - 3` | `x -= 3` |
| `*=` | `x = x * 3` | `x *= 3` |
| `/=` | `x = x / 3` | `x /= 3` |
| `//=` | `x = x // 3` | `x //= 3` |
| `%=` | `x = x % 3` | `x %= 3` |
| `**=` | `x = x ** 3` | `x **= 3` |

### 5. Operadores de Identidad

| Operador | Descripción | Uso |
|----------|-------------|-----|
| `is` | Compara identidad de objetos | `x is y` |
| `is not` | Compara si no son el mismo objeto | `x is not y` |

### 6. Operadores de Pertenencia

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `in` | Elemento está en secuencia | `'a' in 'casa'` → `True` |
| `not in` | Elemento no está en secuencia | `'x' not in 'casa'` → `True` |

### Precedencia de Operadores (de mayor a menor)

1. `**` (potencia)
2. `+x`, `-x`, `~x` (unarios)
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. `==`, `!=`, `>`, `<`, `>=`, `<=`
6. `not`
7. `and`
8. `or`

**Consejo:** Usa paréntesis `()` para claridad y control.

## Ejemplos Prácticos

### Ejemplo 1: Operadores Aritméticos
```python
# Operaciones básicas
a = 10
b = 3

suma = a + b          # 13
resta = a - b         # 7
multiplicacion = a * b  # 30
division = a / b      # 3.333...
division_entera = a // b  # 3
modulo = a % b        # 1
potencia = a ** b     # 1000

print(f"{a} + {b} = {suma}")
print(f"{a} // {b} = {division_entera} (resto: {modulo})")
print(f"{a} ** {b} = {potencia}")
```

### Ejemplo 2: Operadores de Comparación
```python
edad = 18
edad_minima = 18

# Comparaciones
es_mayor_edad = edad >= edad_minima  # True
es_menor = edad < edad_minima        # False
es_exacto = edad == edad_minima      # True

print(f"¿Es mayor de edad? {es_mayor_edad}")
print(f"¿Es menor? {es_menor}")
print(f"¿Tiene exactamente {edad_minima} años? {es_exacto}")
```

### Ejemplo 3: Operadores Lógicos
```python
edad = 20
tiene_licencia = True
tiene_auto = False

# AND - Todas las condiciones deben ser True
puede_conducir = edad >= 18 and tiene_licencia
print(f"¿Puede conducir? {puede_conducir}")  # True

# OR - Al menos una condición debe ser True
tiene_transporte = tiene_auto or tiene_licencia
print(f"¿Tiene transporte? {tiene_transporte}")  # True

# NOT - Invierte el valor booleano
no_tiene_auto = not tiene_auto
print(f"¿No tiene auto? {no_tiene_auto}")  # True
```

### Ejemplo 4: Operadores de Asignación Compuestos
```python
puntos = 100

# Incrementar puntos
puntos += 50    # puntos = puntos + 50 → 150
print(f"Puntos: {puntos}")

# Duplicar puntos
puntos *= 2     # puntos = puntos * 2 → 300
print(f"Puntos duplicados: {puntos}")

# Reducir a la mitad
puntos //= 2    # puntos = puntos // 2 → 150
print(f"Puntos reducidos: {puntos}")
```

### Ejemplo 5: Precedencia de Operadores
```python
# Sin paréntesis
resultado1 = 2 + 3 * 4      # 14 (multiplicación primero)

# Con paréntesis
resultado2 = (2 + 3) * 4    # 20 (suma primero)

# Expresión compleja
resultado3 = 2 ** 3 + 4 * 5 - 6 / 2  # 8 + 20 - 3 = 25

print(f"2 + 3 * 4 = {resultado1}")
print(f"(2 + 3) * 4 = {resultado2}")
print(f"2**3 + 4*5 - 6/2 = {resultado3}")
```

### Ejemplo 6: Operadores de Pertenencia
```python
frase = "Python es genial"
vocales = "aeiou"

# Verificar si está en la cadena
tiene_python = "Python" in frase     # True
tiene_java = "Java" in frase         # False

# Verificar vocales
letra = "a"
es_vocal = letra in vocales          # True

print(f"'Python' está en la frase: {tiene_python}")
print(f"'{letra}' es vocal: {es_vocal}")
```

## Ejercicios Propuestos

### Ejercicio 1: Calculadora Básica
Crea un programa que:
- Pida dos números al usuario
- Realice todas las operaciones aritméticas
- Muestre los resultados formateados

### Ejercicio 2: Verificador de Edad
Crea un programa que:
- Pida el año de nacimiento
- Calcule la edad actual
- Verifique si es mayor de edad (≥18)
- Muestre un mensaje apropiado

### Ejercicio 3: Calculadora de Descuento
Crea un programa que:
- Pida el precio original
- Pida el porcentaje de descuento
- Calcule el precio final
- Muestre el ahorro

```python
# Fórmula: precio_final = precio - (precio * descuento / 100)
```

### Ejercicio 4: Número Par o Impar
Usa el operador módulo `%` para determinar si un número es par o impar.
```python
# Pista: si numero % 2 == 0, es par
```

### Ejercicio 5: Comparador Triple
Pide tres números y determina:
- ¿Son todos iguales?
- ¿Están todos en orden ascendente?
- ¿Al menos uno es mayor a 100?

### Ejercicio 6: Área y Perímetro
Calcula el área y perímetro de un rectángulo:
```python
# Área = base * altura
# Perímetro = 2 * (base + altura)
```

## Casos Especiales y Trucos

### División por Cero
```python
# Esto genera un error
# resultado = 10 / 0  # ZeroDivisionError

# Mejor práctica: verificar antes
divisor = 0
if divisor != 0:
    resultado = 10 / divisor
else:
    print("Error: No se puede dividir por cero")
```

### Comparación en Cadena
```python
edad = 25
# Python permite comparaciones encadenadas
if 18 <= edad < 65:
    print("Adulto en edad laboral")
```

### Swap de Variables
```python
a = 5
b = 10
# Intercambio pythónico (sin variable temporal)
a, b = b, a
print(f"a={a}, b={b}")  # a=10, b=5
```

## Recursos Adicionales
- [Documentación oficial - Operadores](https://docs.python.org/3/library/operator.html)
- [Real Python - Operators](https://realpython.com/python-operators-expressions/)
- [W3Schools - Python Operators](https://www.w3schools.com/python/python_operators.asp)

## Notas Importantes
- La división `/` siempre retorna float, incluso con números enteros
- Usa `//` para división entera (sin decimales)
- El operador `%` es útil para verificar divisibilidad
- Los operadores lógicos evalúan de izquierda a derecha (cortocircuito)
- Usa paréntesis para mayor claridad en expresiones complejas
