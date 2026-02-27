# *args y **kwargs

## Objetivos de Aprendizaje
- Crear funciones que acepten un número variable de argumentos con `*args`
- Crear funciones que acepten argumentos de palabra clave variables con `**kwargs`
- Combinar parámetros regulares con `*args` y `**kwargs`
- Desempacar listas y diccionarios con `*` y `**`

## Conceptos Teóricos

### El Problema

¿Cómo creamos una función que acepte cualquier cantidad de argumentos?

```python
# ¿Cómo sumar N números?
sumar(1, 2)
sumar(1, 2, 3)
sumar(1, 2, 3, 4, 5)
```

### `*args` - Argumentos Posicionales Variables

Recoge todos los argumentos posicionales extras en una **tupla**:

```python
def sumar(*args):
    return sum(args)

print(sumar(1, 2))        # 3
print(sumar(1, 2, 3, 4))  # 10
```

> El nombre `args` es convención; técnicamente puede ser cualquier nombre.

### `**kwargs` - Argumentos de Palabra Clave Variables

Recoge todos los keyword arguments extras en un **diccionario**:

```python
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Madrid")
```

### Combinación de Parámetros

El orden **obligatorio** es:

```python
def funcion(posicional, *args, **kwargs):
    pass
```

```python
def funcion(obligatorio, /, normal, *, solo_keyword, **kwargs):
    pass
```

### Desempaquetado con `*` y `**`

```python
def sumar(a, b, c):
    return a + b + c

numeros = [1, 2, 3]
print(sumar(*numeros))    # desempaqueta lista -> sumar(1, 2, 3)

datos = {"a": 1, "b": 2, "c": 3}
print(sumar(**datos))     # desempaqueta dict  -> sumar(a=1, b=2, c=3)
```

## Recursos Adicionales
- [Python Docs - Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
