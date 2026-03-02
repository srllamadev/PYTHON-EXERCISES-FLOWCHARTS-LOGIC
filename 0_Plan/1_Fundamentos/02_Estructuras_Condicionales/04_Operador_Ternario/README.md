# Operador Ternario

## Objetivos de Aprendizaje
- Dominar la sintaxis del operador ternario en Python
- Saber cuándo usar y cuándo evitar el operador ternario
- Escribir código condicional conciso y legible
- Entender las alternativas al operador ternario

## Conceptos Teóricos

### ¿Qué es el Operador Ternario?

El operador ternario (también llamado **expresión condicional**) es una forma concisa de escribir un `if-else` simple en una sola línea.

### Sintaxis

```python
valor_si_true if condicion else valor_si_false
```

**Equivalente a:**
```python
if condicion:
    resultado = valor_si_true
else:
    resultado = valor_si_false
```

### Estructura

```
┌──────────────┐     ┌─────────┐     ┌──────────────┐
│ Valor si True│  if │Condición│ else│ Valor si False│
└──────────────┘     └─────────┘     └──────────────┘
```

## Ejemplos Básicos

### Ejemplo 1: Asignación Simple
```python
# Con if-else tradicional
edad = 20
if edad >= 18:
    estado = "Mayor de edad"
else:
    estado = "Menor de edad"

# Con operador ternario
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
```

### Ejemplo 2: Retorno de Función
```python
# Tradicional
def obtener_descuento(es_miembro):
    if es_miembro:
        return 0.15
    else:
        return 0.0

# Con ternario
def obtener_descuento(es_miembro):
    return 0.15 if es_miembro else 0.0
```

### Ejemplo 3: Formateo de Salida
```python
puntos = 1500

# Tradicional
if puntos > 1000:
    mensaje = "¡Alto nivel!"
else:
    mensaje = "Sigue intentando"

# Con ternario
mensaje = "¡Alto nivel!" if puntos > 1000 else "Sigue intentando"
```

## Casos de Uso Comunes

### 1. Valores por Defecto
```python
nombre = input_usuario if input_usuario else "Anónimo"
precio = precio_descuento if hay_descuento else precio_normal
```

### 2. Selección de Valores
```python
# Obtener el mayor de dos números
maximo = a if a > b else b

# Obtener el menor de dos números
minimo = a if a < b else b
```

### 3. Formateo Condicional
```python
# Singular vs plural
items = 1
texto = f"{items} item" if items == 1 else f"{items} items"

# Signo de número
numero = -5
signo = "positivo" if numero >= 0 else "negativo"
```

### 4. Valores Booleanos
```python
# Invertir booleano
activo = False
nuevo_estado = False if activo else True

# Mejor forma para invertir
nuevo_estado = not activo
```

## Operadores Ternarios Anidados

⚠️ **Precaución:** Los ternarios anidados pueden ser confusos.

### Sintaxis de Anidación
```python
valor_si_cond1 if condicion1 else (valor_si_cond2 if condicion2 else valor_default)
```

### Ejemplo: Calificaciones
```python
nota = 85

# Ternario anidado (poco legible)
letra = "A" if nota >= 90 else ("B" if nota >= 80 else ("C" if nota >= 70 else "F"))

# Mejor usar if-elif-else tradicional
if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
else:
    letra = "F"
```

**Regla:** Si necesitas más de 2 niveles, usa `if-elif-else` tradicional.

## Cuándo Usar el Operador Ternario

### ✅ Casos Apropiados

1. **Asignaciones simples**
```python
estado = "activo" if is_active else "inactivo"
```

2. **Valores por defecto**
```python
nombre = input_nombre or "Sin nombre"  # Alternativa
nombre = input_nombre if input_nombre else "Sin nombre"  # Ternario
```

3. **Expresiones cortas en f-strings**
```python
print(f"El usuario está {'activo' if is_active else 'inactivo'}")
```

4. **Retorno de funciones simples**
```python
def es_par(n):
    return True if n % 2 == 0 else False
    # Mejor aún: return n % 2 == 0
```

### ❌ Casos a Evitar

1. **Lógica compleja**
```python
# ❌ MAL: Muy complejo
resultado = funcion1() if condicion_larga and otra_condicion else funcion2() if tercera_condicion else funcion3()

# ✅ BIEN: Usar if-elif-else
if condicion_larga and otra_condicion:
    resultado = funcion1()
elif tercera_condicion:
    resultado = funcion2()
else:
    resultado = funcion3()
```

2. **Múltiples anidaciones**
```python
# ❌ MAL: Difícil de leer
x = a if cond1 else (b if cond2 else (c if cond3 else d))

# ✅ BIEN: Más claro
if cond1:
    x = a
elif cond2:
    x = b
elif cond3:
    x = c
else:
    x = d
```

3. **Con efectos secundarios**
```python
# ❌ MAL: Efectos secundarios ocultos
x = procesar_y_modificar() if condicion else otro_proceso()

# ✅ BIEN: Más explícito
if condicion:
    x = procesar_y_modificar()
else:
    x = otro_proceso()
```

## Ejemplos Prácticos

### Ejemplo 1: Verificador de Paridad
```python
numero = 7

# Ternario
tipo = "Par" if numero % 2 == 0 else "Impar"
print(f"{numero} es {tipo}")
```

### Ejemplo 2: Descuento
```python
total = 150
es_vip = True

# Ternario
descuento = total * 0.20 if es_vip else 0
precio_final = total - descuento

print(f"Total: ${total}")
print(f"Descuento: ${descuento}")
print(f"Final: ${precio_final}")
```

### Ejemplo 3: Mensaje de Saludo
```python
hora = 14

# Ternario
saludo = "Buenos días" if hora < 12 else ("Buenas tardes" if hora < 20 else "Buenas noches")
print(saludo)

# Mejor con if-elif-else para 3+ opciones
if hora < 12:
    saludo = "Buenos días"
elif hora < 20:
    saludo = "Buenas tardes"
else:
    saludo = "Buenas noches"
```

### Ejemplo 4: Formateo de Texto
```python
cantidad = 1

# Singular vs plural
mensaje = f"Tienes {cantidad} mensaje" if cantidad == 1 else f"Tienes {cantidad} mensajes"
print(mensaje)
```

### Ejemplo 5: Validación
```python
edad = 17

# Ternario
acceso = "Permitido" if edad >= 18 else "Denegado"
emoji = "✅" if edad >= 18 else "❌"

print(f"{emoji} Acceso: {acceso}")
```

## Alternativas al Operador Ternario

### 1. Usar Diccionario (para múltiples opciones)
```python
# En lugar de ternarios anidados
dia = 3
nombre_dia = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}.get(dia, "Día inválido")
```

### 2. Usar Funciones
```python
# Para lógica repetitiva
def obtener_categoria_edad(edad):
    if edad < 13:
        return "Niño"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto mayor"

categoria = obtener_categoria_edad(25)
```

### 3. Usar `or` para Valores por Defecto
```python
# En lugar de ternario
nombre = input_usuario or "Anónimo"

# Equivalente ternario
nombre = input_usuario if input_usuario else "Anónimo"
```

## Ejercicios Propuestos

### Ejercicio 1: Convertir a Ternario
Convierte estos if-else a operadores ternarios:
```python
# 1
if temperatura > 30:
    clima = "Calor"
else:
    clima = "Frío"

# 2
if edad >= 18:
    puede_votar = True
else:
    puede_votar = False
```

### Ejercicio 2: Mayor de Tres Números
Usa ternarios para encontrar el mayor de tres números.
```python
a, b, c = 15, 23, 8
# Encuentra el mayor usando ternarios
```

### Ejercicio 3: Calculadora de Descuento
Usa ternario para calcular descuento:
- Compra >= $1000: 20% descuento
- Compra < $1000: sin descuento

### Ejercicio 4: Clasificador de Nota
Usa ternario simple para:
- Nota >= 60: "Aprobado"
- Nota < 60: "Reprobado"

### Ejercicio 5: Formateo de Precio
Formatea un precio con o sin descuento:
```python
precio = 100
tiene_descuento = True
# Muestra: "$100" o "$100 (descuento aplicado)"
```

### Ejercicio 6: Refactorizar Ternarios Complejos
Simplifica este ternario anidado usando if-elif-else:
```python
x = a if cond1 else (b if cond2 else (c if cond3 else d))
```

## Comparación: Ternario vs if-else

| Aspecto | Operador Ternario | if-else Tradicional |
|---------|-------------------|---------------------|
| **Longitud** | 1 línea | 3-4 líneas |
| **Legibilidad** | Buena para casos simples | Mejor para lógica compleja |
| **Anidación** | Difícil de leer | Más clara |
| **Uso** | Asignaciones simples | Cualquier caso |
| **Expresión** | Sí (retorna valor) | No (es statement) |

## Buenas Prácticas

### ✅ DO (Hacer)

```python
# 1. Usa para asignaciones simples
estado = "on" if activo else "off"

# 2. Mantén las líneas cortas
es_mayor = True if edad >= 18 else False

# 3. Usa en f-strings
print(f"Usuario {'activo' if online else 'offline'}")

# 4. Simplifica cuando sea posible
# En lugar de:
es_par = True if n % 2 == 0 else False
# Usa:
es_par = n % 2 == 0
```

### ❌ DON'T (No Hacer)

```python
# 1. No anides demasiado
resultado = a if c1 else (b if c2 else (c if c3 else d))  # MAL

# 2. No hagas líneas muy largas
mensaje = "Este es un mensaje muy largo..." if condicion_compleja and otra_condicion else "Otro mensaje largo..."  # MAL

# 3. No uses para lógica compleja
x = calcular_algo_complejo() if validar_muchas_cosas() else procesar_alternativa()  # MAL

# 4. No uses efectos secundarios
x = modificar_estado() if cond else resetear()  # MAL
```

## Trucos y Tips

### 1. Ternario en Comprensiones de Lista
```python
numeros = [1, 2, 3, 4, 5]
# Duplicar pares, triplicar impares
resultado = [n*2 if n % 2 == 0 else n*3 for n in numeros]
```

### 2. Ternario en Funciones Lambda
```python
es_adulto = lambda edad: True if edad >= 18 else False
```

### 3. Ternario para Valores Mínimo/Máximo
```python
maximo = a if a > b else b
minimo = a if a < b else b

# Aunque es mejor usar:
maximo = max(a, b)
minimo = min(a, b)
```

## Recursos Adicionales
- [PEP 308 - Conditional Expressions](https://www.python.org/dev/peps/pep-0308/)
- [Real Python - Ternary Operator](https://realpython.com/python-conditional-statements/#conditional-expressions-pythons-ternary-operator)
- [Python Docs - Conditional Expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

## Notas Importantes
- El operador ternario es una **expresión**, no un statement
- Se evalúa y retorna un valor
- Mantén la simplicidad: si tienes dudas, usa if-else tradicional
- La legibilidad siempre es más importante que la brevedad
- Evita ternarios anidados con más de 2 niveles
- Es ideal para asignaciones simples de una sola línea
