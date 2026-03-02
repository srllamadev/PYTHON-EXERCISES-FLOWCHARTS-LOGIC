# For Loops

## Concepto
El bucle `for` itera sobre una secuencia (lista, tupla, string, etc.) ejecutando un bloque de código para cada elemento.

## Sintaxis Básica
```python
for elemento in secuencia:
    # código a ejecutar por cada elemento
```

## Características
- Ideal cuando conoces la cantidad de iteraciones o tienes una secuencia definida
- Más Pythónico y legible que while para iterar sobre colecciones
- Automáticamente maneja el índice y la condición de parada

## Estructuras de Datos compatibles
- Listas: `[1, 2, 3]`
- Tuplas: `(1, 2, 3)`
- Strings: `"Python"`
- Diccionarios: `{'a': 1, 'b': 2}`
- Conjuntos: `{1, 2, 3}`
- Rangos: `range(10)`

## Funciones Útiles
- `enumerate()`: obtener índice y valor
- `zip()`: iterar sobre múltiples secuencias
- `reversed()`: iterar en orden inverso
- `sorted()`: iterar en orden ordenado

## Cuándo usar For vs While
**For**: Cuando sabes cuántas veces iterar o tienes una colección
**While**: Cuando la condición de parada es dinámica o desconocida
