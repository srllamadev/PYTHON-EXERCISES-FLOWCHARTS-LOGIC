"""
Ejercicios de *args y **kwargs
================================

Completa los ejercicios siguientes. Las soluciones están al final.
"""

print("=" * 60)
print("EJERCICIOS - *args y **kwargs")
print("=" * 60)

# ============================================
# EJERCICIO 1: Operaciones con *args
# ============================================
print("\nEJERCICIO 1: Operaciones con *args")
print("-" * 60)
print("Crea las siguientes funciones que usen *args:")
print("  a) 'multiplicar(*args)' -> multiplica todos los valores")
print("  b) 'promedio(*args)'    -> calcula el promedio")
print("  c) 'maximo(*args)'      -> retorna el máximo (sin usar max())")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 2: Información con **kwargs
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 2: Información con **kwargs")
print("-" * 60)
print("Crea 'tarjeta_presentacion(**kwargs)' que imprima una")
print("tarjeta formateada con cualquier información recibida.")
print("Ejemplo de llamada:")
print("  tarjeta_presentacion(nombre='Ana', cargo='Dev', empresa='Tech')")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 3: Función Mixta
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 3: Función Mixta")
print("-" * 60)
print("Crea 'resumen_pedido(cliente, *productos, **opciones)':")
print("  - cliente: nombre del cliente (str)")
print("  - *productos: nombres de productos pedidos")
print("  - **opciones: kwargs como envio='express', descuento=10")
print("Imprime un resumen del pedido.")

# TODO: Escribe tu código aquí




# ============================================
# EJERCICIO 4: Desempaquetado
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 4: Desempaquetado")
print("-" * 60)
print("Dada esta función y estos datos:")
print("  def registrar(nombre, edad, ciudad): ...")
print("  datos_tupla = ('María', 30, 'Barcelona')")
print("  datos_dict  = {'nombre': 'Luis', 'edad': 25, 'ciudad': 'Lima'}")
print("Llama a registrar() desempaquetando cada estructura de datos.")

def registrar(nombre, edad, ciudad):
    print(f"Registrado: {nombre}, {edad} años, {ciudad}")

datos_tupla = ('María', 30, 'Barcelona')
datos_dict  = {'nombre': 'Luis', 'edad': 25, 'ciudad': 'Lima'}

# TODO: Llama a registrar desempaquetando datos_tupla y datos_dict




# ============================================
# EJERCICIO 5: RETO - Merge de Diccionarios
# ============================================
print("\n" + "=" * 60)
print("EJERCICIO 5: RETO - Merge de Diccionarios")
print("-" * 60)
print("Crea 'merge(**dicts_as_kwargs)' pero recibe múltiples")
print("diccionarios como argumentos posicionales *dicts y")
print("los combina en uno solo.")
print("Ejemplo: merge({'a':1}, {'b':2}, {'c':3}) -> {'a':1,'b':2,'c':3}")

# TODO: Escribe tu código aquí




# ============================================
# SOLUCIONES
# ============================================
# def multiplicar(*args):
#     resultado = 1
#     for n in args:
#         resultado *= n
#     return resultado
#
# def promedio(*args):
#     if not args:
#         return 0
#     return sum(args) / len(args)
#
# print(multiplicar(2, 3, 4))   # 24
# print(promedio(10, 20, 30))   # 20.0
