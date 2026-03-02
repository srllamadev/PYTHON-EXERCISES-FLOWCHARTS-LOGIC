# Conjuntos (set)

## ¿Qué son los Conjuntos?

Los conjuntos son estructuras de datos **mutables** y **no ordenadas** que almacenan elementos **únicos**. Están basados en la teoría matemática de conjuntos y son ideales para eliminar duplicados y realizar operaciones matemáticas.

## Características Principales

- ✅ **Elementos únicos**: No permite duplicados
- ✅ **No ordenados**: No mantienen orden de inserción
- ✅ **Mutables**: Se pueden agregar/eliminar elementos
- ✅ **No indexados**: No se puede acceder por índice
- ✅ **Búsqueda rápida**: O(1) para verificar pertenencia
- ✅ **Elementos hashables**: Solo puede contener elementos inmutables
- ✅ **Operaciones matemáticas**: Unión, intersección, diferencia, etc.

## Sintaxis Básica

```python
# Creación de conjuntos
conjunto_vacio = set()  # ⚠️ {} crea un dict vacío, no un set
numeros = {1, 2, 3, 4, 5}
letras = {'a', 'b', 'c'}
mixto = {1, "dos", 3.0, True, (1, 2)}  # Tipos mixtos OK

# Constructor set()
desde_lista = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4} - elimina duplicados
desde_string = set("Python")  # {'P', 'y', 't', 'h', 'o', 'n'}
desde_rango = set(range(5))  # {0, 1, 2, 3, 4}

# Set comprehension
cuadrados = {x**2 for x in range(6)}  # {0, 1, 4, 9, 16, 25}
```

## Operaciones Comunes

### Agregar y Eliminar Elementos

```python
frutas = {"manzana", "banana"}

# Agregar un elemento
frutas.add("cereza")

# Agregar múltiples elementos
frutas.update(["durazno", "kiwi"])
frutas.update({"uva", "pera"})

# Eliminar elementos
frutas.remove("banana")      # Error si no existe
frutas.discard("banana")     # No error si no existe
elemento = frutas.pop()      # Elimina y retorna elemento aleatorio
frutas.clear()               # Elimina todos
```

### Métodos Principales

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `add(elem)` | Agrega un elemento | `set.add(5)` |
| `update(iterable)` | Agrega múltiples elementos | `set.update([1, 2, 3])`  |
| `remove(elem)` | Elimina elemento (error si no existe) | `set.remove(5)` |
| `discard(elem)` | Elimina elemento (sin error) | `set.discard(5)` |
| `pop()` | Elimina y retorna elemento aleatorio | `set.pop()` |
| `clear()` | Elimina todos los elementos | `set.clear()` |
| `copy()` | Retorna copia superficial | `nuevo = set.copy()` |

## Operaciones Matemáticas

### Unión (|)
```python
A = {1, 2, 3}
B = {3, 4, 5}
union = A | B              # {1, 2, 3, 4, 5}
union = A.union(B)         # Alternativa
```

### Intersección (&)
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
interseccion = A & B       # {3, 4}
interseccion = A.intersection(B)  # Alternativa
```

### Diferencia (-)
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
diferencia = A - B         # {1, 2} - elementos en A pero no en B
diferencia = A.difference(B)  # Alternativa
```

### Diferencia Simétrica (^)
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
dif_simetrica = A ^ B      # {1, 2, 5, 6} - elementos en A o B, pero no en ambos
dif_simetrica = A.symmetric_difference(B)  # Alternativa
```

### Subconjunto y Superconjunto
```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))       # True - A es subconjunto de B
print(B.issuperset(A))     # True - B es superconjunto de A
print(A.isdisjoint(B))     # False - tienen elementos en común
```

## Operaciones con Asignación

| Operación | Descripción | Ejemplo |
|-----------|-------------|---------|
| `\|=` | Unión con asignación | `A \|= B` |
| `&=` | Intersección con asignación | `A &= B` |
| `-=` | Diferencia con asignación | `A -= B` |
| `^=` | Diferencia simétrica con asignación | `A ^= B` |

```python
A = {1, 2, 3}
B = {3, 4, 5}

A |= B  # A ahora es {1, 2, 3, 4, 5}
```

## frozenset (Conjunto Inmutable)

```python
# Conjunto inmutable
fs = frozenset([1, 2, 3, 4])

# No se puede modificar
# fs.add(5)  # Error

# Puede ser clave de diccionario
diccionario = {
    frozenset([1, 2]): "valor1",
    frozenset([3, 4]): "valor2"
}

# Útil como elemento de otro set
conjunto_de_conjuntos = {
    frozenset([1, 2]),
    frozenset([3, 4])
}
```

## Iteración

```python
numeros = {1, 2, 3, 4, 5}

# Básica (orden no garantizado)
for num in numeros:
    print(num)

# Ordenada
for num in sorted(numeros):
    print(num)

# Con enumerate
for i, num in enumerate(sorted(numeros)):
    print(f"{i}: {num}")
```

## Comprensión de Conjuntos

```python
# Básica
cuadrados = {x**2 for x in range(6)}
# {0, 1, 4, 9, 16, 25}

# Con condicional
pares = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}

# De string
vocales = {c for c in "hola mundo" if c in "aeiou"}
# {'a', 'o', 'u'}
```

## Casos de Uso Comunes

- 🔍 Eliminar duplicados de una lista
- 🧮 Operaciones matemáticas de conjuntos
- ✅ Verificar pertenencia rápidamente
- 🎯 Encontrar elementos únicos
- 🔄 Comparar colecciones (intersección, diferencia)
- 📊 Análisis de datos (elementos comunes/diferentes)
- 🏷️ Tags o etiquetas únicas

## Complejidad Temporal

| Operación | Complejidad |
|-----------|-------------|
| Add | O(1) |
| Remove | O(1) |
| Search (in) | O(1) |
| Union | O(len(s1) + len(s2)) |
| Intersection | O(min(len(s1), len(s2))) |
| Difference | O(len(s1)) |

## Restricciones de Elementos

### ✅ Elementos Válidos (Hashables)
```python
set_valido = {1, 2, "tres", 4.5, True, None, (1, 2)}
```

### ❌ Elementos Inválidos (No Hashables)
```python
# Esto NO funciona
# set_invalido = {
#     [1, 2],      # Error: lista
#     {1: 2},      # Error: diccionario
#     {1, 2}       # Error: conjunto
# }
```

## Comparación: set vs list vs dict

| Característica | set | list | dict |
|----------------|-----|------|------|
| Ordenado | No | Sí | Sí (3.7+) |
| Indexado | No | Sí | Por clave |
| Duplicados | No | Sí | No (claves) |
| Mutable | Sí | Sí | Sí |
| Búsqueda | O(1) | O(n) | O(1) |
| Uso principal | Únicos | Secuencias | Mapeos |

## Eliminar Duplicados de Lista

```python
# Problema común: eliminar duplicados
numeros_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]

# Solución 1: Convertir a set
unicos = list(set(numeros_con_duplicados))
# [1, 2, 3, 4, 5] - orden no garantizado

# Solución 2: Mantener orden
def eliminar_duplicados_ordenado(lista):
    visto = set()
    resultado = []
    for item in lista:
        if item not in visto:
            visto.add(item)
            resultado.append(item)
    return resultado

unicos_ordenado = eliminar_duplicados_ordenado(numeros_con_duplicados)
# [1, 2, 3, 4, 5] - orden preservado
```

## Buenas Prácticas

✅ Usar para eliminar duplicados rápidamente  
✅ Preferir para verificación de pertenencia frecuente  
✅ Usar operaciones matemáticas cuando sean aplicables  
✅ Usar `frozenset` para sets inmutables o claves de dict  
✅ Convertir a list y ordenar si necesitas orden específico  

❌ No usar si necesitas orden específico  
❌ No usar si necesitas acceso por índice  
❌ Evitar para elementos mutables (no son hashables)  
❌ No asumir orden en la iteración  

## Trucos y Patrones

### Encontrar elementos comunes
```python
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comunes = list(set(lista1) & set(lista2))  # [4, 5]
```

### Encontrar elementos únicos
```python
todos = lista1 + lista2
solo_en_uno = list(set(lista1) ^ set(lista2))  # [1, 2, 3, 6, 7, 8]
```

### Verificar si todos son únicos
```python
def todos_unicos(lista):
    return len(lista) == len(set(lista))

print(todos_unicos([1, 2, 3]))      # True
print(todos_unicos([1, 2, 2, 3]))   # False
```
