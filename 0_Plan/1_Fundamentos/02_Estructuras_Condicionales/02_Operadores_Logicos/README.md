# Operadores Lógicos

## Objetivos de Aprendizaje
- Dominar los operadores lógicos AND, OR y NOT
- Combinar múltiples condiciones de manera efectiva
- Entender la precedencia de operadores lógicos
- Conocer el concepto de cortocircuito de evaluación

## Conceptos Teóricos

### Los Tres Operadores Lógicos

Python tiene tres operadores lógicos principales:

1. **`and`** - Y lógico (conjunción)
2. **`or`** - O lógico (disyunción)
3. **`not`** - Negación lógica

### 1. Operador `and`

Retorna `True` solo si **ambas** condiciones son verdaderas.

**Sintaxis:**
```python
condicion1 and condicion2
```

**Tabla de Verdad:**
| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

**Ejemplos:**
```python
edad = 25
tiene_licencia = True

# Ambas condiciones deben ser True
puede_conducir = edad >= 18 and tiene_licencia  # True

# Si una es False, el resultado es False
edad = 16
puede_conducir = edad >= 18 and tiene_licencia  # False
```

### 2. Operador `or`

Retorna `True` si **al menos una** condición es verdadera.

**Sintaxis:**
```python
condicion1 or condicion2
```

**Tabla de Verdad:**
| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

**Ejemplos:**
```python
es_fin_de_semana = dia == "sábado" or dia == "domingo"

# True si alguna condición es True
tiene_descuento = es_estudiante or es_senior or es_miembro  # True si alguno
```

### 3. Operador `not`

Invierte el valor booleano (negación).

**Sintaxis:**
```python
not condicion
```

**Tabla de Verdad:**
| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

**Ejemplos:**
```python
archivo_existe = True
archivo_no_existe = not archivo_existe  # False

if not usuario_autenticado:
    print("Debe iniciar sesión")
```

## Combinación de Operadores

### Múltiples ANDs
```python
# Todas las condiciones deben ser True
if edad >= 18 and tiene_licencia and tiene_auto:
    print("Puede conducir su propio auto")
```

### Múltiples ORs
```python
# Al menos una condición debe ser True
if dia == "sábado" or dia == "domingo" or es_feriado:
    print("No hay clases")
```

### Combinación de AND y OR
```python
# Se puede combinar, pero usa paréntesis para claridad
if (edad >= 18 and tiene_licencia) or es_instructor:
    print("Puede conducir")
```

## Precedencia de Operadores Lógicos

**Orden de evaluación (de mayor a menor precedencia):**

1. **Paréntesis** `()`
2. **not**
3. **and**
4. **or**

**Ejemplo:**
```python
# Sin paréntesis
resultado = True or False and False
# Se evalúa como: True or (False and False)
# Resultado: True

# Con paréntesis (cambia el resultado)
resultado = (True or False) and False
# Se evalúa: (True) and False
# Resultado: False
```

**Recomendación:** Siempre usa paréntesis para mayor claridad.

## Cortocircuito de Evaluación

Python evalúa expresiones lógicas de izquierda a derecha y **detiene la evaluación** tan pronto como conoce el resultado.

### Cortocircuito con `and`
```python
# Si la primera condición es False, no evalúa la segunda
if False and funcion_costosa():
    # funcion_costosa() NUNCA se ejecuta
    pass

# Ejemplo práctico
if archivo != None and archivo.exists():
    # Primero verifica que archivo no sea None
    # Solo si no es None, llama a exists()
    leer_archivo()
```

### Cortocircuito con `or`
```python
# Si la primera condición es True, no evalúa la segunda
if True or funcion_costosa():
    # funcion_costosa() NUNCA se ejecuta
    pass

# Ejemplo práctico
nombre = input_usuario or "Anónimo"
# Si input_usuario está vacío (False), usa "Anónimo"
```

## Ejemplos Prácticos

### Ejemplo 1: Validación de Acceso
```python
usuario = "admin"
contraseña = "1234"
edad = 25

# Múltiples validaciones con AND
if usuario == "admin" and contraseña == "1234" and edad >= 18:
    print("Acceso concedido")
else:
    print("Acceso denegado")
```

### Ejemplo 2: Descuentos Múltiples
```python
es_estudiante = True
es_senior = False
es_miembro = False

# Al menos una condición con OR
if es_estudiante or es_senior or es_miembro:
    print("Tiene derecho a descuento")
    descuento = 0.15
else:
    print("Sin descuento")
    descuento = 0
```

### Ejemplo 3: Validación de Rango
```python
edad = 25

# Combinación de operadores
if edad >= 18 and edad <= 65:
    print("Adulto en edad laboral")

# Mejor forma (pythónica)
if 18 <= edad <= 65:
    print("Adulto en edad laboral")
```

### Ejemplo 4: Sistema de Alertas
```python
temperatura = 35
humedad = 80

# Múltiples condiciones
if temperatura > 30 and humedad > 70:
    print("⚠️ Alerta: Calor y humedad extremos")
elif temperatura > 30 or humedad > 70:
    print("⚠️ Precaución: Condiciones adversas")
else:
    print("✓ Condiciones normales")
```

### Ejemplo 5: Validación de Formulario
```python
nombre = "Juan"
email = "juan@email.com"
edad = 20

# Todas las validaciones deben pasar
formulario_valido = (
    nombre != "" and
    "@" in email and
    edad >= 18
)

if formulario_valido:
    print("✓ Formulario válido")
else:
    print("✗ Formulario inválido")
```

### Ejemplo 6: Operador NOT en Validaciones
```python
archivo_procesado = False

if not archivo_procesado:
    print("Procesando archivo...")
    procesar()

# Equivalente a:
if archivo_procesado == False:
    print("Procesando archivo...")
```

### Ejemplo 7: Verificación de Texto Vacío
```python
texto = input("Ingresa tu nombre: ")

# NOT para verificar si está vacío
if not texto or texto.isspace():
    print("Error: Debes ingresar un nombre")
else:
    print(f"Hola, {texto}")
```

## Ejercicios Propuestos

### Ejercicio 1: Sistema de Login
Crea un programa que:
- Pida usuario y contraseña
- Verifique que ambos sean correctos usando `and`
- Muestre "Acceso concedido" o "Acceso denegado"

### Ejercicio 2: Verificador de Día Laboral
Crea un programa que:
- Pida un día de la semana
- Use `or` para determinar si es día laboral
- Días laborales: lunes a viernes

### Ejercicio 3: Calculadora de Beca
Determina si un estudiante califica para beca:
- Promedio >= 85 AND situación económica baja
- OR promedio >= 95 (independiente de situación)

### Ejercicio 4: Validador de Edad para Actividad
Crea un programa que determine si puede hacer una actividad:
- Edad: 12-65 años
- Y no tener problemas de salud
- O tener autorización médica

### Ejercicio 5: Detector de Triángulo Rectángulo
Dados tres lados, verifica si forman un triángulo rectángulo:
- Usar el teorema de Pitágoras: a² + b² = c²
- Debe verificar las tres posibles combinaciones

### Ejercicio 6: Sistema de Membresía
Determina el tipo de acceso:
- VIP: (es_premium AND antiguedad > 1) OR monto_gastado > 10000
- Regular: es_miembro AND not es_premium
- Visitante: not es_miembro

## Expresiones Complejas

### Ejemplo: Validación de Contraseña Segura
```python
contraseña = "Python2024!"
longitud = len(contraseña)
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_minuscula = any(c.islower() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
tiene_especial = any(c in "!@#$%^&*()" for c in contraseña)

es_segura = (
    longitud >= 8 and
    tiene_mayuscula and
    tiene_minuscula and
    tiene_numero and
    tiene_especial
)

if es_segura:
    print("✓ Contraseña segura")
else:
    print("✗ Contraseña no cumple los requisitos")
```

## Leyes de De Morgan

Útiles para simplificar expresiones:

**Ley 1:** `not (A and B)` = `not A or not B`
```python
# Estas dos expresiones son equivalentes
if not (edad >= 18 and tiene_licencia):
    print("No puede conducir")

if edad < 18 or not tiene_licencia:
    print("No puede conducir")
```

**Ley 2:** `not (A or B)` = `not A and not B`
```python
# Estas dos expresiones son equivalentes
if not (es_fin_de_semana or es_feriado):
    print("Día laboral")

if not es_fin_de_semana and not es_feriado:
    print("Día laboral")
```

## Buenas Prácticas

### ✅ DO (Hacer)

```python
# 1. Usa paréntesis para claridad
if (edad >= 18 and tiene_licencia) or es_instructor:
    print("Puede conducir")

# 2. Divide condiciones complejas
es_adulto = edad >= 18
tiene_permiso = tiene_licencia or es_instructor
if es_adulto and tiene_permiso:
    print("Puede conducir")

# 3. Usa nombres descriptivos
if usuario_autenticado and tiene_permisos:
    mostrar_contenido_privado()
```

### ❌ DON'T (No Hacer)

```python
# 1. No comparar booleanos explícitamente
if condicion == True:  # MAL
    pass
if condicion:  # BIEN
    pass

# 2. No usar doble negación
if not (not condicion):  # MAL
if condicion:  # BIEN
    pass

# 3. No hacer condiciones demasiado complejas
if a and b and c and d and e and f or g and h:  # MAL
    pass
```

## Errores Comunes

### 1. Olvidar Paréntesis en Expresiones Mixtas
```python
# ❌ CONFUSO
if edad > 18 and altura > 1.60 or peso < 80:
    pass

# ✅ CLARO
if (edad > 18 and altura > 1.60) or peso < 80:
    pass
```

### 2. Usar `and` en vez de `or` (o viceversa)
```python
# ❌ ERROR (nunca será True)
if dia == "sábado" and dia == "domingo":
    pass

# ✅ CORRECTO
if dia == "sábado" or dia == "domingo":
    pass
```

### 3. Comparaciones Redundantes
```python
# ❌ REDUNDANTE
if edad >= 18 and edad < 100 and edad > 0:
    pass

# ✅ SIMPLIFICADO
if 0 < edad < 100 and edad >= 18:
    pass
```

## Recursos Adicionales
- [Documentación - Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Real Python - Logical Operators](https://realpython.com/python-operators-expressions/)
- [W3Schools - Python Booleans](https://www.w3schools.com/python/python_booleans.asp)

## Notas Importantes
- `and` retorna el primer valor False o el último valor si todos son True
- `or` retorna el primer valor True o el último valor si todos son False
- Usa el cortocircuito a tu favor para evitar errores
- Los paréntesis aumentan la legibilidad
- `not` tiene mayor precedencia que `and` y `or`
