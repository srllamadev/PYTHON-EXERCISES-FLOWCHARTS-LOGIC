# Decoradores Básicos

## Objetivos de Aprendizaje
- Entender que las funciones son objetos de primera clase
- Comprender qué es un closure
- Escribir un decorador simple
- Usar la sintaxis `@decorador`
- Usar `functools.wraps` para preservar metadatos

## Conceptos Teóricos

### Funciones como Objetos

En Python, las funciones son objetos. Pueden:
- Asignarse a variables
- Pasarse como argumentos
- Retornarse desde otras funciones

```python
def saludar():
    return "¡Hola!"

mi_funcion = saludar       # sin paréntesis = no la llama
print(mi_funcion())        # ¡Hola!
```

### Funciones Anidadas y Closures

```python
def exterior(nombre):
    def interior():          # función anidada
        return f"Hola, {nombre}!"
    return interior          # retorna la función (no la llama)

fn = exterior("Ana")
print(fn())   # Hola, Ana!
```

`interior` "recuerda" el valor de `nombre`. Eso es un **closure**.

### ¿Qué es un Decorador?

Un decorador es una función que:
1. **Recibe** una función como argumento
2. Define una función **wrapper** que extiende el comportamiento
3. **Retorna** el wrapper

```python
def mi_decorador(funcion):
    def wrapper():
        print("Antes de ejecutar")
        funcion()
        print("Después de ejecutar")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()
# Antes de ejecutar
# ¡Hola!
# Después de ejecutar
```

### `@decorador` es equivalente a:

```python
saludar = mi_decorador(saludar)
```

### Preservar Metadatos con `functools.wraps`

```python
from functools import wraps

def mi_decorador(funcion):
    @wraps(funcion)          # preserva __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return funcion(*args, **kwargs)
    return wrapper
```

### Decoradores con Parámetros

```python
def repetir(n):
    def decorador(funcion):
        @wraps(funcion)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcion(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("¡Hola!")
```

## Recursos Adicionales
- [Python Docs - Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [PEP 318 - Decorators for Functions](https://peps.python.org/pep-0318/)
