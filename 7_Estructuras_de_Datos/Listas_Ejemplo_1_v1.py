"""
LISTAS EN PYTHON
Las listas son estructuras de datos que almacenan elementos ordenados de cualquier tipo.
Son mutables (modificables) y se definen con corchetes [].
"""

# =============================================
# 1. CREACIÓN DE LISTAS
# =============================================
# Crear una lista vacía
lista_vacia = []

# Crear lista con elementos iniciales
frutas = ["manzana", "banana", "cereza"]
numeros = [10, 20, 30, 40]
mixta = [1, "hola", 3.14, True]

print("Lista de frutas:", frutas)

# =============================================
# 2. ACCESO A ELEMENTOS
# =============================================
# Indexación positiva (0-based)
primer_fruta = frutas[0]        # 'manzana'
ultima_fruta = frutas[-1]       # 'cereza' (indexación negativa)

print("\nPrimera fruta:", primer_fruta)
print("Última fruta:", ultima_fruta)

# Slicing (sub-listas)
dos_primeras = frutas[0:2]      # ['manzana', 'banana']
ultimas_dos = frutas[-2:]        # ['banana', 'cereza']

print("Dos primeras:", dos_primeras)
print("Últimas dos:", ultimas_dos)

# =============================================
# 3. MODIFICACIÓN DE LISTAS
# =============================================
# Cambiar un elemento
frutas[1] = "kiwi"
print("\nLista modificada:", frutas)  # ['manzana', 'kiwi', 'cereza']

# Agregar elementos
frutas.append("naranja")        # Añade al final
frutas.insert(1, "mango")       # Inserta en posición específica
print("Después de agregar:", frutas)

# =============================================
# 4. OPERACIONES COMUNES
# =============================================
# Longitud de la lista
print("\nCantidad de frutas:", len(frutas))

# Eliminar elementos
eliminado = frutas.pop(2)       # Elimina por índice
frutas.remove("cereza")         # Elimina por valor

print("Fruta eliminada:", eliminado)
print("Lista después de eliminar:", frutas)

# Ordenamiento
numeros.sort(reverse=True)      # Orden descendente
print("\nNúmeros ordenados:", numeros)

# Búsqueda
if "manzana" in frutas:
    print("Manzana está en la lista")

# =============================================
# 5. ITERACIÓN
# =============================================
print("\nRecorrido con for:")
for fruta in frutas:
    print(fruta.capitalize())  # Imprime cada fruta capitalizada

# Comprensión de listas (list comprehension)
cuadrados = [x**2 for x in range(1, 5)]
print("\nCuadrados:", cuadrados)  # [1, 4, 9, 16]