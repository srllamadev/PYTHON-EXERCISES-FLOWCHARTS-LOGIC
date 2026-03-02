# Parámetros y Argumentos

## Objetivos de Aprendizaje
- Diferenciar entre parámetros y argumentos
- Usar parámetros posicionales y por nombre
- Definir valores por defecto para parámetros
- Combinar distintos tipos de argumentos

## Conceptos Teóricos

### Parámetros vs Argumentos

| Término | Definición | Ejemplo |
|---|---|---|
| **Parámetro** | Variable en la definición de la función | `def saludar(nombre):` |
| **Argumento** | Valor que pasamos al llamar la función | `saludar("Ana")` |

### Parámetros Posicionales

Se asignan según el orden en que se pasan:

```python
def presentar(nombre, edad):
    print(f"Soy {nombre} y tengo {edad} años.")

presentar("Carlos", 25)   # nombre="Carlos", edad=25
presentar("Ana", 30)      # nombre="Ana",    edad=30
```

### Argumentos por Nombre (Keyword Arguments)

Se especifica el nombre del parámetro al llamar:

```python
presentar(edad=25, nombre="Carlos")  # El orden no importa
presentar(nombre="Ana", edad=30)
```

### Valores por Defecto

Se asignan en la definición. Se usan si no se pasa el argumento:

```python
def saludar(nombre, mensaje="¡Hola"):
    print(f"{mensaje}, {nombre}!")

saludar("Luis")              # ¡Hola, Luis!
saludar("Luis", "Buenos días")  # Buenos días, Luis!
```

> ⚠️ Los parámetros con valor por defecto deben ir **al final**

### Reglas de Combinación

```python
def funcion(obligatorio, opcional="default"):
    pass

# Válido:
funcion("valor")
funcion("valor", "otro")
funcion("valor", opcional="otro")

# Inválido:
# funcion()  -> Error: falta argumento obligatorio
```

## Recursos Adicionales
- [Python Docs - More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
