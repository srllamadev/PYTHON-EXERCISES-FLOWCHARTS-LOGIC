# Scope (Alcance de Variables)

## Objetivos de Aprendizaje
- Comprender qué es el scope o alcance de una variable
- Diferenciar variables locales de globales
- Usar `global` y `nonlocal` cuando sea necesario
- Aplicar la regla LEGB

## Conceptos Teóricos

### ¿Qué es el Scope?
El scope determina **desde dónde es accesible** una variable.

### Variables Locales

Definidas dentro de una función. Solo existen mientras la función ejecuta:

```python
def mi_funcion():
    x = 10   # variable local
    print(x)

mi_funcion()   # 10
# print(x)    # NameError: x no existe aquí
```

### Variables Globales

Definidas fuera de todas las funciones. Accesibles en todo el archivo:

```python
nombre = "Python"   # variable global

def mostrar():
    print(nombre)   # puede LEER la variable global

mostrar()   # Python
```

### Modificar una Variable Global: `global`

Para **modificar** una global dentro de una función:

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)   # 2
```

> ⚠️ El uso excesivo de `global` es una mala práctica. Prefiere `return`.

### La Regla LEGB

Python busca nombres en este orden:

| Letra | Nombre | Descripción |
|---|---|---|
| **L** | Local | Dentro de la función actual |
| **E** | Enclosing | Función exterior (closures) |
| **G** | Global | Nivel del módulo |
| **B** | Built-in | Funciones propias de Python (`len`, `print`...) |

### `nonlocal`

Para modificar una variable de la función **exterior** desde una función **interior**:

```python
def exterior():
    x = 10
    def interior():
        nonlocal x
        x += 5
    interior()
    print(x)   # 15

exterior()
```

## Recursos Adicionales
- [Python Docs - Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
