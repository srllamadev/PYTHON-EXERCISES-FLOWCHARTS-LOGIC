"""
Ejemplos de Return Values (Valores de Retorno)
===============================================

Muestra cómo retornar valores simples, múltiples valores
y el uso práctico de return en diferentes contextos.
"""

# ============================================
# 1. RETURN BÁSICO
# ============================================
print("=" * 50)
print("1. RETURN BÁSICO")
print("=" * 50)

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

x, y = 10, 4
print(f"{x} + {y} = {sumar(x, y)}")
print(f"{x} - {y} = {restar(x, y)}")
print(f"{x} * {y} = {multiplicar(x, y)}")
print(f"{x} / {y} = {dividir(x, y)}")

# ============================================
# 2. FUNCIONES SIN RETURN -> None
# ============================================
print("\n" + "=" * 50)
print("2. FUNCIONES SIN RETURN -> None")
print("=" * 50)

def imprimir_mensaje(msg):
    print(msg)   # Solo imprime, no retorna

resultado = imprimir_mensaje("Mensaje de prueba")
print(f"Valor retornado: {resultado}")   # None

# ============================================
# 3. RETORNO DE MÚLTIPLES VALORES
# ============================================
print("\n" + "=" * 50)
print("3. RETORNO MÚLTIPLE (TUPLAS)")
print("=" * 50)

def estadisticas(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)
    return minimo, maximo, promedio   # retorna tupla

datos = [4, 8, 15, 16, 23, 42]
mn, mx, prom = estadisticas(datos)
print(f"Lista:    {datos}")
print(f"Mínimo:   {mn}")
print(f"Máximo:   {mx}")
print(f"Promedio: {prom:.2f}")

# También como tupla sin desempacar
resultado_tuple = estadisticas(datos)
print(f"Como tupla: {resultado_tuple}")

# ============================================
# 4. EARLY RETURN (RETORNO TEMPRANO)
# ============================================
print("\n" + "=" * 50)
print("4. EARLY RETURN - VALIDACIONES")
print("=" * 50)

def dividir_seguro(a, b):
    if b == 0:
        return None   # Retorna temprano
    return a / b

print(dividir_seguro(10, 2))   # 5.0
print(dividir_seguro(10, 0))   # None

def es_mayor_de_edad(edad):
    if not isinstance(edad, int):
        return "Error: la edad debe ser un entero"
    if edad < 0:
        return "Error: la edad no puede ser negativa"
    return edad >= 18

print(es_mayor_de_edad(20))    # True
print(es_mayor_de_edad(15))    # False
print(es_mayor_de_edad(-5))    # Error
print(es_mayor_de_edad("abc")) # Error

# ============================================
# 5. USAR EL RETORNO EN EXPRESIONES
# ============================================
print("\n" + "=" * 50)
print("5. USAR VALORES RETORNADOS")
print("=" * 50)

def cuadrado(n):
    return n ** 2

def hipotenusa(a, b):
    return (cuadrado(a) + cuadrado(b)) ** 0.5

# Anidado como argumento
print(f"Hipotenusa de 3,4: {hipotenusa(3, 4)}")
print(f"Cuadrado de 5 + Cuadrado de 3 = {cuadrado(5) + cuadrado(3)}")
print(f"Mayor cuadrado: {max(cuadrado(3), cuadrado(7), cuadrado(5))}")

# ============================================
# 6. RETORNAR DIFERENTES TIPOS
# ============================================
print("\n" + "=" * 50)
print("6. RETORNAR DIFERENTES TIPOS")
print("=" * 50)

def clasificar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

def factores(n):
    """Retorna una lista con los factores de n."""
    return [i for i in range(1, n + 1) if n % i == 0]

def info_numero(n):
    """Retorna un diccionario con información del número."""
    return {
        "valor": n,
        "clasificacion": clasificar_numero(n),
        "factores": factores(abs(n)) if n != 0 else [],
        "es_par": n % 2 == 0
    }

for num in [12, -5, 0]:
    info = info_numero(num)
    print(f"Número {info['valor']}: {info['clasificacion']}, "
          f"par={info['es_par']}, factores={info['factores']}")
