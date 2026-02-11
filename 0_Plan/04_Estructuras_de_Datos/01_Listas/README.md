# Listas (list)

## ¿Qué son las Listas?

Las listas son estructuras de datos **mutables** y **ordenadas** que pueden contener elementos de cualquier tipo. Son la estructura más versátil en Python.

## Características Principales

- ✅ **Mutables**: Se pueden modificar después de su creación
- ✅ **Ordenadas**: Mantienen el orden de los elementos
- ✅ **Indexadas**: Acceso mediante índices (0, 1, 2, ...)
- ✅ **Permiten duplicados**: Pueden tener elementos repetidos
- ✅ **Heterogéneas**: Pueden contener diferentes tipos de datos

## Sintaxis Básica

```python
# Creación de listas
lista_vacia = []
numeros = [1, 2, 3, 4, 5]
mixta = [1, "dos", 3.0, True, [5, 6]]

# Constructor list()
lista_desde_string = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
lista_desde_rango = list(range(5))   # [0, 1, 2, 3, 4]
```

## Operaciones Comunes

### Acceso a Elementos
```python
frutas = ["manzana", "banana", "cereza"]
primera = frutas[0]      # "manzana"
ultima = frutas[-1]      # "cereza"
```

### Slicing (Rebanado)
```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeros_tres = numeros[:3]        # [0, 1, 2]
ultimos_tres = numeros[-3:]        # [7, 8, 9]
del_2_al_5 = numeros[2:6]         # [2, 3, 4, 5]
pares = numeros[::2]               # [0, 2, 4, 6, 8]
invertida = numeros[::-1]          # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### Métodos Principales

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `append(x)` | Agrega un elemento al final | `lista.append(10)` |
| `extend(iterable)` | Extiende la lista con elementos de otro iterable | `lista.extend([1, 2, 3])` |
| `insert(i, x)` | Inserta elemento en posición i | `lista.insert(0, "primero")` |
| `remove(x)` | Elimina la primera ocurrencia de x | `lista.remove("elemento")` |
| `pop([i])` | Elimina y retorna elemento en posición i | `lista.pop()` |
| `clear()` | Elimina todos los elementos | `lista.clear()` |
| `index(x)` | Retorna índice de la primera ocurrencia | `lista.index("buscar")` |
| `count(x)` | Cuenta ocurrencias de x | `lista.count(5)` |
| `sort()` | Ordena la lista in-place | `lista.sort()` |
| `reverse()` | Invierte la lista in-place | `lista.reverse()` |
| `copy()` | Retorna una copia superficial | `nueva = lista.copy()` |

## Listas Anidadas

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento = matriz[1][2]  # 6
```

## Iteración

```python
frutas = ["manzana", "banana", "cereza"]

# Básica
for fruta in frutas:
    print(fruta)

# Con índice
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# While
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1
```

## Casos de Uso Comunes

- 📊 Almacenar secuencias de datos
- 🔄 Pilas (stacks) y colas (queues)
- 📝 Listas de tareas o elementos
- 🎲 Colecciones ordenadas que requieren modificación
- 📈 Datos tabulares simples

## Complejidad Temporal

| Operación | Complejidad |
|-----------|-------------|
| Acceso por índice | O(1) |
| Append | O(1) |
| Insert | O(n) |
| Delete | O(n) |
| Search | O(n) |
| Sort | O(n log n) |

## Buenas Prácticas

✅ Usar nombres descriptivos en plural  
✅ Mantener tipos consistentes cuando sea posible  
✅ Usar list comprehensions para transformaciones simples  
✅ Evitar modificar listas mientras se iteran  
✅ Usar `copy()` para duplicar listas  

❌ No usar listas para búsquedas frecuentes (usa dict o set)  
❌ Evitar listas muy anidadas (dificultan lectura)  
❌ No usar índices mágicos sin documentar  
