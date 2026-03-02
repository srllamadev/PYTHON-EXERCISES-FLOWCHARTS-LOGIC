# Return Values (Valores de Retorno)

## Objetivos de Aprendizaje
- Usar `return` para devolver valores desde una función
- Retornar múltiples valores usando tuplas
- Entender qué ocurre si una función no tiene `return`
- Usar el valor retornado en otras expresiones

## Conceptos Teóricos

### La Sentencia `return`

```python
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(3, 5)   # total = 8
print(total)           # 8
```

`return` hace dos cosas:
1. **Sale** de la función inmediatamente
2. **Devuelve** un valor al lugar donde fue llamada

### Funciones sin `return`

Si no hay `return`, la función retorna `None`:

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

resultado = saludar("Ana")
print(resultado)   # None
```

### Retornar Múltiples Valores

Python permite retornar varios valores como una tupla:

```python
def dividir(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo   # retorna una tupla

q, r = dividir(17, 5)
print(q, r)   # 3 2
```

### `return` Temprano (Early Return)

Puedes usar `return` sin valor para salir antes de tiempo:

```python
def dividir_seguro(a, b):
    if b == 0:
        print("Error: división entre cero")
        return   # Sale aquí, retorna None
    return a / b
```

### Usar el Valor Retornado

```python
def al_cuadrado(n):
    return n ** 2

# En una expresión
print(al_cuadrado(4) + al_cuadrado(3))   # 16 + 9 = 25

# Como argumento de otra función
print(max(al_cuadrado(3), al_cuadrado(5)))   # 25
```

## Recursos Adicionales
- [Python Docs - return statement](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement)
