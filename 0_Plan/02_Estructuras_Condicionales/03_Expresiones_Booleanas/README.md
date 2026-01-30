# Expresiones Booleanas

## Objetivos de Aprendizaje
- Entender qué valores son considerados verdaderos o falsos en Python
- Dominar las expresiones booleanas complejas
- Aprender a simplificar condiciones
- Conocer los valores Truthy y Falsy

## Conceptos Teóricos

### ¿Qué es una Expresión Booleana?

Una expresión booleana es cualquier expresión que se evalúa como `True` o `False`.

**Ejemplos:**
```python
5 > 3                    # True
edad >= 18               # Puede ser True o False
usuario == "admin"       # Puede ser True o False
x > 0 and x < 100       # True o False
```

## Valores Truthy y Falsy

En Python, no solo `True` y `False` tienen valor booleano. Cualquier valor puede ser evaluado en un contexto booleano.

### Valores que son False (Falsy)

Los siguientes valores se consideran **False** en contextos booleanos:

| Valor | Tipo | Descripción |
|-------|------|-------------|
| `False` | bool | Valor booleano False |
| `None` | NoneType | Ausencia de valor |
| `0` | int | Cero entero |
| `0.0` | float | Cero decimal |
| `0j` | complex | Cero complejo |
| `''` | str | String vacío |
| `[]` | list | Lista vacía |
| `()` | tuple | Tupla vacía |
| `{}` | dict | Diccionario vacío |
| `set()` | set | Conjunto vacío |
| `range(0)` | range | Rango vacío |

### Valores que son True (Truthy)

**TODO lo demás** se considera **True**, incluyendo:

```python
True                    # bool True
1, 2, -5, 42           # Cualquier número diferente de cero
"texto", "0", " "      # Cualquier string no vacío
[1], [0], [False]      # Cualquier lista no vacía
(1,), (0,)             # Cualquier tupla no vacía
{'key': 'value'}       # Cualquier dict no vacío
{1, 2, 3}             # Cualquier set no vacío
```

## Función bool()

La función `bool()` convierte cualquier valor a su equivalente booleano.

```python
bool(0)          # False
bool(1)          # True
bool("")         # False
bool("texto")    # True
bool([])         # False
bool([1, 2])     # True
bool(None)       # False
```

## Expresiones Booleanas en Acción

### 1. Uso Directo de Truthy/Falsy
```python
# En lugar de:
if len(lista) > 0:
    print("Lista tiene elementos")

# Puedes usar:
if lista:  # Más pythónico
    print("Lista tiene elementos")
```

### 2. Verificación de Existencia
```python
nombre = input("Nombre: ")

# Verificar si el usuario ingresó algo
if nombre:  # Si no está vacío
    print(f"Hola {nombre}")
else:
    print("No ingresaste un nombre")
```

### 3. Valores por Defecto con `or`
```python
# Si el usuario no ingresa nada, usa un valor por defecto
nombre = input("Nombre (opcional): ") or "Anónimo"
edad = input("Edad (opcional): ") or "No especificada"
```

## Comparaciones Múltiples

### Comparaciones Encadenadas
Python permite encadenar comparaciones de manera elegante:

```python
# En lugar de:
if x > 0 and x < 100:
    print("x está entre 0 y 100")

# Puedes usar:
if 0 < x < 100:  # Más legible
    print("x está entre 0 y 100")
```

**Más ejemplos:**
```python
# Verificar que está en rango
if 18 <= edad <= 65:
    print("Edad laboral")

# Múltiples comparaciones
if a < b < c < d:
    print("Orden ascendente")

# Igualdad múltiple
if x == y == z:
    print("Todos son iguales")
```

## Operadores de Identidad

### `is` vs `==`

- **`==`**: Compara valores (igualdad de contenido)
- **`is`**: Compara identidad (mismo objeto en memoria)

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (mismo contenido)
print(a is b)  # False (diferentes objetos)
print(a is c)  # True (mismo objeto)
```

**Uso común de `is`:**
```python
# Verificar None (siempre usa 'is')
if variable is None:
    print("Sin valor")

if variable is not None:
    print("Tiene valor")

# Verificar True/False (aunque no es necesario)
if flag is True:
    print("Verdadero")
```

## Operadores de Pertenencia

### `in` y `not in`

Verifican si un elemento está en una secuencia:

```python
# En strings
if "python" in texto.lower():
    print("Contiene 'python'")

# En listas
if nombre in lista_usuarios:
    print("Usuario registrado")

# En diccionarios (verifica claves)
if "edad" in diccionario:
    print("Tiene el campo 'edad'")

# Negación
if email not in lista_bloqueados:
    print("Email válido")
```

## Simplificación de Expresiones

### Ejemplo 1: Redundancia
```python
# ❌ REDUNDANTE
if es_adulto == True:
    print("Adulto")

# ✅ SIMPLIFICADO
if es_adulto:
    print("Adulto")
```

### Ejemplo 2: Doble Negación
```python
# ❌ CONFUSO
if not (not condicion):
    print("Confuso")

# ✅ SIMPLE
if condicion:
    print("Claro")
```

### Ejemplo 3: Asignación Condicional
```python
# ❌ VERBOSO
if puntaje >= 100:
    nivel = "Alto"
else:
    nivel = "Bajo"

# ✅ CONCISO (operador ternario)
nivel = "Alto" if puntaje >= 100 else "Bajo"
```

## Expresiones Complejas

### Ejemplo: Validación de Datos
```python
def validar_usuario(usuario, edad, email):
    """Valida los datos de un usuario."""
    
    # Expresión booleana compleja
    usuario_valido = (
        usuario and                    # No vacío
        len(usuario) >= 3 and         # Longitud mínima
        usuario.isalnum() and         # Solo alfanumérico
        edad and                       # Edad proporcionada
        18 <= edad <= 120 and         # Rango válido
        email and                      # Email proporcionado
        "@" in email and              # Tiene @
        "." in email.split("@")[1]    # Dominio válido
    )
    
    return usuario_valido
```

### Ejemplo: Reglas de Negocio
```python
def calcular_descuento(monto, es_cliente_vip, dias_desde_compra):
    """Calcula el descuento aplicable."""
    
    # Múltiples condiciones de negocio
    descuento_vip = es_cliente_vip and monto >= 100
    descuento_volumen = monto >= 1000
    descuento_recompra = dias_desde_compra <= 30 and monto >= 50
    
    # Retorna el mejor descuento
    if descuento_volumen:
        return 0.25  # 25%
    elif descuento_vip:
        return 0.20  # 20%
    elif descuento_recompra:
        return 0.15  # 15%
    else:
        return 0.0   # Sin descuento
```

## Ejemplos Prácticos

### Ejemplo 1: Verificación de Lista Vacía
```python
items = []

# Forma pythónica
if not items:
    print("Lista vacía")

# Menos pythónico
if len(items) == 0:
    print("Lista vacía")
```

### Ejemplo 2: Verificación de String
```python
nombre = input("Nombre: ")

# Verificar que no esté vacío y no sea solo espacios
if nombre and not nombre.isspace():
    print(f"Hola {nombre}")
else:
    print("Nombre inválido")
```

### Ejemplo 3: Valores Opcionales
```python
config = {
    "debug": True,
    "timeout": 30
}

# Usar .get() con valor por defecto
debug_mode = config.get("debug", False)
max_retries = config.get("max_retries", 3)  # No existe, usa 3
```

## Ejercicios Propuestos

### Ejercicio 1: Truthy y Falsy
Prueba `bool()` con diferentes valores:
- Números: 0, 1, -1, 0.0
- Strings: "", "0", " ", "False"
- Colecciones: [], [0], {}, {"key": None}

### Ejercicio 2: Validador de Entrada
Crea una función que valide entrada del usuario:
- No debe estar vacía
- No debe ser solo espacios
- Longitud entre 3 y 20 caracteres

### Ejercicio 3: Verificador de Email
Crea una función que valide un email:
- No vacío
- Contiene @
- Tiene texto antes y después de @
- El dominio tiene un punto

### Ejercicio 4: Filtro de Lista
Filtra una lista removiendo valores falsy:
```python
lista = [0, 1, "", "texto", None, False, [], [1], {}, {"a": 1}]
# Resultado esperado: [1, "texto", [1], {"a": 1}]
```

### Ejercicio 5: Comparaciones Encadenadas
Clasifica notas usando comparaciones encadenadas:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: 0-59

### Ejercicio 6: Optimizador de Condiciones
Simplifica estas expresiones:
```python
# 1
if variable == True:
    pass

# 2
if len(lista) > 0:
    pass

# 3
if not (a > b):
    pass
```

## Buenas Prácticas

### ✅ DO (Hacer)

```python
# 1. Usa truthy/falsy apropiadamente
if lista:
    procesar(lista)

# 2. Verifica None con 'is'
if valor is None:
    inicializar()

# 3. Usa 'in' para pertenencia
if item in coleccion:
    procesar(item)

# 4. Comparaciones encadenadas
if 0 <= edad < 18:
    categoria = "Menor"
```

### ❌ DON'T (No Hacer)

```python
# 1. No compares con True/False explícitamente
if variable == True:  # MAL
    pass

# 2. No uses == para None
if variable == None:  # MAL
    pass

# 3. No uses len() innecesariamente
if len(lista) > 0:  # MAL
    pass

# 4. No hagas doble negación
if not (not condicion):  # MAL
    pass
```

## Tabla de Referencia Rápida

| Expresión | Resultado | Explicación |
|-----------|-----------|-------------|
| `bool(0)` | False | Cero es falsy |
| `bool(1)` | True | Cualquier número != 0 |
| `bool("")` | False | String vacío es falsy |
| `bool(" ")` | True | String con espacio no está vacío |
| `bool([])` | False | Lista vacía es falsy |
| `bool([0])` | True | Lista con elemento (aunque sea 0) |
| `bool(None)` | False | None es falsy |
| `"x" in "texto"` | True | 'x' está en 'texto' |
| `5 in [1,2,3]` | False | 5 no está en la lista |
| `0 < 5 < 10` | True | Comparación encadenada |
| `a is b` | ? | Compara identidad de objetos |
| `a == b` | ? | Compara valores |

## Recursos Adicionales
- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Boolean Operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)
- [Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)

## Notas Importantes
- En Python, casi todo puede ser evaluado como True o False
- Solo unos pocos valores son False (0, None, vacíos, False)
- Usa `is` para comparar con None, no `==`
- Las comparaciones encadenadas son una característica pythónica
- Simplifica tus expresiones booleanas para mayor legibilidad
