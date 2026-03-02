# Lambda Functions (Funciones Anónimas)

## Objetivos de Aprendizaje
- Entender qué es una función lambda
- Escribir funciones lambda simples
- Usar lambdas con `map()`, `filter()` y `sorted()`
- Reconocer cuándo es apropiado usar lambdas

## Conceptos Teóricos

### ¿Qué es una Lambda?

Una **lambda** es una función anónima (sin nombre) de una sola expresión:

```python
# Función normal
def cuadrado(x):
    return x ** 2

# Equivalente lambda
cuadrado = lambda x: x ** 2

print(cuadrado(5))   # 25
```

### Sintaxis

```
lambda parámetros : expresión
```

- Puede tener **cero o más** parámetros
- Solo puede contener **una expresión**
- **Retorna** automáticamente el resultado de la expresión

### Lambdas con Cero, Uno o Varios Parámetros

```python
sin_params   = lambda: "Hola!"
un_param     = lambda x: x * 2
dos_params   = lambda x, y: x + y
tres_params  = lambda x, y, z: x + y + z
```

### Uso con `sorted()`

El caso más común de las lambdas es como función de ordenamiento:

```python
personas = [("Ana", 30), ("Luis", 20), ("María", 25)]
ordenado = sorted(personas, key=lambda p: p[1])
# [("Luis", 20), ("María", 25), ("Ana", 30)]
```

### Uso con `map()` y `filter()`

```python
# map: aplica la función a cada elemento
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
# [1, 4, 9, 16, 25]

# filter: conserva elementos que cumplan la condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4]
```

### ¿Cuándo Usar Lambda?

| ✅ Úsala cuando... | ❌ No la uses cuando... |
|---|---|
| La función es muy simple | Necesitas docstring |
| Se usa una sola vez | La lógica es compleja |
| Como argumento de otra función | Necesitas múltiples líneas |

## Recursos Adicionales
- [Python Docs - Lambda Expressions](https://docs.python.org/3/reference/expressions.html#lambda)
