"""
Ejemplos prácticos de Conjuntos (set) en Python
Autor: Python Course
Fecha: 2026
"""

# ============================================
# 1. CREACIÓN DE CONJUNTOS
# ============================================

print("=" * 50)
print("1. CREACIÓN DE CONJUNTOS")
print("=" * 50)

# Diferentes formas de crear conjuntos
conjunto_vacio = set()  # {} crearía un diccionario
numeros = {1, 2, 3, 4, 5}
letras = {'a', 'b', 'c', 'd'}
mixto = {1, "dos", 3.0, True, (1, 2)}

# Constructor set()
desde_lista = set([1, 2, 2, 3, 3, 4])  # Elimina duplicados automáticamente
desde_string = set("Python")
desde_rango = set(range(1, 6))

# Set comprehension
cuadrados = {x**2 for x in range(6)}
pares = {x for x in range(10) if x % 2 == 0}

print(f"Conjunto vacío: {conjunto_vacio} - Tipo: {type(conjunto_vacio)}")
print(f"Números: {numeros}")
print(f"Desde lista con duplicados: {desde_lista}")
print(f"Desde string: {desde_string}")
print(f"Cuadrados: {cuadrados}")
print(f"Pares: {pares}")

# ============================================
# 2. AGREGAR Y ELIMINAR ELEMENTOS
# ============================================

print("\n" + "=" * 50)
print("2. AGREGAR Y ELIMINAR ELEMENTOS")
print("=" * 50)

frutas = {"manzana", "banana", "cereza"}
print(f"Frutas inicial: {frutas}")

# Agregar un elemento
frutas.add("durazno")
print(f"Después de add: {frutas}")

# Agregar múltiples elementos
frutas.update(["kiwi", "uva", "pera"])
print(f"Después de update: {frutas}")

# Intentar agregar duplicado (no hace nada)
frutas.add("manzana")
print(f"Después de agregar duplicado: {frutas}")

# Eliminar con remove (error si no existe)
frutas.remove("banana")
print(f"Después de remove: {frutas}")

# Eliminar con discard (no error si no existe)
frutas.discard("kiwi")
frutas.discard("sandía")  # No existe, pero no hay error
print(f"Después de discard: {frutas}")

# Pop (elimina elemento aleatorio)
elemento = frutas.pop()
print(f"Elemento eliminado con pop: {elemento}")
print(f"Frutas después de pop: {frutas}")

# ============================================
# 3. OPERACIONES MATEMÁTICAS
# ============================================

print("\n" + "=" * 50)
print("3. OPERACIONES MATEMÁTICAS")
print("=" * 50)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")

# Unión (|) - Elementos en A o B o ambos
union = A | B
print(f"\nA | B (Unión): {union}")
print(f"A.union(B):     {A.union(B)}")

# Intersección (&) - Elementos en A y B
interseccion = A & B
print(f"\nA & B (Intersección): {interseccion}")
print(f"A.intersection(B):    {A.intersection(B)}")

# Diferencia (-) - Elementos en A pero no en B
diferencia = A - B
print(f"\nA - B (Diferencia):      {diferencia}")
print(f"A.difference(B):         {A.difference(B)}")

# Diferencia simétrica (^) - Elementos en A o B pero no en ambos
dif_simetrica = A ^ B
print(f"\nA ^ B (Dif. Simétrica):       {dif_simetrica}")
print(f"A.symmetric_difference(B):    {A.symmetric_difference(B)}")

# ============================================
# 4. SUBCONJUNTOS Y SUPERCONJUNTOS
# ============================================

print("\n" + "=" * 50)
print("4. SUBCONJUNTOS Y SUPERCONJUNTOS")
print("=" * 50)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}

print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")

# Subconjunto
print(f"\nA.issubset(B):    {A.issubset(B)}")     # True
print(f"A <= B:           {A <= B}")             # True
print(f"A < B:            {A < B}")              # True (subconjunto propio)
print(f"B.issubset(A):    {B.issubset(A)}")     # False

# Superconjunto
print(f"\nB.issuperset(A):  {B.issuperset(A)}")   # True
print(f"B >= A:           {B >= A}")             # True
print(f"B > A:            {B > A}")              # True (superconjunto propio)

# Conjuntos disjuntos (sin elementos comunes)
print(f"\nA.isdisjoint(B):  {A.isdisjoint(B)}")   # False
print(f"A.isdisjoint(C):  {A.isdisjoint(C)}")   # True

# ============================================
# 5. OPERACIONES CON ASIGNACIÓN
# ============================================

print("\n" + "=" * 50)
print("5. OPERACIONES CON ASIGNACIÓN")
print("=" * 50)

X = {1, 2, 3}
Y = {3, 4, 5}

print(f"X inicial: {X}")
print(f"Y:         {Y}")

# Unión con asignación
X_copia = X.copy()
X_copia |= Y
print(f"\nX |= Y:    {X_copia}")

# Intersección con asignación
X_copia = X.copy()
X_copia &= Y
print(f"X &= Y:    {X_copia}")

# Diferencia con asignación
X_copia = X.copy()
X_copia -= Y
print(f"X -= Y:    {X_copia}")

# Diferencia simétrica con asignación
X_copia = X.copy()
X_copia ^= Y
print(f"X ^= Y:    {X_copia}")

# ============================================
# 6. FROZENSET (INMUTABLE)
# ============================================

print("\n" + "=" * 50)
print("6. FROZENSET (CONJUNTO INMUTABLE)")
print("=" * 50)

# Crear frozenset
fs = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {fs}")
print(f"Tipo: {type(fs)}")

# No se puede modificar
# fs.add(6)  # Error: AttributeError

# Puede ser elemento de un set
conjunto_de_frozensets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}
print(f"\nConjunto de frozensets: {conjunto_de_frozensets}")

# Puede ser clave de diccionario
diccionario = {
    frozenset([1, 2]): "primero",
    frozenset([3, 4]): "segundo"
}
print(f"Dict con frozenset como clave: {diccionario}")

# ============================================
# 7. ELIMINAR DUPLICADOS
# ============================================

print("\n" + "=" * 50)
print("7. ELIMINAR DUPLICADOS")
print("=" * 50)

# Lista con duplicados
numeros_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
print(f"Lista original: {numeros_duplicados}")

# Método 1: Con set (orden no garantizado)
unicos = list(set(numeros_duplicados))
print(f"Sin duplicados (set): {unicos}")

# Método 2: Preservando orden
def eliminar_duplicados_ordenado(lista):
    visto = set()
    resultado = []
    for item in lista:
        if item not in visto:
            visto.add(item)
            resultado.append(item)
    return resultado

unicos_ordenado = eliminar_duplicados_ordenado(numeros_duplicados)
print(f"Sin duplicados (orden preservado): {unicos_ordenado}")

# ============================================
# 8. COMPRENSIÓN DE CONJUNTOS
# ============================================

print("\n" + "=" * 50)
print("8. COMPRENSIÓN DE CONJUNTOS")
print("=" * 50)

# Básica
cuadrados = {x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados}")

# Con condicional
pares = {x for x in range(20) if x % 2 == 0}
print(f"Pares 0-19: {pares}")

# De string
texto = "Hola Mundo"
vocales = {c.lower() for c in texto if c.lower() in "aeiou"}
print(f"Vocales en '{texto}': {vocales}")

# Múltiplos
multiplos_3 = {x for x in range(1, 31) if x % 3 == 0}
print(f"Múltiplos de 3 (1-30): {multiplos_3}")

# ============================================
# 9. VERIFICAR PERTENENCIA
# ============================================

print("\n" + "=" * 50)
print("9. VERIFICAR PERTENENCIA")
print("=" * 50)

frutas = {"manzana", "banana", "cereza", "durazno"}

print(f"Frutas: {frutas}")
print(f"'banana' in frutas: {'banana' in frutas}")
print(f"'kiwi' in frutas: {'kiwi' in frutas}")
print(f"'uva' not in frutas: {'uva' not in frutas}")

# Verificar múltiples
buscar = ["manzana", "kiwi", "cereza", "pera"]
print(f"\nBuscando {buscar}:")
for fruta in buscar:
    if fruta in frutas:
        print(f"  ✓ {fruta} encontrada")
    else:
        print(f"  ✗ {fruta} NO encontrada")

# ============================================
# 10. EJEMPLO PRÁCTICO 1: ANÁLISIS DE TEXTO
# ============================================

print("\n" + "=" * 50)
print("10. EJEMPLO PRÁCTICO: ANÁLISIS DE TEXTO")
print("=" * 50)

texto1 = "Python es un lenguaje de programación poderoso"
texto2 = "Python es versátil y fácil de aprender"

# Convertir a sets de palabras
palabras1 = set(texto1.lower().split())
palabras2 = set(texto2.lower().split())

print(f"Texto 1: {texto1}")
print(f"Palabras únicas: {palabras1}\n")

print(f"Texto 2: {texto2}")
print(f"Palabras únicas: {palabras2}\n")

# Palabras en común
comunes = palabras1 & palabras2
print(f"Palabras en ambos textos: {comunes}")

# Palabras solo en texto 1
solo_texto1 = palabras1 - palabras2
print(f"Palabras solo en texto 1: {solo_texto1}")

# Palabras solo en texto 2
solo_texto2 = palabras2 - palabras1
print(f"Palabras solo en texto 2: {solo_texto2}")

# Todas las palabras únicas
todas = palabras1 | palabras2
print(f"Total palabras únicas: {len(todas)}")

# ============================================
# 11. EJEMPLO PRÁCTICO 2: GESTIÓN DE USUARIOS
# ============================================

print("\n" + "=" * 50)
print("11. EJEMPLO PRÁCTICO: GESTIÓN DE USUARIOS")
print("=" * 50)

# Usuarios en diferentes categorías
usuarios_premium = {"ana", "luis", "maría", "carlos"}
usuarios_activos = {"luis", "maría", "pedro", "elena"}
usuarios_admin = {"ana", "pedro"}

print(f"Premium: {usuarios_premium}")
print(f"Activos: {usuarios_activos}")
print(f"Admin:   {usuarios_admin}")

# Usuarios premium Y activos
premium_activos = usuarios_premium & usuarios_activos
print(f"\nPremium y Activos: {premium_activos}")

# Usuarios premium PERO NO activos
premium_inactivos = usuarios_premium - usuarios_activos
print(f"Premium pero Inactivos: {premium_inactivos}")

# Todos los usuarios únicos
todos_usuarios = usuarios_premium | usuarios_activos | usuarios_admin
print(f"Total usuarios únicos: {len(todos_usuarios)}")
print(f"Usuarios: {todos_usuarios}")

# Usuarios que son admin Y premium
admin_premium = usuarios_admin & usuarios_premium
print(f"\nAdmin y Premium: {admin_premium}")

# ============================================
# 12. EJEMPLO PRÁCTICO 3: VALIDACIÓN DE DATOS
# ============================================

print("\n" + "=" * 50)
print("12. EJEMPLO PRÁCTICO: VALIDACIÓN")
print("=" * 50)

# Validar que todos los IDs son únicos
ids_registrados = [101, 102, 103, 104, 105, 102, 106, 103]

print(f"IDs registrados: {ids_registrados}")
print(f"Total registros: {len(ids_registrados)}")
print(f"IDs únicos: {len(set(ids_registrados))}")

if len(ids_registrados) == len(set(ids_registrados)):
    print("✓ Todos los IDs son únicos")
else:
    print("✗ Hay IDs duplicados")
    # Encontrar duplicados
    vistos = set()
    duplicados = set()
    for id_ in ids_registrados:
        if id_ in vistos:
            duplicados.add(id_)
        vistos.add(id_)
    print(f"  IDs duplicados: {duplicados}")

# ============================================
# 13. EJEMPLO PRÁCTICO 4: COMPARAR INVENTARIOS
# ============================================

print("\n" + "=" * 50)
print("13. EJEMPLO PRÁCTICO: INVENTARIOS")
print("=" * 50)

# Inventarios de dos tiendas
tienda_a = {"laptop", "mouse", "teclado", "monitor", "webcam"}
tienda_b = {"laptop", "audifonos", "teclado", "tableta", "webcam"}

print(f"Tienda A: {tienda_a}")
print(f"Tienda B: {tienda_b}")

# Productos en ambas tiendas
ambas = tienda_a & tienda_b
print(f"\nEn ambas tiendas: {ambas}")

# Solo en tienda A
solo_a = tienda_a - tienda_b
print(f"Solo en Tienda A: {solo_a}")

# Solo en tienda B
solo_b = tienda_b - tienda_a
print(f"Solo en Tienda B: {solo_b}")

# Catálogo completo
catalogo = tienda_a | tienda_b
print(f"\nCatálogo completo: {catalogo}")
print(f"Total productos únicos: {len(catalogo)}")

print("\n" + "=" * 50)
print("FIN DE LOS EJEMPLOS")
print("=" * 50)
