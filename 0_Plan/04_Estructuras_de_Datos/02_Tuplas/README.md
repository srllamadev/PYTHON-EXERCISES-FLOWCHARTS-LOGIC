# Tuplas (tuple)

## ¿Qué son las Tuplas?

Las tuplas son estructuras de datos **inmutables** y **ordenadas** similares a las listas, pero que no pueden modificarse después de su creación. Son ideales para datos que no deben cambiar.

## Características Principales

- ✅ **Inmutables**: No se pueden modificar después de su creación
- ✅ **Ordenadas**: Mantienen el orden de los elementos
- ✅ **Indexadas**: Acceso mediante índices (0, 1, 2, ...)
- ✅ **Permiten duplicados**: Pueden tener elementos repetidos
- ✅ **Heterogéneas**: Pueden contener diferentes tipos de datos
- ✅ **Hashables**: Pueden ser claves de diccionarios
- ✅ **Más rápidas**: Mayor rendimiento que las listas

## Sintaxis Básica

```python
# Creación de tuplas
tupla_vacia = ()
numeros = (1, 2, 3, 4, 5)
punto = (10, 20)
mixta = (1, "dos", 3.0, True)

# Sin paréntesis (empaquetado)
coordenadas = 10, 20, 30

# Tupla de un elemento (requiere coma)
un_elemento = (42,)  # Correcto
no_tupla = (42)      # Esto es un int, NO una tupla

# Constructor tuple()
desde_lista = tuple([1, 2, 3])
desde_string = tuple("Python")
```

## Operaciones Comunes

### Acceso a Elementos
```python
colores = ("rojo", "verde", "azul")
primero = colores[0]     # "rojo"
ultimo = colores[-1]     # "azul"
```

### Slicing
```python
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
primeros = numeros[:3]      # (0, 1, 2)
ultimos = numeros[-3:]      # (7, 8, 9)
pares = numeros[::2]        # (0, 2, 4, 6, 8)
```

### Métodos Principales

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `count(x)` | Cuenta ocurrencias de x | `tupla.count(5)` |
| `index(x)` | Retorna índice de la primera ocurrencia | `tupla.index("valor")` |

> ⚠️ **Nota**: Las tuplas tienen solo 2 métodos porque son inmutables

## Desempaquetado de Tuplas

```python
# Desempaquetado básico
punto = (10, 20)
x, y = punto
print(f"x={x}, y={y}")  # x=10, y=20

# Desempaquetado con *
numeros = (1, 2, 3, 4, 5)
primero, *resto, ultimo = numeros
# primero=1, resto=[2, 3, 4], ultimo=5

# Intercambio de valores
a = 5
b = 10
a, b = b, a  # a=10, b=5

# Retorno múltiple de funciones
def obtener_coordenadas():
    return 10, 20, 30

x, y, z = obtener_coordenadas()
```

## Inmutabilidad

```python
# Esto NO funciona (error)
tupla = (1, 2, 3)
# tupla[0] = 10  # TypeError

# Pero se puede crear una nueva tupla
tupla = (10, 2, 3)  # OK

# Importante: Los objetos mutables dentro de tuplas SÍ pueden cambiar
tupla_con_lista = (1, [2, 3], 4)
tupla_con_lista[1].append(5)  # OK
# tupla_con_lista es ahora (1, [2, 3, 5], 4)
```

## Tuplas como Claves de Diccionarios

```python
# Las tuplas pueden ser claves (son hashables)
coordenadas_ciudades = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522, -118.2437): "Los Ángeles",
    (51.5074, -0.1278): "Londres"
}

# Las listas NO pueden ser claves
# esto_no_funciona = {[1, 2]: "valor"}  # TypeError
```

## Tuplas Nombradas (namedtuple)

```python
from collections import namedtuple

# Definir estructura
Punto = namedtuple('Punto', ['x', 'y'])
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])

# Crear instancias
p = Punto(10, 20)
persona = Persona('Ana', 25, 'Madrid')

# Acceso por nombre
print(p.x, p.y)  # 10 20
print(persona.nombre)  # Ana

# También funciona acceso por índice
print(p[0], p[1])  # 10 20
```

## Comparación: Tuplas vs Listas

| Característica | Tupla | Lista |
|----------------|-------|-------|
| Mutabilidad | Inmutable | Mutable |
| Sintaxis | `()` | `[]` |
| Métodos | 2 (count, index) | Muchos |
| Performance | Más rápida | Más lenta |
| Uso de memoria | Menor | Mayor |
| Como clave dict | ✅ Sí | ❌ No |
| Casos de uso | Datos fijos | Datos cambiantes |

## Casos de Uso Comunes

- 🔒 Datos que no deben modificarse (constantes)
- 🗝️ Claves de diccionarios
- 📍 Coordenadas o puntos (x, y, z)
- 📅 Fechas y tiempos
- 🔄 Retorno múltiple de funciones
- 📊 Registros de base de datos
- 🎯 Valores de configuración inmutables

## Complejidad Temporal

| Operación | Complejidad |
|-----------|-------------|
| Acceso por índice | O(1) |
| Search | O(n) |
| Creación | O(n) |
| Slice | O(k) donde k es tamaño del slice |

## Ventajas de la Inmutabilidad

✅ **Seguridad**: No se pueden modificar accidentalmente  
✅ **Performance**: Más rápidas que listas  
✅ **Hashable**: Pueden ser claves de diccionarios  
✅ **Threading**: Seguras en entornos multi-hilo  
✅ **Integridad**: Garantizan datos consistentes  

## Cuándo Usar Tuplas vs Listas

### Usa Tuplas cuando:
- Los datos no deben cambiar
- Necesitas usar como clave de diccionario
- Quieres mejor rendimiento
- Representas registros estructurados
- Retornas múltiples valores de una función

### Usa Listas cuando:
- Los datos pueden/deben cambiar
- Necesitas agregar/eliminar elementos
- Requieres métodos de manipulación
- La colección crece dinámicamente

## Buenas Prácticas

✅ Usar para datos inmutables por naturaleza  
✅ Preferir para retorno de funciones  
✅ Usar namedtuple para mayor claridad  
✅ Aprovechar el desempaquetado  
✅ Usar como claves de diccionarios  

❌ No usar si necesitas modificar datos  
❌ Evitar tuplas muy largas (dificultan lectura)  
❌ No abusar de índices numéricos (usa namedtuple)  
