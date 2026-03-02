"""
Ejemplos de Scope (Alcance de Variables)
=========================================

Demuestra la diferencia entre variables locales y globales,
y cómo funciona la regla LEGB en Python.
"""

# ============================================
# 1. VARIABLE LOCAL
# ============================================
print("=" * 50)
print("1. VARIABLE LOCAL")
print("=" * 50)

def mostrar_local():
    mensaje = "Soy una variable LOCAL"   # solo existe aquí
    print(mensaje)

mostrar_local()
# print(mensaje)   # Descomenta para ver el NameError

# ============================================
# 2. VARIABLE GLOBAL
# ============================================
print("\n" + "=" * 50)
print("2. VARIABLE GLOBAL")
print("=" * 50)

PI = 3.14159   # global

def calcular_area(radio):
    # PI es accesible aquí (solo lectura)
    return PI * radio ** 2

print(f"Área con radio 5: {calcular_area(5):.4f}")
print(f"Valor de PI (global): {PI}")

# ============================================
# 3. LOCAL OCULTA A LA GLOBAL
# ============================================
print("\n" + "=" * 50)
print("3. LOCAL OCULTA A LA GLOBAL (SHADOWING)")
print("=" * 50)

nombre = "Global"

def shadowing():
    nombre = "Local"   # nueva variable local, no modifica la global
    print(f"Dentro de la función: {nombre}")

shadowing()
print(f"Fuera de la función:  {nombre}")   # sigue siendo "Global"

# ============================================
# 4. MODIFICAR GLOBAL CON `global`
# ============================================
print("\n" + "=" * 50)
print("4. USAR 'global' PARA MODIFICAR")
print("=" * 50)

contador = 0

def incrementar():
    global contador
    contador += 1
    print(f"  Contador: {contador}")

incrementar()
incrementar()
incrementar()
print(f"Valor final: {contador}")

# ============================================
# 5. ALTERNATIVA CORRECTA: USAR RETURN
# ============================================
print("\n" + "=" * 50)
print("5. ALTERNATIVA CORRECTA: RETURN")
print("=" * 50)

def incrementar_correcto(valor):
    return valor + 1   # No necesito `global`

mi_contador = 0
mi_contador = incrementar_correcto(mi_contador)
mi_contador = incrementar_correcto(mi_contador)
mi_contador = incrementar_correcto(mi_contador)
print(f"Contador con return: {mi_contador}")

# ============================================
# 6. REGLA LEGB EN PRÁCTICA
# ============================================
print("\n" + "=" * 50)
print("6. REGLA LEGB")
print("=" * 50)

x = "Global"   # G - Global

def exterior():
    x = "Enclosing"   # E - Enclosing
    def interior():
        x = "Local"   # L - Local
        print(f"Dentro de interior: {x}")
    interior()
    print(f"Dentro de exterior: {x}")

exterior()
print(f"En el módulo: {x}")

# ============================================
# 7. nonlocal
# ============================================
print("\n" + "=" * 50)
print("7. nonlocal")
print("=" * 50)

def crear_contador():
    cuenta = 0
    def incrementar():
        nonlocal cuenta   # modifica 'cuenta' de 'crear_contador'
        cuenta += 1
        return cuenta
    return incrementar

contador_fn = crear_contador()
print(contador_fn())   # 1
print(contador_fn())   # 2
print(contador_fn())   # 3
