"""
Ejemplos prácticos de Tuplas en Python
Autor: Python Course
Fecha: 2026
"""

from collections import namedtuple

# ============================================
# 1. CREACIÓN DE TUPLAS
# ============================================

print("=" * 50)
print("1. CREACIÓN DE TUPLAS")
print("=" * 50)

# Diferentes formas de crear tuplas
tupla_vacia = ()
numeros = (1, 2, 3, 4, 5)
punto = (10, 20)
mixta = (1, "dos", 3.0, True, None)

# Sin paréntesis (empaquetado)
coordenadas = 10, 20, 30

# Tupla de un elemento
un_elemento = (42,)
no_es_tupla = (42)  # Esto es un int

# Constructor tuple()
desde_lista = tuple([1, 2, 3])
desde_string = tuple("Python")
desde_rango = tuple(range(5))

print(f"Tupla vacía: {tupla_vacia} - Tipo: {type(tupla_vacia)}")
print(f"Números: {numeros}")
print(f"Punto: {punto}")
print(f"Sin paréntesis: {coordenadas}")
print(f"Un elemento: {un_elemento} - Tipo: {type(un_elemento)}")
print(f"NO es tupla: {no_es_tupla} - Tipo: {type(no_es_tupla)}")
print(f"Desde string: {desde_string}")

# ============================================
# 2. ACCESO A ELEMENTOS
# ============================================

print("\n" + "=" * 50)
print("2. ACCESO A ELEMENTOS")
print("=" * 50)

colores = ("rojo", "verde", "azul", "amarillo", "morado")

print(f"Primer color: {colores[0]}")
print(f"Tercer color: {colores[2]}")
print(f"Último color: {colores[-1]}")
print(f"Penúltimo color: {colores[-2]}")

# ============================================
# 3. SLICING
# ============================================

print("\n" + "=" * 50)
print("3. SLICING")
print("=" * 50)

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"Original: {numeros}")
print(f"Primeros 5: {numeros[:5]}")
print(f"Últimos 3: {numeros[-3:]}")
print(f"Del índice 2 al 6: {numeros[2:7]}")
print(f"Cada 2 elementos: {numeros[::2]}")
print(f"Invertida: {numeros[::-1]}")

# ============================================
# 4. MÉTODOS DE TUPLAS
# ============================================

print("\n" + "=" * 50)
print("4. MÉTODOS DE TUPLAS")
print("=" * 50)

numeros = (1, 2, 2, 3, 2, 4, 5, 2, 6)

# count() - Contar ocurrencias
contador = numeros.count(2)
print(f"El 2 aparece {contador} veces en {numeros}")

# index() - Encontrar índice
indice = numeros.index(3)
print(f"El primer 3 está en el índice: {indice}")

# Buscar desde cierta posición
indice_segundo_2 = numeros.index(2, 2)  # Buscar desde índice 2
print(f"El segundo 2 está en el índice: {indice_segundo_2}")

# ============================================
# 5. INMUTABILIDAD
# ============================================

print("\n" + "=" * 50)
print("5. INMUTABILIDAD")
print("=" * 50)

tupla = (1, 2, 3, 4, 5)
print(f"Tupla original: {tupla}")

# Esto causaría un error
# tupla[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Pero podemos crear una nueva tupla
nueva_tupla = (10,) + tupla[1:]
print(f"Nueva tupla: {nueva_tupla}")

# Concatenación crea nueva tupla
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_combinada = tupla1 + tupla2
print(f"Combinada: {tupla_combinada}")

# Repetición
tupla_repetida = tupla1 * 3
print(f"Repetida: {tupla_repetida}")

# IMPORTANTE: Objetos mutables dentro de tuplas
tupla_con_lista = (1, [2, 3], 4)
print(f"\nAntes: {tupla_con_lista}")
tupla_con_lista[1].append(5)  # La lista interna SÍ puede cambiar
print(f"Después: {tupla_con_lista}")

# ============================================
# 6. DESEMPAQUETADO
# ============================================

print("\n" + "=" * 50)
print("6. DESEMPAQUETADO")
print("=" * 50)

# Desempaquetado básico
punto = (10, 20)
x, y = punto
print(f"Punto: {punto} -> x={x}, y={y}")

# Desempaquetado con múltiples valores
persona = ("Ana", 25, "Madrid", "Ingeniera")
nombre, edad, ciudad, profesion = persona
print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}, Profesión: {profesion}")

# Desempaquetado con * (resto)
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
primero, segundo, *resto = numeros
print(f"Primero: {primero}, Segundo: {segundo}, Resto: {resto}")

primero, *medio, ultimo = numeros
print(f"Primero: {primero}, Medio: {medio}, Último: {ultimo}")

# Intercambio de valores
a = 5
b = 10
print(f"Antes: a={a}, b={b}")
a, b = b, a
print(f"Después del intercambio: a={a}, b={b}")

# ============================================
# 7. TUPLAS EN FUNCIONES
# ============================================

print("\n" + "=" * 50)
print("7. TUPLAS EN FUNCIONES")
print("=" * 50)

# Retornar múltiples valores
def obtener_estadisticas(numeros):
    """Retorna min, max, promedio de una lista"""
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)
    return minimo, maximo, promedio  # Retorna tupla

datos = [10, 20, 30, 40, 50]
min_val, max_val, prom = obtener_estadisticas(datos)
print(f"Datos: {datos}")
print(f"Mínimo: {min_val}, Máximo: {max_val}, Promedio: {prom}")

# Función con parámetros tupla
def calcular_distancia(punto1, punto2):
    """Calcula distancia euclidiana entre dos puntos"""
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distancia

p1 = (0, 0)
p2 = (3, 4)
dist = calcular_distancia(p1, p2)
print(f"\nDistancia entre {p1} y {p2}: {dist}")

# ============================================
# 8. TUPLAS COMO CLAVES DE DICCIONARIOS
# ============================================

print("\n" + "=" * 50)
print("8. TUPLAS COMO CLAVES DE DICCIONARIOS")
print("=" * 50)

# Coordenadas como claves
coordenadas_ciudades = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522, -118.2437): "Los Ángeles",
    (51.5074, -0.1278): "Londres",
    (48.8566, 2.3522): "París"
}

print("Ciudades por coordenadas:")
for coords, ciudad in coordenadas_ciudades.items():
    lat, lon = coords
    print(f"  {ciudad}: Lat {lat}, Lon {lon}")

# Buscar ciudad
coordenada_buscar = (51.5074, -0.1278)
if coordenada_buscar in coordenadas_ciudades:
    print(f"\nCoordenada {coordenada_buscar}: {coordenadas_ciudades[coordenada_buscar]}")

# Tablero de ajedrez
tablero = {
    ('a', 1): 'Torre Blanca',
    ('b', 1): 'Caballo Blanco',
    ('c', 1): 'Alfil Blanco',
    ('d', 1): 'Reina Blanca',
    ('e', 1): 'Rey Blanco'
}

print(f"\nPieza en (d, 1): {tablero[('d', 1)]}")

# ============================================
# 9. TUPLAS NOMBRADAS (namedtuple)
# ============================================

print("\n" + "=" * 50)
print("9. TUPLAS NOMBRADAS")
print("=" * 50)

# Definir estructuras
Punto = namedtuple('Punto', ['x', 'y'])
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])
Producto = namedtuple('Producto', ['id', 'nombre', 'precio', 'stock'])

# Crear instancias
p1 = Punto(10, 20)
p2 = Punto(x=30, y=40)  # Con nombres

persona1 = Persona('Ana', 25, 'Madrid')
persona2 = Persona(nombre='Luis', edad=30, ciudad='Barcelona')

producto = Producto(1, 'Laptop', 999.99, 15)

# Acceso por nombre (más legible)
print(f"Punto 1: x={p1.x}, y={p1.y}")
print(f"Punto 2: x={p2.x}, y={p2.y}")

print(f"\nPersona: {persona1.nombre}, {persona1.edad} años, vive en {persona1.ciudad}")

print(f"\nProducto: {producto.nombre}, Precio: ${producto.precio}, Stock: {producto.stock}")

# También funciona acceso por índice
print(f"Primer valor de punto: {p1[0]}")

# Convertir a diccionario
dict_persona = persona1._asdict()
print(f"\nPersona como dict: {dict_persona}")

# ============================================
# 10. OPERACIONES Y COMPARACIONES
# ============================================

print("\n" + "=" * 50)
print("10. OPERACIONES")
print("=" * 50)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenación
combinada = tupla1 + tupla2
print(f"Concatenación: {combinada}")

# Repetición
repetida = tupla1 * 3
print(f"Repetición: {repetida}")

# Pertenencia
print(f"¿2 está en tupla1? {2 in tupla1}")
print(f"¿10 está en tupla1? {10 in tupla1}")

# Longitud
print(f"Longitud de tupla1: {len(tupla1)}")

# Min, Max, Sum
numeros = (5, 2, 8, 1, 9, 3)
print(f"\nTupla: {numeros}")
print(f"Mínimo: {min(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Suma: {sum(numeros)}")

# Comparaciones
tupla_a = (1, 2, 3)
tupla_b = (1, 2, 4)
tupla_c = (1, 2, 3)

print(f"\n{tupla_a} == {tupla_c}: {tupla_a == tupla_c}")
print(f"{tupla_a} < {tupla_b}: {tupla_a < tupla_b}")
print(f"{tupla_a} > {tupla_b}: {tupla_a > tupla_b}")

# ============================================
# 11. EJEMPLO PRÁCTICO: BASE DE DATOS
# ============================================

print("\n" + "=" * 50)
print("11. EJEMPLO PRÁCTICO: REGISTROS")
print("=" * 50)

# Definir estructura de registro
Empleado = namedtuple('Empleado', ['id', 'nombre', 'departamento', 'salario'])

# Base de datos de empleados (tupla de tuplas)
empleados = (
    Empleado(1, "Ana García", "Ventas", 45000),
    Empleado(2, "Luis Pérez", "IT", 55000),
    Empleado(3, "María López", "IT", 52000),
    Empleado(4, "Carlos Ruiz", "RRHH", 48000),
    Empleado(5, "Elena Torres", "Ventas", 47000),
)

print("LISTA DE EMPLEADOS")
print("-" * 60)
print(f"{'ID':<5} {'Nombre':<15} {'Departamento':<12} {'Salario':>10}")
print("-" * 60)

for emp in empleados:
    print(f"{emp.id:<5} {emp.nombre:<15} {emp.departamento:<12} ${emp.salario:>9,.2f}")

# Filtrar por departamento
print("\n\nEMPLEADOS DE IT:")
print("-" * 40)
empleados_it = [emp for emp in empleados if emp.departamento == "IT"]
for emp in empleados_it:
    print(f"  {emp.nombre}: ${emp.salario:,.2f}")

# Calcular salario promedio
salario_total = sum(emp.salario for emp in empleados)
salario_promedio = salario_total / len(empleados)
print(f"\nSalario promedio: ${salario_promedio:,.2f}")

# Empleado con mayor salario
empleado_mayor_salario = max(empleados, key=lambda emp: emp.salario)
print(f"Mayor salario: {empleado_mayor_salario.nombre} - ${empleado_mayor_salario.salario:,.2f}")

print("\n" + "=" * 50)
print("FIN DE LOS EJEMPLOS")
print("=" * 50)
