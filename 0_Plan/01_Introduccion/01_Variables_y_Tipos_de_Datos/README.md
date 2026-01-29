# Variables y Tipos de Datos

## Objetivos de Aprendizaje
- Comprender qué son las variables y cómo se utilizan
- Conocer los tipos de datos básicos en Python
- Aprender a declarar y asignar variables
- Entender la tipificación dinámica de Python

## Conceptos Teóricos

### ¿Qué es una Variable?
Una variable es un contenedor que almacena datos en la memoria. En Python, no necesitas declarar el tipo de dato explícitamente.

### Tipos de Datos Básicos

#### 1. Números
- **int**: Números enteros
  ```python
  edad = 25
  año = 2024
  ```

- **float**: Números decimales
  ```python
  altura = 1.75
  precio = 99.99
  ```

- **complex**: Números complejos
  ```python
  numero_complejo = 3 + 4j
  ```

#### 2. Texto
- **str**: Cadenas de texto
  ```python
  nombre = "Juan"
  mensaje = 'Hola Mundo'
  texto_largo = """Esto es un
  texto de múltiples líneas"""
  ```

#### 3. Booleanos
- **bool**: Verdadero o Falso
  ```python
  es_mayor_edad = True
  tiene_descuento = False
  ```

#### 4. None
- Representa la ausencia de valor
  ```python
  resultado = None
  ```

### Reglas para Nombrar Variables

✅ **Permitido:**
- Comenzar con letra o guión bajo: `nombre`, `_privado`
- Usar letras, números y guiones bajos: `variable_1`, `miVariable2`
- Sensible a mayúsculas: `Nombre` ≠ `nombre`

❌ **No Permitido:**
- Comenzar con número: `1variable`
- Usar palabras reservadas: `for`, `if`, `class`
- Usar caracteres especiales: `mi-variable`, `mi variable`

### Convenciones de Nomenclatura (PEP 8)
- **snake_case**: Para variables y funciones
  ```python
  nombre_completo = "Juan Pérez"
  edad_usuario = 30
  ```

- **UPPER_CASE**: Para constantes
  ```python
  PI = 3.14159
  MAX_INTENTOS = 3
  ```

### Verificar Tipo de Dato
```python
type(variable)  # Devuelve el tipo de dato
isinstance(variable, tipo)  # Verifica si es de un tipo específico
```

## Ejemplos Prácticos

### Ejemplo 1: Declaración de Variables
```python
# Números
edad = 25
altura = 1.75
temperatura = -10

# Texto
nombre = "María"
apellido = "García"

# Booleanos
es_estudiante = True
tiene_descuento = False

# Imprimir valores
print(f"Nombre: {nombre} {apellido}")
print(f"Edad: {edad}")
print(f"Altura: {altura}m")
print(f"Es estudiante: {es_estudiante}")
```

### Ejemplo 2: Verificar Tipos
```python
numero = 42
texto = "Python"
decimal = 3.14

print(type(numero))   # <class 'int'>
print(type(texto))    # <class 'str'>
print(type(decimal))  # <class 'float'>
```

### Ejemplo 3: Conversión de Tipos (Casting)
```python
# String a número
edad_texto = "25"
edad_numero = int(edad_texto)

# Número a string
precio = 99.99
precio_texto = str(precio)

# Float a int (pierde decimales)
altura = 1.75
altura_entera = int(altura)  # 1

print(f"Edad: {edad_numero} (tipo: {type(edad_numero)})")
print(f"Precio: {precio_texto} (tipo: {type(precio_texto)})")
print(f"Altura entera: {altura_entera}")
```

### Ejemplo 4: Asignación Múltiple
```python
# Asignar múltiples variables en una línea
x, y, z = 1, 2, 3

# Asignar el mismo valor a múltiples variables
a = b = c = 0

# Intercambiar valores
x, y = y, x
```

## Ejercicios Propuestos

### Ejercicio 1: Variables Básicas
Crea variables para almacenar:
- Tu nombre (string)
- Tu edad (int)
- Tu altura en metros (float)
- Si eres estudiante (bool)

Imprime todos los valores con mensajes descriptivos.

### Ejercicio 2: Calculadora de IMC
Crea variables para peso (kg) y altura (m), luego calcula el IMC.
```python
# IMC = peso / (altura ** 2)
```

### Ejercicio 3: Conversión de Tipos
Pide al usuario su edad como texto, conviértela a número, suma 10 años y muestra el resultado.

### Ejercicio 4: Variables Múltiples
Crea un programa que almacene información de un producto:
- Nombre del producto
- Precio
- Cantidad en stock
- Está disponible (bool)

Imprime un resumen formateado.

## Recursos Adicionales
- [Documentación oficial - Variables](https://docs.python.org/3/tutorial/introduction.html)
- [PEP 8 - Style Guide](https://pep8.org/)
- [Real Python - Variables](https://realpython.com/python-variables/)

## Notas Importantes
- Python usa tipificación dinámica: el tipo se asigna automáticamente
- Las variables se pueden reasignar con diferentes tipos
- Usa nombres descriptivos para tus variables
- Sigue las convenciones PEP 8 para código limpio
