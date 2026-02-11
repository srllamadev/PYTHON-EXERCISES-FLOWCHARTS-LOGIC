# Diccionarios (dict)

## ¿Qué son los Diccionarios?

Los diccionarios son estructuras de datos **mutables** y **no ordenadas** (desde Python 3.7+ mantienen orden de inserción) que almacenan pares **clave-valor**. Son ideales para búsquedas rápidas y mapeos.

## Características Principales

- ✅ **Mutables**: Se pueden modificar después de su creación
- ✅ **No indexados**: Acceso mediante claves, no índices numéricos
- ✅ **Claves únicas**: No pueden tener claves duplicadas
- ✅ **Orden de inserción**: Desde Python 3.7+ mantienen el orden
- ✅ **Búsqueda rápida**: O(1) en promedio para acceso
- ✅ **Valores cualquier tipo**: Valores pueden ser de cualquier tipo
- ✅ **Claves hashables**: Las claves deben ser inmutables

## Sintaxis Básica

```python
# Creación de diccionarios
diccionario_vacio = {}
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
numeros = {1: "uno", 2: "dos", 3: "tres"}
mixto = {"texto": "hola", 100: "número", (1, 2): "tupla"}

# Constructor dict()
desde_lista = dict([("a", 1), ("b", 2), ("c", 3)])
con_keywords = dict(nombre="Luis", edad=30, ciudad="Barcelona")
desde_zip = dict(zip(["x", "y", "z"], [1, 2, 3]))

# Comprehension
cuadrados = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Operaciones Comunes

### Acceso a Elementos
```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Acceso directo
nombre = persona["nombre"]  # "Ana"

# Método get() (más seguro)
edad = persona.get("edad")           # 25
pais = persona.get("pais", "España")  # "España" (valor por defecto)

# Modificar valor
persona["edad"] = 26

# Agregar nuevo par
persona["profesion"] = "Ingeniera"

# Eliminar
del persona["ciudad"]
profesion = persona.pop("profesion")  # Elimina y retorna
```

### Métodos Principales

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `get(key, default)` | Obtiene valor o default si no existe | `dict.get("key", 0)` |
| `keys()` | Retorna vista de las claves | `dict.keys()` |
| `values()` | Retorna vista de los valores | `dict.values()` |
| `items()` | Retorna vista de pares (clave, valor) | `dict.items()` |
| `update(dict2)` | Actualiza con pares de otro diccionario | `dict1.update(dict2)` |
| `pop(key)` | Elimina y retorna valor de la clave | `dict.pop("key")` |
| `popitem()` | Elimina y retorna último par insertado | `dict.popitem()` |
| `clear()` | Elimina todos los elementos | `dict.clear()` |
| `setdefault(key, default)` | Obtiene valor o lo crea con default | `dict.setdefault("key", 0)` |
| `copy()` | Retorna copia superficial | `nuevo = dict.copy()` |

## Iteración

```python
estudiante = {"nombre": "Luis", "edad": 20, "carrera": "Ingeniería"}

# Iterar sobre claves
for clave in estudiante:
    print(clave)

for clave in estudiante.keys():
    print(clave)

# Iterar sobre valores
for valor in estudiante.values():
    print(valor)

# Iterar sobre pares clave-valor
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
```

## Diccionarios Anidados

```python
empresa = {
    "nombre": "Tech Corp",
    "fundacion": 2010,
    "empleados": {
        "juan": {"puesto": "CEO", "salario": 100000},
        "ana": {"puesto": "CTO", "salario": 90000},
        "luis": {"puesto": "Developer", "salario": 60000}
    },
    "productos": ["Software A", "Software B"]
}

# Acceso anidado
ceo_salario = empresa["empleados"]["juan"]["salario"]  # 100000
```

## Operaciones Avanzadas

### Fusionar Diccionarios

```python
# Python 3.9+
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
fusionado = dict1 | dict2  # {"a": 1, "b": 2, "c": 3, "d": 4}

# Método update
dict1.update(dict2)

# Desempaquetado
fusionado = {**dict1, **dict2}
```

### setdefault() vs get()

```python
conteo = {}

# Con get()
palabra = "hola"
conteo[palabra] = conteo.get(palabra, 0) + 1

# Con setdefault() (más corto)
conteo.setdefault(palabra, 0)
conteo[palabra] += 1
```

### Diccionario por Defecto (defaultdict)

```python
from collections import defaultdict

# Contador automático
conteo = defaultdict(int)
for palabra in ["a", "b", "a", "c", "b", "a"]:
    conteo[palabra] += 1  # No necesita inicializar

# Lista automática
grupos = defaultdict(list)
grupos["frutas"].append("manzana")  # Crea la lista automáticamente
```

### OrderedDict (dict ordenado)

```python
from collections import OrderedDict

# Antes de Python 3.7 para garantizar orden
ordenado = OrderedDict([("z", 1), ("a", 2), ("m", 3)])

# Mover al final
ordenado.move_to_end("z")  # z ahora está al final

# Mover al inicio
ordenado.move_to_end("a", last=False)
```

## Comprensión de Diccionarios

```python
# Básica
cuadrados = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Con condicional
pares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# Desde dos listas
llaves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 25, "Madrid"]
persona = {k: v for k, v in zip(llaves, valores)}
```

## Casos de Uso Comunes

- 🗂️ Mapeos y asociaciones (clave-valor)
- 📊 Contadores y frecuencias
- 🔍 Búsqueda rápida de datos
- ⚙️ Configuraciones y opciones
- 📝 Caché y memoización
- 🌐 Parsing de JSON/APIs
- 📚 Índices y lookups 🎯 Representación de objetos
    
## Complejidad Temporal

| Operación | Complejidad Promedio | Peor Caso |
|-----------|---------------------|-----------|
| Acceso get/set | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search (in) | O(1) | O(n) |
| Iteration | O(n) | O(n) |

## Restricciones de Claves

### ✅ Claves Válidas (Hashables)
```python
dict_valido = {
    "string": 1,
    42: 2,
    3.14: 3,
    True: 4,
    (1, 2): 5,
    None: 6
}
```

### ❌ Claves Inválidas (No Hashables)
```python
# Esto NO funciona
# dict_invalido = {
#     [1, 2]: "lista",        # Error
#     {1: 2}: "diccionario",  # Error
#     {1, 2}: "conjunto"      # Error
# }
```

## Buenas Prácticas

✅ Usar claves descriptivas y consistentes  
✅ Preferir `get()` sobre acceso directo para evitar KeyError  
✅ Usar `setdefault()` para valores por defecto  
✅ Usar dict comprehensions para transformaciones  
✅ Validar existencia de claves con `in`  
✅ Usar `defaultdict` para contadores o agrupaciones  

❌ No usar claves mutables (listas, sets, dicts)  
❌ Evitar claves con tipos mixtos sin razón  
❌ No modificar diccionario durante iteración  
❌ No usar diccionarios para datos ordenados críticos (usa list de tuplas)  

## Patrones Comunes

### Contador de Frecuencias
```python
texto = "hola mundo"
frecuencia = {}
for char in texto:
    frecuencia[char] = frecuencia.get(char, 0) + 1
```

### Agrupar por Criterio
```python
estudiantes = [
    {"nombre": "Ana", "grado": "A"},
    {"nombre": "Luis", "grado": "B"},
    {"nombre": "María", "grado": "A"}
]

por_grado = {}
for est in estudiantes:
    grado = est["grado"]
    por_grado.setdefault(grado, []).append(est["nombre"])
```

### Cache/Memoización
```python
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    resultado = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = resultado
    return resultado
```

## Comparación: dict vs otros tipos

| Característica | dict | list | set |
|----------------|------|------|-----|
| Ordenado | Sí (3.7+) | Sí | No |
| Indexado | Por clave | Por índice | N/A |
| Duplicados | Claves únicas | Sí | No |
| Mutable | Sí | Sí | Sí |
| Búsqueda | O(1) | O(n) | O(1) |
| Uso principal | Mapeos | Secuencias | Únicos |
