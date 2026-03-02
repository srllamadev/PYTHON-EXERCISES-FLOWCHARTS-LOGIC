# Comentarios y Documentación

## Objetivos de Aprendizaje
- Comprender la importancia de los comentarios en el código
- Aprender los diferentes tipos de comentarios en Python
- Conocer las convenciones de documentación (docstrings)
- Aplicar buenas prácticas de documentación

## Conceptos Teóricos

### ¿Por qué son importantes los comentarios?

✅ **Beneficios:**
- Explican el propósito del código
- Facilitan el mantenimiento
- Ayudan a otros desarrolladores (y a ti mismo en el futuro)
- Documentan decisiones técnicas
- Marcan áreas pendientes (TODO)

❌ **Malas prácticas:**
- Comentarios obvios que repiten lo que el código ya dice
- Comentarios desactualizados o incorrectos
- Código comentado que debería eliminarse
- Demasiados comentarios innecesarios

## Tipos de Comentarios en Python

### 1. Comentarios de Una Línea

Se usan con el símbolo `#`

```python
# Esto es un comentario de una línea
nombre = "Juan"  # También puede ir al final de una línea

# Calcular el área del círculo
radio = 5
area = 3.14159 * radio ** 2
```

### 2. Comentarios de Múltiples Líneas

Python no tiene sintaxis especial para comentarios multilínea, pero se usan:

**Opción 1: Múltiples # (Recomendado)**
```python
# Este es un comentario
# que abarca varias líneas
# y explica algo complejo
resultado = calcular_algo()
```

**Opción 2: String Multilínea (No Recomendado como comentario)**
```python
"""
Este técnicamente no es un comentario,
es un string sin asignar.
Usa solo para docstrings.
"""
```

### 3. Docstrings (Strings de Documentación)

Son cadenas de documentación que describen módulos, clases, funciones y métodos.

#### Sintaxis
```python
def funcion():
    """Este es un docstring."""
    pass
```

#### Estilos de Docstrings

**Estilo de Una Línea:**
```python
def saludar(nombre):
    """Retorna un saludo personalizado."""
    return f"Hola {nombre}"
```

**Estilo Multilínea:**
```python
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El área del rectángulo
    
    Raises:
        ValueError: Si base o altura son negativos
    """
    if base < 0 or altura < 0:
        raise ValueError("Dimensiones no pueden ser negativas")
    return base * altura
```

## Convenciones de Documentación

### PEP 257 - Docstring Conventions

#### 1. Docstring de Módulo
```python
"""
Módulo de utilidades matemáticas.

Este módulo proporciona funciones para cálculos
geométricos básicos.

Autor: Juan Pérez
Fecha: 2024-01-15
"""

import math

def area_circulo(radio):
    """Calcula el área de un círculo."""
    return math.pi * radio ** 2
```

#### 2. Docstring de Clase
```python
class Persona:
    """
    Representa a una persona con nombre y edad.
    
    Attributes:
        nombre (str): El nombre de la persona
        edad (int): La edad de la persona
    
    Methods:
        saludar(): Retorna un saludo personalizado
        es_mayor_edad(): Verifica si es mayor de 18 años
    """
    
    def __init__(self, nombre, edad):
        """
        Inicializa una nueva instancia de Persona.
        
        Args:
            nombre (str): El nombre de la persona
            edad (int): La edad de la persona
        """
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        """Retorna un saludo con el nombre de la persona."""
        return f"Hola, soy {self.nombre}"
```

#### 3. Docstring de Función
```python
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Lista de números (int o float)
    
    Returns:
        float: El promedio de los números
    
    Raises:
        ValueError: Si la lista está vacía
        TypeError: Si la lista contiene elementos no numéricos
    
    Example:
        >>> calcular_promedio([1, 2, 3, 4, 5])
        3.0
        >>> calcular_promedio([10, 20])
        15.0
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    try:
        return sum(numeros) / len(numeros)
    except TypeError:
        raise TypeError("Todos los elementos deben ser números")
```

## Estilos de Docstrings Populares

### 1. Google Style
```python
def funcion(arg1, arg2):
    """
    Resumen breve de la función.
    
    Descripción más detallada si es necesaria.
    
    Args:
        arg1 (int): Descripción del primer argumento
        arg2 (str): Descripción del segundo argumento
    
    Returns:
        bool: Descripción del valor de retorno
    
    Raises:
        ValueError: Cuándo se lanza esta excepción
    """
    pass
```

### 2. NumPy Style
```python
def funcion(arg1, arg2):
    """
    Resumen breve de la función.
    
    Descripción más detallada si es necesaria.
    
    Parameters
    ----------
    arg1 : int
        Descripción del primer argumento
    arg2 : str
        Descripción del segundo argumento
    
    Returns
    -------
    bool
        Descripción del valor de retorno
    
    Raises
    ------
    ValueError
        Cuándo se lanza esta excepción
    """
    pass
```

### 3. Sphinx/reStructuredText Style
```python
def funcion(arg1, arg2):
    """
    Resumen breve de la función.
    
    Descripción más detallada si es necesaria.
    
    :param arg1: Descripción del primer argumento
    :type arg1: int
    :param arg2: Descripción del segundo argumento
    :type arg2: str
    :return: Descripción del valor de retorno
    :rtype: bool
    :raises ValueError: Cuándo se lanza esta excepción
    """
    pass
```

## Tipos de Comentarios Especiales

### 1. TODO Comments
```python
# TODO: Implementar validación de email
# TODO: Optimizar este bucle
# TODO: Agregar manejo de errores

def validar_usuario(email):
    # TODO: Implementar validación completa
    return True
```

### 2. FIXME Comments
```python
# FIXME: Este cálculo da resultados incorrectos para números negativos
def calcular(x):
    return x * 2  # FIXME: Bug conocido
```

### 3. HACK/XXX Comments
```python
# HACK: Solución temporal hasta refactorizar
# XXX: Esta parte del código necesita revisión
```

### 4. NOTE Comments
```python
# NOTE: Este algoritmo asume que la lista está ordenada
# NOTE: Requiere Python 3.8 o superior
```

## Ejemplos Prácticos

### Ejemplo 1: Código Bien Documentado
```python
"""
Módulo de gestión de estudiantes.

Proporciona funcionalidades para crear, actualizar y
gestionar información de estudiantes.
"""

class Estudiante:
    """
    Representa a un estudiante con sus datos académicos.
    
    Attributes:
        nombre (str): Nombre completo del estudiante
        edad (int): Edad del estudiante
        calificaciones (list): Lista de calificaciones
    """
    
    def __init__(self, nombre, edad):
        """
        Inicializa un nuevo estudiante.
        
        Args:
            nombre (str): Nombre completo del estudiante
            edad (int): Edad del estudiante (debe ser > 0)
        
        Raises:
            ValueError: Si la edad es menor o igual a 0
        """
        if edad <= 0:
            raise ValueError("La edad debe ser mayor a 0")
        
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []
    
    def agregar_calificacion(self, calificacion):
        """
        Agrega una calificación al registro del estudiante.
        
        Args:
            calificacion (float): Calificación entre 0 y 10
        
        Raises:
            ValueError: Si la calificación está fuera del rango [0, 10]
        """
        if not 0 <= calificacion <= 10:
            raise ValueError("Calificación debe estar entre 0 y 10")
        
        self.calificaciones.append(calificacion)
    
    def calcular_promedio(self):
        """
        Calcula el promedio de las calificaciones.
        
        Returns:
            float: Promedio de calificaciones, o 0 si no hay calificaciones
        """
        if not self.calificaciones:
            return 0
        
        return sum(self.calificaciones) / len(self.calificaciones)
```

### Ejemplo 2: Comentarios en Algoritmos Complejos
```python
def quicksort(arr):
    """
    Implementa el algoritmo QuickSort.
    
    QuickSort es un algoritmo de ordenamiento eficiente que usa
    el paradigma divide y conquista.
    
    Args:
        arr (list): Lista de elementos comparables
    
    Returns:
        list: Lista ordenada en orden ascendente
    
    Time Complexity: O(n log n) en promedio, O(n²) en el peor caso
    Space Complexity: O(log n)
    """
    # Caso base: lista vacía o de un elemento ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Elegir pivote (elemento del medio)
    pivote = arr[len(arr) // 2]
    
    # Dividir en tres sublistas:
    # - Elementos menores que el pivote
    # - Elementos iguales al pivote
    # - Elementos mayores que el pivote
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    # Aplicar recursivamente y combinar resultados
    return quicksort(menores) + iguales + quicksort(mayores)
```

### Ejemplo 3: Documentación de Constantes
```python
# Configuración de la aplicación
MAX_INTENTOS = 3  # Número máximo de intentos de login
TIMEOUT = 30      # Tiempo de espera en segundos
API_VERSION = "2.0"  # Versión de la API utilizada

# Códigos de error
ERROR_USUARIO_NO_ENCONTRADO = 404
ERROR_CREDENCIALES_INVALIDAS = 401
ERROR_SERVIDOR = 500
```

## Herramientas para Documentación

### 1. help() y __doc__
```python
def saludar(nombre):
    """Retorna un saludo personalizado."""
    return f"Hola {nombre}"

# Ver documentación
print(saludar.__doc__)  # Retorna un saludo personalizado
help(saludar)  # Muestra información detallada
```

### 2. Sphinx
Generador de documentación automática desde docstrings.

### 3. pydoc
```bash
# Generar documentación HTML
python -m pydoc -w modulo

# Ver documentación en el navegador
python -m pydoc -b
```

## Ejercicios Propuestos

### Ejercicio 1: Documentar Función
Crea una función que calcule el factorial de un número y documéntala completamente con:
- Docstring descriptivo
- Parámetros
- Valor de retorno
- Ejemplos de uso
- Posibles excepciones

### Ejercicio 2: Clase Documentada
Crea una clase `CuentaBancaria` con métodos para depositar, retirar y consultar saldo. Documenta:
- La clase
- El constructor
- Cada método
- Los atributos

### Ejercicio 3: Módulo Completo
Crea un módulo de utilidades matemáticas con:
- Docstring del módulo
- 3-4 funciones documentadas
- Constantes documentadas
- Ejemplos de uso en los docstrings

### Ejercicio 4: Mejorar Código Legacy
Toma este código sin documentar y agrega comentarios y docstrings apropiados:
```python
def p(l):
    if len(l) == 0:
        return False
    for i in range(2, int(l ** 0.5) + 1):
        if l % i == 0:
            return False
    return True
```

### Ejercicio 5: Code Review
Analiza este código y mejora sus comentarios:
```python
# suma
def s(a, b):
    return a + b  # suma a y b

# imprime el resultado de la suma de 5 y 3
print(s(5, 3))
```

## Buenas Prácticas

### ✅ DO (Hacer)
- Escribe docstrings para todas las funciones públicas
- Usa comentarios para explicar el "por qué", no el "qué"
- Mantén los comentarios actualizados con el código
- Usa nombres de variables descriptivos (reduce necesidad de comentarios)
- Documenta decisiones no obvias

### ❌ DON'T (No Hacer)
- No comentes código obvio
- No dejes código comentado (usa control de versiones)
- No escribas comentarios innecesarios
- No uses comentarios para compensar mal código
- No documentes en exceso

### Ejemplo de Código Auto-Explicativo
```python
# ❌ MAL: Comentarios innecesarios
# Sumar precio e impuesto
t = p + (p * 0.16)  # multiplicar precio por 0.16 y sumar

# ✅ BIEN: Código auto-explicativo
IVA = 0.16
total = precio + (precio * IVA)

# O mejor aún
def calcular_total_con_iva(precio):
    """Calcula el total incluyendo IVA del 16%."""
    IVA = 0.16
    return precio * (1 + IVA)
```

## Recursos Adicionales
- [PEP 257 - Docstring Conventions](https://pep257.readthedocs.io/)
- [PEP 8 - Comments](https://pep8.org/#comments)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Real Python - Documenting Python Code](https://realpython.com/documenting-python-code/)

## Notas Importantes
- Los docstrings son accesibles en tiempo de ejecución vía `__doc__`
- Usa triple comillas dobles `"""` para docstrings
- Los comentarios son para desarrolladores, los docstrings para usuarios
- Un buen código necesita pocos comentarios
- La documentación es parte del código, no opcional
