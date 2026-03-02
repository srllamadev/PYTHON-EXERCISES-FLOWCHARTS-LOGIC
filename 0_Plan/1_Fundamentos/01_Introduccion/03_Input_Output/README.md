# Input/Output (Entrada/Salida)

## Objetivos de Aprendizaje
- Dominar la función `print()` para mostrar información
- Aprender a usar `input()` para recibir datos del usuario
- Conocer diferentes formas de formatear texto
- Entender la conversión de tipos en entrada de datos

## Conceptos Teóricos

### Output - Función `print()`

La función `print()` muestra información en la consola.

#### Sintaxis Básica
```python
print(objeto1, objeto2, ..., sep=' ', end='\n')
```

**Parámetros importantes:**
- `sep`: Separador entre objetos (por defecto: espacio)
- `end`: Carácter al final (por defecto: nueva línea `\n`)

### Input - Función `input()`

La función `input()` solicita datos al usuario.

#### Sintaxis Básica
```python
variable = input(prompt)
```

**Importante:** `input()` siempre retorna un **string** (texto).

## Función print() - Detalles

### 1. Print Básico
```python
print("Hola Mundo")
print(42)
print(3.14)
print(True)
```

### 2. Imprimir Múltiples Valores
```python
nombre = "Juan"
edad = 25
print("Nombre:", nombre, "Edad:", edad)
# Salida: Nombre: Juan Edad: 25
```

### 3. Parámetro `sep`
```python
print("Python", "Java", "C++", sep=" | ")
# Salida: Python | Java | C++

print(2024, 12, 25, sep="-")
# Salida: 2024-12-25
```

### 4. Parámetro `end`
```python
print("Cargando", end="...")
print("Completado")
# Salida: Cargando...Completado

# Imprimir en la misma línea
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
```

### 5. Caracteres Especiales
```python
print("Línea 1\nLínea 2")        # \n = nueva línea
print("Columna1\tColumna2")      # \t = tabulación
print("Texto \"entre comillas\"") # \" = comillas escapadas
print("Ruta: C:\\Users\\Docs")   # \\ = barra invertida
```

## Formateo de Strings

### 1. Concatenación
```python
nombre = "María"
mensaje = "Hola " + nombre + ", bienvenida"
print(mensaje)
```

### 2. f-strings (Recomendado - Python 3.6+)
```python
nombre = "Carlos"
edad = 30
altura = 1.75

# Formato básico
print(f"Me llamo {nombre} y tengo {edad} años")

# Con expresiones
print(f"El año que viene tendré {edad + 1} años")

# Formateo numérico
precio = 99.99999
print(f"Precio: ${precio:.2f}")  # 99.99 (2 decimales)

# Alineación
print(f"{'Nombre':<10} {'Edad':>5}")  # <: izq, >: der, ^: centro
print(f"{nombre:<10} {edad:>5}")
```

### 3. Método .format()
```python
mensaje = "Me llamo {} y tengo {} años".format("Ana", 28)
print(mensaje)

# Con índices
mensaje = "Me llamo {0} {1}. Apellido: {1}".format("Juan", "Pérez")
print(mensaje)  # Me llamo Juan Pérez. Apellido: Pérez

# Con nombres
mensaje = "Me llamo {nombre} y tengo {edad} años".format(nombre="Luis", edad=35)
print(mensaje)
```

### 4. Operador % (Antiguo)
```python
nombre = "Pedro"
edad = 40
print("Me llamo %s y tengo %d años" % (nombre, edad))
```

## Función input()

### 1. Input Básico
```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}")
```

### 2. Conversión de Tipos
```python
# input() siempre retorna string
edad_texto = input("¿Cuántos años tienes? ")
edad = int(edad_texto)  # Convertir a entero

# Forma abreviada
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides? "))
```

### 3. Validación Básica
```python
# Sin validación (puede generar error)
numero = int(input("Ingresa un número: "))

# Con validación simple
texto = input("Ingresa un número: ")
if texto.isdigit():
    numero = int(texto)
    print(f"Número ingresado: {numero}")
else:
    print("Error: No ingresaste un número válido")
```

## Ejemplos Prácticos

### Ejemplo 1: Programa de Saludo
```python
print("=" * 40)
print("PROGRAMA DE BIENVENIDA")
print("=" * 40)

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
ciudad = input("¿De dónde eres? ")

print("\n" + "-" * 40)
print(f"Hola {nombre}!")
print(f"Tienes {edad} años y vives en {ciudad}")
print(f"Bienvenido/a al curso de Python")
print("-" * 40)
```

### Ejemplo 2: Calculadora Simple
```python
print("CALCULADORA SIMPLE")
print("-" * 30)

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "Error: división por cero"

print("\nRESULTADOS:")
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} × {num2} = {multiplicacion}")
print(f"{num1} ÷ {num2} = {division}")
```

### Ejemplo 3: Formateo de Tabla
```python
print(f"{'Producto':<15} {'Precio':>10} {'Cantidad':>10}")
print("-" * 37)
print(f"{'Laptop':<15} ${1299.99:>9.2f} {5:>10}")
print(f"{'Mouse':<15} ${29.99:>9.2f} {120:>10}")
print(f"{'Teclado':<15} ${79.99:>9.2f} {45:>10}")
```

### Ejemplo 4: Entrada Múltiple
```python
# Una sola línea de entrada con split()
datos = input("Ingresa tu nombre y edad separados por espacio: ")
nombre, edad = datos.split()

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
```

### Ejemplo 5: Formato con Relleno
```python
titulo = "Python"
print(f"{titulo:*^30}")  # ************Python************

numero = 42
print(f"{numero:05}")    # 00042 (rellena con ceros)

precio = 1234.5
print(f"${precio:,.2f}") # $1,234.50 (con separador de miles)
```

## Ejercicios Propuestos

### Ejercicio 1: Ficha Personal
Crea un programa que pida:
- Nombre completo
- Edad
- Ciudad
- Profesión

Luego muestra un resumen formateado con bordes y títulos.

### Ejercicio 2: Conversor de Temperaturas
Pide una temperatura en Celsius y conviértela a Fahrenheit.
```python
# Fórmula: F = C * 9/5 + 32
```
Muestra el resultado con 2 decimales.

### Ejercicio 3: Calculadora de Propina
Pide:
- Monto de la cuenta
- Porcentaje de propina

Calcula y muestra:
- Propina a pagar
- Total con propina

### Ejercicio 4: Información Formateada
Crea una tabla que muestre:
```
ESTUDIANTE          EDAD    PROMEDIO
----------------------------------------
Juan Pérez           20       8.50
María García         22       9.25
Pedro López          21       7.80
```

### Ejercicio 5: Recibo de Compra
Pide al usuario:
- Nombre del producto
- Precio unitario
- Cantidad

Muestra un recibo formateado con:
- Detalle de compra
- Subtotal
- IVA (16%)
- Total

### Ejercicio 6: Input con Validación
Crea un programa que:
1. Pida un número
2. Verifique que sea válido (usando `try-except`)
3. Si es válido, muestra su cuadrado
4. Si no, muestra un mensaje de error

## Trucos y Mejores Prácticas

### 1. Input con Valor por Defecto
```python
nombre = input("Nombre [Usuario]: ") or "Usuario"
# Si el usuario solo presiona Enter, usa "Usuario"
```

### 2. Limpiar Espacios
```python
nombre = input("Nombre: ").strip()  # Elimina espacios al inicio/final
```

### 3. Múltiples Prints en una Línea
```python
print("Procesando", end=" ")
print("datos", end=" ")
print("ahora")
# Salida: Procesando datos ahora
```

### 4. Print con Archivos
```python
with open("salida.txt", "w") as archivo:
    print("Este texto va al archivo", file=archivo)
```

### 5. Pretty Printing
```python
import pprint
datos = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
pprint.pprint(datos)  # Muestra más legible
```

## Errores Comunes

### ❌ Error 1: Olvidar Convertir input()
```python
# INCORRECTO
edad = input("Edad: ")
if edad > 18:  # Error: comparar string con número
    print("Mayor de edad")

# CORRECTO
edad = int(input("Edad: "))
if edad > 18:
    print("Mayor de edad")
```

### ❌ Error 2: Concatenar String con Número
```python
# INCORRECTO
edad = 25
print("Tengo " + edad + " años")  # Error

# CORRECTO
print("Tengo " + str(edad) + " años")
# O mejor con f-string
print(f"Tengo {edad} años")
```

## Recursos Adicionales
- [Documentación - print()](https://docs.python.org/3/library/functions.html#print)
- [Documentación - input()](https://docs.python.org/3/library/functions.html#input)
- [Python String Formatting](https://realpython.com/python-string-formatting/)
- [f-strings Guide](https://realpython.com/python-f-strings/)

## Notas Importantes
- Siempre usa f-strings para formateo moderno (Python 3.6+)
- `input()` retorna string - convierte al tipo necesario
- Valida las entradas del usuario para evitar errores
- Usa `end=""` para print sin salto de línea
- Formatea números con `:.2f` para decimales
