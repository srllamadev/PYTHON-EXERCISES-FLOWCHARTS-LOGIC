# if, elif, else

## Objetivos de Aprendizaje
- Comprender cómo funcionan las estructuras condicionales
- Dominar la sintaxis de if, elif y else
- Aprender a anidar condicionales cuando sea necesario
- Escribir código condicional claro y mantenible

## Conceptos Teóricos

### ¿Qué son las Estructuras Condicionales?

Las estructuras condicionales permiten que tu programa tome decisiones y ejecute diferentes bloques de código según se cumplan o no ciertas condiciones.

### Sintaxis Básica

#### 1. Sentencia `if` Simple

```python
if condicion:
    # Código que se ejecuta si la condición es True
    instruccion1
    instruccion2
```

**Importante:** La indentación (espacios al inicio) es obligatoria en Python.

#### 2. Sentencia `if-else`

```python
if condicion:
    # Se ejecuta si la condición es True
    instruccion1
else:
    # Se ejecuta si la condición es False
    instruccion2
```

#### 3. Sentencia `if-elif-else`

```python
if condicion1:
    # Se ejecuta si condicion1 es True
    instruccion1
elif condicion2:
    # Se ejecuta si condicion1 es False y condicion2 es True
    instruccion2
elif condicion3:
    # Se ejecuta si condicion1 y condicion2 son False, y condicion3 es True
    instruccion3
else:
    # Se ejecuta si todas las condiciones anteriores son False
    instruccion4
```

### Reglas Importantes

1. **Dos puntos (`:`)** - Obligatorios después de cada condición
2. **Indentación** - Usa 4 espacios (estándar PEP 8)
3. **Evaluación secuencial** - Se evalúa de arriba hacia abajo
4. **Solo un bloque se ejecuta** - El primero que sea True
5. **else es opcional** - No siempre es necesario

## Ejemplos Prácticos

### Ejemplo 1: if Simple
```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar")

print("Programa terminado")
```

**Salida:**
```
Eres mayor de edad
Puedes votar
Programa terminado
```

### Ejemplo 2: if-else
```python
temperatura = 15

if temperatura > 25:
    print("Hace calor")
    print("Usa ropa ligera")
else:
    print("Hace frío")
    print("Usa abrigo")

print("Que tengas un buen día")
```

**Salida:**
```
Hace frío
Usa abrigo
Que tengas un buen día
```

### Ejemplo 3: if-elif-else
```python
calificacion = 85

if calificacion >= 90:
    letra = "A"
    print("Excelente")
elif calificacion >= 80:
    letra = "B"
    print("Muy bien")
elif calificacion >= 70:
    letra = "C"
    print("Bien")
elif calificacion >= 60:
    letra = "D"
    print("Suficiente")
else:
    letra = "F"
    print("Reprobado")

print(f"Tu calificación es: {letra}")
```

**Salida:**
```
Muy bien
Tu calificación es: B
```

### Ejemplo 4: Comparaciones Encadenadas
```python
edad = 25

# Forma pythónica
if 18 <= edad < 65:
    print("Adulto en edad laboral")

# Equivalente a:
if edad >= 18 and edad < 65:
    print("Adulto en edad laboral")
```

### Ejemplo 5: Condicionales Anidados
```python
edad = 20
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Puede conducir")
    else:
        print("Mayor de edad pero sin licencia")
else:
    print("Menor de edad, no puede conducir")
```

**Mejor forma (sin anidación excesiva):**
```python
if edad < 18:
    print("Menor de edad, no puede conducir")
elif not tiene_licencia:
    print("Mayor de edad pero sin licencia")
else:
    print("Puede conducir")
```

### Ejemplo 6: Validación de Entrada
```python
numero = int(input("Ingresa un número del 1 al 10: "))

if numero < 1:
    print("Error: El número es muy pequeño")
elif numero > 10:
    print("Error: El número es muy grande")
else:
    print(f"Número válido: {numero}")
```

### Ejemplo 7: Verificador de Día de la Semana
```python
dia = input("Ingresa un día de la semana: ").lower()

if dia == "lunes" or dia == "martes" or dia == "miercoles":
    print("Inicio de semana")
elif dia == "jueves" or dia == "viernes":
    print("Fin de semana laboral")
elif dia == "sabado" or dia == "domingo":
    print("Fin de semana")
else:
    print("Día no válido")
```

### Ejemplo 8: Calculadora de IMC con Categorías
```python
peso = 70
altura = 1.75

imc = peso / (altura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    categoria = "Bajo peso"
    recomendacion = "Consulta a un nutricionista"
elif imc < 25:
    categoria = "Peso normal"
    recomendacion = "Mantén tu estilo de vida saludable"
elif imc < 30:
    categoria = "Sobrepeso"
    recomendacion = "Considera aumentar tu actividad física"
else:
    categoria = "Obesidad"
    recomendacion = "Consulta a un profesional de la salud"

print(f"Categoría: {categoria}")
print(f"Recomendación: {recomendacion}")
```

## Ejercicios Propuestos

### Ejercicio 1: Verificador de Edad para Votar
Crea un programa que:
- Pida la edad del usuario
- Determine si puede votar (18 o más)
- Muestre un mensaje apropiado

### Ejercicio 2: Calculadora de Descuentos
Crea un programa que:
- Pida el monto de compra
- Aplique descuentos según:
  - >= $1000: 20% descuento
  - >= $500: 10% descuento
  - < $500: Sin descuento
- Muestre el precio final

### Ejercicio 3: Número Positivo, Negativo o Cero
Crea un programa que:
- Pida un número al usuario
- Determine si es positivo, negativo o cero
- Muestre el resultado

### Ejercicio 4: Año Bisiesto
Crea un programa que determine si un año es bisiesto.
Reglas:
- Divisible por 4 → bisiesto
- PERO si es divisible por 100 → NO bisiesto
- EXCEPTO si es divisible por 400 → SÍ bisiesto

Ejemplos: 2020 (bisiesto), 1900 (no), 2000 (bisiesto)

### Ejercicio 5: Calculadora Simple con Menú
Crea una calculadora que:
- Muestre un menú: 1.Suma, 2.Resta, 3.Multiplicación, 4.División
- Pida dos números
- Realice la operación seleccionada
- Valide división por cero

### Ejercicio 6: Clasificador de Triángulos
Dado tres lados, determina:
- Si forman un triángulo válido (suma de 2 lados > tercer lado)
- Tipo: Equilátero (3 lados iguales), Isósceles (2 iguales), Escaleno (todos diferentes)

### Ejercicio 7: Sistema de Calificaciones
Convierte calificación numérica a letra:
- 90-100: A (Excelente)
- 80-89: B (Muy bien)
- 70-79: C (Bien)
- 60-69: D (Suficiente)
- 0-59: F (Reprobado)

Incluye validación de rango (0-100).

## Diagramas de Flujo

### If Simple
```
    [Inicio]
       |
       v
   ¿condición?
    /      \
   Sí      No
   |        |
[código]    |
   |        |
   v        v
    [Continúa]
```

### If-Else
```
    [Inicio]
       |
       v
   ¿condición?
    /      \
   Sí      No
   |        |
[código1] [código2]
   |        |
   v        v
    [Continúa]
```

### If-Elif-Else
```
    [Inicio]
       |
       v
   ¿condición1?
    /      \
   Sí      No
   |        |
[código1]   v
   |    ¿condición2?
   |     /      \
   |    Sí      No
   |    |        |
   |  [código2] [código3]
   |    |        |
   v    v        v
    [Continúa]
```

## Buenas Prácticas

### ✅ DO (Hacer)

```python
# 1. Usar nombres descriptivos
if edad >= 18:
    print("Mayor de edad")

# 2. Evitar comparaciones redundantes
if es_estudiante:  # BIEN
    print("Descuento aplicado")

# 3. Usar guard clauses
if edad < 0:
    print("Error: edad inválida")
    return

# 4. Condiciones positivas primero
if archivo_existe:
    procesar_archivo()
else:
    print("Archivo no encontrado")
```

### ❌ DON'T (No Hacer)

```python
# 1. No comparar booleanos explícitamente
if es_estudiante == True:  # MAL
    print("Descuento")

# 2. No anidar excesivamente
if condicion1:
    if condicion2:
        if condicion3:  # MAL: Muy anidado
            codigo()

# 3. No repetir código en todas las ramas
if opcion == 1:
    print("Operación completada")  # Repetido
    procesar_uno()
elif opcion == 2:
    print("Operación completada")  # Repetido
    procesar_dos()
```

## Errores Comunes

### 1. Olvidar los dos puntos
```python
# ❌ ERROR
if edad >= 18
    print("Mayor")

# ✅ CORRECTO
if edad >= 18:
    print("Mayor")
```

### 2. Indentación incorrecta
```python
# ❌ ERROR
if edad >= 18:
print("Mayor")  # Sin indentación

# ✅ CORRECTO
if edad >= 18:
    print("Mayor")
```

### 3. Usar = en vez de ==
```python
# ❌ ERROR
if edad = 18:  # Esto es asignación
    print("Tiene 18")

# ✅ CORRECTO
if edad == 18:  # Esto es comparación
    print("Tiene 18")
```

### 4. Rango de valores mal definido
```python
# ❌ ERROR
if nota >= 90 and nota <= 100:  # Redundante

# ✅ CORRECTO
if 90 <= nota <= 100:  # Pythónico
```

## Recursos Adicionales
- [Documentación oficial - if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Real Python - Conditional Statements](https://realpython.com/python-conditional-statements/)
- [PEP 8 - Indentation](https://pep8.org/#indentation)

## Notas Importantes
- La indentación es OBLIGATORIA en Python (usa 4 espacios)
- Solo un bloque se ejecuta en una cadena if-elif-else
- `elif` es la abreviatura de "else if"
- Puedes tener múltiples `elif`, pero solo un `else`
- El bloque `else` es opcional
- Usa comparaciones encadenadas para rangos: `if 18 <= edad < 65:`
