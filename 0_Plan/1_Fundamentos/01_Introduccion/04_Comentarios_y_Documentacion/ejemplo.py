"""
Ejemplos de Comentarios y Documentación en Python
=================================================

Este módulo demuestra las mejores prácticas para comentar
y documentar código Python de manera profesional.

Autor: Python Course
Fecha: 2024-01-29
Versión: 1.0
"""

# ============================================
# 1. COMENTARIOS DE UNA LÍNEA
# ============================================
print("=" * 60)
print("1. COMENTARIOS DE UNA LÍNEA")
print("=" * 60)

# Este es un comentario de una línea
x = 10  # También puede ir al final de una línea

# Calcular el área de un círculo
radio = 5
PI = 3.14159
area = PI * radio ** 2  # Fórmula: π × r²

print(f"Área del círculo: {area:.2f}")


# ============================================
# 2. COMENTARIOS MULTILÍNEA
# ============================================
print("\n" + "=" * 60)
print("2. COMENTARIOS MULTILÍNEA")
print("=" * 60)

# Este algoritmo implementa la búsqueda binaria
# que es más eficiente que la búsqueda lineal
# para listas ordenadas.
# Complejidad: O(log n)

def busqueda_binaria(lista, objetivo):
    """Implementación de búsqueda binaria."""
    inicio = 0
    fin = len(lista) - 1
    
    # Continuar mientras haya elementos por buscar
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return -1  # No encontrado


# ============================================
# 3. DOCSTRINGS - FUNCIONES
# ============================================
print("\n" + "=" * 60)
print("3. DOCSTRINGS EN FUNCIONES")
print("=" * 60)

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Lista de números (int o float)
    
    Returns:
        float: El promedio de los números
    
    Raises:
        ValueError: Si la lista está vacía
    
    Examples:
        >>> calcular_promedio([1, 2, 3, 4, 5])
        3.0
        >>> calcular_promedio([10, 20])
        15.0
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    return sum(numeros) / len(numeros)


# Usar la función
notas = [9.5, 8.7, 9.0, 8.5]
promedio = calcular_promedio(notas)
print(f"Notas: {notas}")
print(f"Promedio: {promedio:.2f}")

# Ver el docstring
print(f"\nDocstring de la función:")
print(calcular_promedio.__doc__)


# ============================================
# 4. DOCSTRINGS - CLASES
# ============================================
print("\n" + "=" * 60)
print("4. DOCSTRINGS EN CLASES")
print("=" * 60)

class Estudiante:
    """
    Representa a un estudiante con sus datos académicos.
    
    Esta clase maneja la información básica de un estudiante
    y proporciona métodos para gestionar sus calificaciones.
    
    Attributes:
        nombre (str): Nombre completo del estudiante
        matricula (str): Número de matrícula
        calificaciones (list): Lista de calificaciones
    
    Methods:
        agregar_calificacion(calificacion): Agrega una nueva calificación
        calcular_promedio(): Calcula el promedio de calificaciones
    """
    
    def __init__(self, nombre, matricula):
        """
        Inicializa un nuevo estudiante.
        
        Args:
            nombre (str): Nombre completo del estudiante
            matricula (str): Número de matrícula único
        """
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = []
    
    def agregar_calificacion(self, calificacion):
        """
        Agrega una calificación al registro del estudiante.
        
        Args:
            calificacion (float): Calificación entre 0 y 10
        
        Raises:
            ValueError: Si la calificación está fuera del rango válido
        """
        if not 0 <= calificacion <= 10:
            raise ValueError("La calificación debe estar entre 0 y 10")
        
        self.calificaciones.append(calificacion)
    
    def calcular_promedio(self):
        """
        Calcula el promedio de todas las calificaciones.
        
        Returns:
            float: Promedio de calificaciones, o 0 si no hay calificaciones
        """
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)


# Usar la clase
estudiante = Estudiante("Juan Pérez", "2024-001")
estudiante.agregar_calificacion(9.5)
estudiante.agregar_calificacion(8.7)
estudiante.agregar_calificacion(9.0)

print(f"Estudiante: {estudiante.nombre}")
print(f"Matrícula: {estudiante.matricula}")
print(f"Promedio: {estudiante.calcular_promedio():.2f}")

# Ver docstring de la clase
print(f"\nDocstring de la clase:")
print(Estudiante.__doc__)


# ============================================
# 5. COMENTARIOS ESPECIALES (TODO, FIXME, etc.)
# ============================================
print("\n" + "=" * 60)
print("5. COMENTARIOS ESPECIALES")
print("=" * 60)

def procesar_datos(datos):
    """Procesa una lista de datos."""
    
    # TODO: Implementar validación de datos
    # TODO: Agregar logging
    
    # FIXME: Este bucle es ineficiente para listas grandes
    resultado = []
    for item in datos:
        resultado.append(item * 2)
    
    # HACK: Solución temporal hasta refactorizar
    resultado = [x for x in resultado if x > 0]
    
    # NOTE: Este método será deprecado en la versión 2.0
    return resultado


# ============================================
# 6. CÓDIGO BIEN DOCUMENTADO VS MAL DOCUMENTADO
# ============================================
print("\n" + "=" * 60)
print("6. BUENAS VS MALAS PRÁCTICAS")
print("=" * 60)

# ❌ MAL: Comentarios obvios
# i = i + 1  # incrementar i en 1
# print(x)   # imprimir x

# ✅ BIEN: Código auto-explicativo
contador_intentos = 0
contador_intentos += 1
print(contador_intentos)

# ❌ MAL: Comentario desactualizado
# Calcula el descuento del 10%
descuento = precio * 0.20  # Ahora es 20% pero el comentario no se actualizó

# ✅ BIEN: Usar constantes descriptivas
PORCENTAJE_DESCUENTO = 0.20
descuento_correcto = 1000 * PORCENTAJE_DESCUENTO


# ============================================
# 7. EJEMPLO: FUNCIÓN BIEN DOCUMENTADA
# ============================================
print("\n" + "=" * 60)
print("7. EJEMPLO DE FUNCIÓN BIEN DOCUMENTADA")
print("=" * 60)

def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    
    El factorial de n (escrito como n!) es el producto de todos
    los enteros positivos menores o iguales a n.
    Por definición, 0! = 1.
    
    Args:
        n (int): Número entero no negativo
    
    Returns:
        int: El factorial de n
    
    Raises:
        ValueError: Si n es negativo
        TypeError: Si n no es un entero
    
    Examples:
        >>> calcular_factorial(0)
        1
        >>> calcular_factorial(5)
        120
        >>> calcular_factorial(10)
        3628800
    
    Notes:
        Para números grandes, considere usar math.factorial()
        que está optimizado.
    
    See Also:
        math.factorial: Implementación optimizada de la biblioteca estándar
    """
    # Validar tipo de dato
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    
    # Validar que no sea negativo
    if n < 0:
        raise ValueError("n debe ser no negativo")
    
    # Caso base: 0! = 1
    if n == 0:
        return 1
    
    # Calcular factorial iterativamente
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado


# Probar la función
print(f"5! = {calcular_factorial(5)}")
print(f"10! = {calcular_factorial(10):,}")


# ============================================
# 8. EJEMPLO: ALGORITMO COMPLEJO DOCUMENTADO
# ============================================
print("\n" + "=" * 60)
print("8. ALGORITMO COMPLEJO DOCUMENTADO")
print("=" * 60)

def quicksort(arr):
    """
    Implementa el algoritmo QuickSort para ordenar una lista.
    
    QuickSort es un algoritmo de ordenamiento eficiente que utiliza
    el paradigma divide y conquista. Divide la lista en sublistas
    usando un pivote y las ordena recursivamente.
    
    Args:
        arr (list): Lista de elementos comparables
    
    Returns:
        list: Nueva lista ordenada en orden ascendente
    
    Time Complexity:
        - Mejor caso: O(n log n)
        - Caso promedio: O(n log n)
        - Peor caso: O(n²) - cuando la lista ya está ordenada
    
    Space Complexity:
        O(log n) - por la pila de recursión
    
    Examples:
        >>> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
        >>> quicksort([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
    """
    # Caso base: lista vacía o de un elemento ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Elegir pivote (elemento del medio para mejor rendimiento promedio)
    pivote = arr[len(arr) // 2]
    
    # Dividir en tres sublistas:
    # - menores: elementos menores que el pivote
    # - iguales: elementos iguales al pivote
    # - mayores: elementos mayores que el pivote
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    # Aplicar recursivamente quicksort a las sublistas
    # y combinar los resultados
    return quicksort(menores) + iguales + quicksort(mayores)


# Probar el algoritmo
lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = quicksort(lista_desordenada)

print(f"Original:  {lista_desordenada}")
print(f"Ordenada:  {lista_ordenada}")


# ============================================
# 9. DOCUMENTACIÓN DE CONSTANTES
# ============================================
print("\n" + "=" * 60)
print("9. DOCUMENTACIÓN DE CONSTANTES")
print("=" * 60)

# Configuración de la aplicación
MAX_INTENTOS = 3           # Número máximo de intentos de login
TIMEOUT_SEGUNDOS = 30      # Tiempo de espera para operaciones
API_VERSION = "2.0"        # Versión de la API utilizada
DEBUG_MODE = True          # Activar modo de depuración

# Constantes físicas
VELOCIDAD_LUZ = 299792458  # Velocidad de la luz en m/s
GRAVEDAD_TIERRA = 9.81     # Aceleración de la gravedad en m/s²
PI = 3.14159265359         # Constante pi

# Códigos de error
ERROR_NO_ENCONTRADO = 404     # Recurso no encontrado
ERROR_NO_AUTORIZADO = 401     # Credenciales inválidas
ERROR_SERVIDOR = 500          # Error interno del servidor

print(f"API Version: {API_VERSION}")
print(f"Máximo de intentos: {MAX_INTENTOS}")
print(f"Velocidad de la luz: {VELOCIDAD_LUZ:,} m/s")


# ============================================
# 10. USO DE help()
# ============================================
print("\n" + "=" * 60)
print("10. FUNCIÓN help()")
print("=" * 60)

print("Puedes usar help() para ver la documentación:")
print("Ejemplo: help(calcular_factorial)")
print("\nDocstring accesible vía __doc__:")
print(calcular_factorial.__doc__)


print("\n" + "=" * 60)
print("FIN DE LOS EJEMPLOS")
print("=" * 60)
