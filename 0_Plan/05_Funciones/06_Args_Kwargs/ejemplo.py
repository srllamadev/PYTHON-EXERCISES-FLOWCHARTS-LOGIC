"""
Ejemplos de *args y **kwargs
==============================

Muestra cómo usar argumentos variables en funciones Python.
"""

# ============================================
# 1. *args BÁSICO
# ============================================
print("=" * 50)
print("1. *args - ARGUMENTOS POSICIONALES VARIABLES")
print("=" * 50)

def sumar(*args):
    """Suma cualquier cantidad de números."""
    print(f"  args recibidos: {args}  (tipo: {type(args)})")
    return sum(args)

print(sumar())            # 0
print(sumar(5))           # 5
print(sumar(1, 2, 3))     # 6
print(sumar(10, 20, 30, 40, 50))  # 150

# ============================================
# 2. **kwargs BÁSICO
# ============================================
print("\n" + "=" * 50)
print("2. **kwargs - ARGUMENTOS KEYWORD VARIABLES")
print("=" * 50)

def mostrar_perfil(**kwargs):
    """Muestra la información recibida como pares clave-valor."""
    print(f"  kwargs recibidos: {kwargs}  (tipo: {type(kwargs)})")
    for clave, valor in kwargs.items():
        print(f"  {clave.capitalize()}: {valor}")
    print()

mostrar_perfil(nombre="Ana", edad=28)
mostrar_perfil(nombre="Carlos", ciudad="Madrid", profesion="Ing.", activo=True)

# ============================================
# 3. COMBINANDO args Y kwargs
# ============================================
print("=" * 50)
print("3. COMBINANDO *args Y **kwargs")
print("=" * 50)

def log(nivel, *mensajes, **contexto):
    print(f"[{nivel.upper()}]", end=" ")
    print(" | ".join(str(m) for m in mensajes))
    if contexto:
        for k, v in contexto.items():
            print(f"  {k}={v}")

log("info", "Servidor iniciado")
log("warning", "Memoria alta", "CPU alta", host="server01", uso=87)
log("error", "Conexión perdida", codigo=503, ip="192.168.1.1")

# ============================================
# 4. PARÁMETROS REGULARES + *args + **kwargs
# ============================================
print("\n" + "=" * 50)
print("4. PARÁMETROS REGULARES + *args + **kwargs")
print("=" * 50)

def crear_etiqueta(nombre, *clases, **atributos):
    """Simula la creación de una etiqueta HTML."""
    clases_str = " ".join(clases)
    attrs_str = " ".join(f'{k}="{v}"' for k, v in atributos.items())
    print(f"<{nombre} class='{clases_str}' {attrs_str}></{nombre}>")

crear_etiqueta("div", "container", "main", id="app", style="color:red")
crear_etiqueta("button", "btn", "primary", type="submit")
crear_etiqueta("p", id="texto")

# ============================================
# 5. DESEMPAQUETADO CON * Y **
# ============================================
print("\n" + "=" * 50)
print("5. DESEMPAQUETADO CON * Y **")
print("=" * 50)

def punto(x, y, z):
    print(f"Coordenadas: ({x}, {y}, {z})")

# Desempacar lista/tupla con *
coords_lista = [1, 2, 3]
coords_tupla = (4, 5, 6)
punto(*coords_lista)
punto(*coords_tupla)

# Desempacar diccionario con **
coords_dict = {"x": 7, "y": 8, "z": 9}
punto(**coords_dict)

# ============================================
# 6. PASAR *args A OTRA FUNCIÓN
# ============================================
print("\n" + "=" * 50)
print("6. REENVIAR args Y kwargs")
print("=" * 50)

def mi_print(*args, **kwargs):
    """Envuelve print() para agregar un prefijo."""
    print("[LOG]", *args, **kwargs)

mi_print("Hola mundo")
mi_print("Valor:", 42, sep=" -> ", end="\n\n")
mi_print("A", "B", "C", sep="-")
