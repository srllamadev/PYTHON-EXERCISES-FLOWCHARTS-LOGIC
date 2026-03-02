"""
Ejemplos de Decoradores Básicos
=================================

Muestra el concepto de funciones de primera clase, closures
y la implementación de decoradores desde cero.
"""

from functools import wraps
import time

# ============================================
# 1. FUNCIONES COMO OBJETOS (PRIMERA CLASE)
# ============================================
print("=" * 50)
print("1. FUNCIONES COMO OBJETOS")
print("=" * 50)

def saludar():
    return "¡Hola!"

def despedir():
    return "¡Adiós!"

# Asignar función a variable
accion = saludar
print(accion())   # ¡Hola!

# Lista de funciones
funciones = [saludar, despedir]
for fn in funciones:
    print(fn())

# Pasar función como argumento
def ejecutar(funcion):
    print(f"Ejecutando: {funcion.__name__}")
    return funcion()

resultado = ejecutar(saludar)
print(resultado)

# ============================================
# 2. CLOSURES
# ============================================
print("\n" + "=" * 50)
print("2. CLOSURES")
print("=" * 50)

def crear_saludo(idioma):
    def saludar(nombre):
        if idioma == "es":
            return f"Hola, {nombre}!"
        elif idioma == "en":
            return f"Hello, {nombre}!"
        elif idioma == "fr":
            return f"Bonjour, {nombre}!"
    return saludar          # retorna la función interior

saludar_es = crear_saludo("es")
saludar_en = crear_saludo("en")
saludar_fr = crear_saludo("fr")

print(saludar_es("Ana"))
print(saludar_en("Carlos"))
print(saludar_fr("María"))

# ============================================
# 3. DECORADOR BÁSICO
# ============================================
print("\n" + "=" * 50)
print("3. DECORADOR BÁSICO")
print("=" * 50)

def mayusculas(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        return resultado.upper()
    return wrapper

@mayusculas
def obtener_nombre():
    return "ana pérez"

@mayusculas
def obtener_ciudad():
    return "ciudad de méxico"

print(obtener_nombre())    # ANA PÉREZ
print(obtener_ciudad())    # CIUDAD DE MÉXICO

# ============================================
# 4. DECORADOR DE TEMPORIZACIÓN
# ============================================
print("\n" + "=" * 50)
print("4. DECORADOR DE TEMPORIZACIÓN")
print("=" * 50)

def medir_tiempo(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"  '{funcion.__name__}' tardó {fin - inicio:.6f}s")
        return resultado
    return wrapper

@medir_tiempo
def sumar_hasta(n):
    return sum(range(n))

@medir_tiempo
def contar_caracteres(texto):
    return len(texto)

sumar_hasta(1_000_000)
contar_caracteres("Python es genial! " * 1000)

# ============================================
# 5. DECORADOR DE VALIDACIÓN
# ============================================
print("\n" + "=" * 50)
print("5. DECORADOR DE VALIDACIÓN")
print("=" * 50)

def solo_positivos(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                return f"Error: '{funcion.__name__}' requiere valores positivos"
        return funcion(*args, **kwargs)
    return wrapper

@solo_positivos
def raiz_cuadrada(n):
    return n ** 0.5

@solo_positivos
def logaritmo_base(n, base=10):
    import math
    return math.log(n, base)

print(raiz_cuadrada(25))    # 5.0
print(raiz_cuadrada(-4))    # Error
print(logaritmo_base(100))  # 2.0

# ============================================
# 6. DECORADOR CON PARÁMETROS
# ============================================
print("\n" + "=" * 50)
print("6. DECORADOR CON PARÁMETROS")
print("=" * 50)

def repetir(n=2):
    def decorador(funcion):
        @wraps(funcion)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcion(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def decir_hola():
    print("¡Hola!")

@repetir(2)
def advertencia(mensaje):
    print(f"⚠️  ADVERTENCIA: {mensaje}")

decir_hola()
print()
advertencia("Revisa tu código")

# ============================================
# 7. FUNCTOOLS.WRAPS - PRESERVAR METADATOS
# ============================================
print("\n" + "=" * 50)
print("7. PRESERVAR METADATOS CON wraps")
print("=" * 50)

def sin_wraps(funcion):
    def wrapper(*args, **kwargs):
        return funcion(*args, **kwargs)
    return wrapper

def con_wraps(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        return funcion(*args, **kwargs)
    return wrapper

@sin_wraps
def funcion_sin_wraps():
    """Esta es mi docstring."""
    pass

@con_wraps
def funcion_con_wraps():
    """Esta es mi docstring."""
    pass

print(f"Sin @wraps -> __name__: '{funcion_sin_wraps.__name__}'")
print(f"Con @wraps -> __name__: '{funcion_con_wraps.__name__}'")
print(f"Sin @wraps -> __doc__:  '{funcion_sin_wraps.__doc__}'")
print(f"Con @wraps -> __doc__:  '{funcion_con_wraps.__doc__}'")
