"""
Ejemplos prácticos de Diccionarios en Python
Autor: Python Course
Fecha: 2026
"""

from collections import defaultdict, OrderedDict, Counter

# ============================================
# 1. CREACIÓN DE DICCIONARIOS
# ============================================

print("=" * 50)
print("1. CREACIÓN DE DICCIONARIOS")
print("=" * 50)

# Diferentes formas de crear diccionarios
diccionario_vacio = {}
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
numeros = {1: "uno", 2: "dos", 3: "tres"}
mixto = {"texto": "hola", 100: "número", (1, 2): "tupla como clave"}

# Constructor dict()
desde_lista = dict([("a", 1), ("b", 2), ("c", 3)])
con_keywords = dict(nombre="Luis", edad=30, ciudad="Barcelona")
desde_zip = dict(zip(["x", "y", "z"], [1, 2, 3]))

# Dict comprehension
cuadrados = {x: x**2 for x in range(6)}

print(f"Persona: {persona}")
print(f"Números: {numeros}")
print(f"Desde lista de tuplas: {desde_lista}")
print(f"Con keywords: {con_keywords}")
print(f"Desde zip: {desde_zip}")
print(f"Cuadrados: {cuadrados}")

# ============================================
# 2. ACCESO Y MODIFICACIÓN
# ============================================

print("\n" + "=" * 50)
print("2. ACCESO Y MODIFICACIÓN")
print("=" * 50)

estudiante = {
    "nombre": "Carlos",
    "edad": 22,
    "carrera": "Ingeniería",
    "semestre": 5
}

print(f"Estudiante original: {estudiante}")

# Acceso directo
print(f"\nNombre: {estudiante['nombre']}")
print(f"Edad: {estudiante['edad']}")

# Método get() (más seguro)
carrera = estudiante.get("carrera")
pais = estudiante.get("pais", "México")  # Valor por defecto
print(f"Carrera: {carrera}")
print(f"País (con default): {pais}")

# Modificar valor existente
estudiante["edad"] = 23
print(f"\nDespués de modificar edad: {estudiante}")

# Agregar nuevo par clave-valor
estudiante["promedio"] = 8.5
estudiante["materias"] = ["Cálculo", "Programación", "Física"]
print(f"Después de agregar campos: {estudiante}")

# Eliminar elementos
del estudiante["semestre"]
print(f"\nDespués de eliminar 'semestre': {estudiante}")

promedio = estudiante.pop("promedio")
print(f"Promedio eliminado: {promedio}")
print(f"Diccionario: {estudiante}")

# ============================================
# 3. MÉTODOS DE DICCIONARIOS
# ============================================

print("\n" + "=" * 50)
print("3. MÉTODOS DE DICCIONARIOS")
print("=" * 50)

inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "plátanos": 25
}

print(f"Inventario: {inventario}")

# keys() - Obtener claves
claves = inventario.keys()
print(f"\nClaves: {list(claves)}")

# values() - Obtener valores
valores = inventario.values()
print(f"Valores: {list(valores)}")

# items() - Obtener pares clave-valor
items = inventario.items()
print(f"Items: {list(items)}")

# update() - Actualizar con otro diccionario
nuevos_productos = {"uvas": 15, "peras": 20}
inventario.update(nuevos_productos)
print(f"\nDespués de update: {inventario}")

# setdefault() - Obtener o crear con valor por defecto
kiwis = inventario.setdefault("kiwis", 0)
print(f"Kiwis (creado): {kiwis}")
print(f"Inventario: {inventario}")

# clear()
copia_inventario = inventario.copy()
copia_inventario.clear()
print(f"\nCopia limpia: {copia_inventario}")
print(f"Original intacto: {inventario}")

# ============================================
# 4. ITERACIÓN
# ============================================

print("\n" + "=" * 50)
print("4. ITERACIÓN")
print("=" * 50)

calificaciones = {
    "Ana": 95,
    "Luis": 88,
    "María": 92,
    "Carlos": 85
}

# Iterar sobre claves
print("Nombres de estudiantes:")
for nombre in calificaciones:
    print(f"  - {nombre}")

# Iterar sobre valores
print("\nCalificaciones:")
for calif in calificaciones.values():
    print(f"  - {calif}")

# Iterar sobre pares clave-valor
print("\nReporte completo:")
for nombre, calif in calificaciones.items():
    print(f"  {nombre}: {calif} puntos")

# ============================================
# 5. DICCIONARIOS ANIDADOS
# ============================================

print("\n" + "=" * 50)
print("5. DICCIONARIOS ANIDADOS")
print("=" * 50)

empresa = {
    "nombre": "Tech Solutions",
    "fundacion": 2015,
    "departamentos": {
        "IT": {
            "empleados": 15,
            "presupuesto": 500000,
            "proyectos": ["Web App", "Mobile App"]
        },
        "Ventas": {
            "empleados": 8,
            "presupuesto": 300000,
            "proyectos": ["Campaña Q1", "Expansión"]
        },
        "RRHH": {
            "empleados": 3,
            "presupuesto": 150000,
            "proyectos": ["Reclutamiento", "Capacitación"]
        }
    }
}

print(f"Empresa: {empresa['nombre']}")
print(f"Fundación: {empresa['fundacion']}")

print("\nDepartamentos:")
for dept, info in empresa["departamentos"].items():
    print(f"\n  {dept}:")
    print(f"    Empleados: {info['empleados']}")
    print(f"    Presupuesto: ${info['presupuesto']:,}")
    print(f"    Proyectos: {', '.join(info['proyectos'])}")

# Acceso anidado profundo
primer_proyecto_it = empresa["departamentos"]["IT"]["proyectos"][0]
print(f"\nPrimer proyecto de IT: {primer_proyecto_it}")

# ============================================
# 6. FUSIONAR DICCIONARIOS
# ============================================

print("\n" + "=" * 50)
print("6. FUSIONAR DICCIONARIOS")
print("=" * 50)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

# Método 1: Operador | (Python 3.9+)
fusionado = dict1 | dict2 | dict3
print(f"Fusionado con |: {fusionado}")

# Método 2: Desempaquetado
fusionado2 = {**dict1, **dict2, **dict3}
print(f"Fusionado con **: {fusionado2}")

# Método 3: update()
fusionado3 = {}
fusionado3.update(dict1)
fusionado3.update(dict2)
fusionado3.update(dict3)
print(f"Fusionado con update: {fusionado3}")

# Conflictos: el último valor gana
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 99, "z": 3}
resultado = dict_a | dict_b
print(f"\nConflicto: {dict_a} | {dict_b} = {resultado}")

# ============================================
# 7. COMPRENSIÓN DE DICCIONARIOS
# ============================================

print("\n" + "=" * 50)
print("7. COMPRENSIÓN DE DICCIONARIOS")
print("=" * 50)

# Cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados}")

# Con condicional
pares_cuadrados = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Cuadrados de pares: {pares_cuadrados}")

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Invertido: {invertido}")

# Filtrar diccionario
edades = {"Ana": 25, "Luis": 17, "María": 30, "Carlos": 16, "Elena": 22}
mayores_edad = {nombre: edad for nombre, edad in edades.items() if edad >= 18}
print(f"\nMayores de edad: {mayores_edad}")

# Transformar valores
precios = {"laptop": 1000, "mouse": 25, "teclado": 75}
con_iva = {producto: precio * 1.16 for producto, precio in precios.items()}
print(f"\nPrecios con IVA (16%): {con_iva}")

# ============================================
# 8. DEFAULTDICT
# ============================================

print("\n" + "=" * 50)
print("8. DEFAULTDICT")
print("=" * 50)

# Contador de palabras
texto = "python es genial python es poderoso python es versátil"
palabras = texto.split()

# Con dict normal (más verboso)
conteo_normal = {}
for palabra in palabras:
    conteo_normal[palabra] = conteo_normal.get(palabra, 0) + 1
print(f"Conteo con dict normal: {conteo_normal}")

# Con defaultdict (más limpio)
conteo_default = defaultdict(int)
for palabra in palabras:
    conteo_default[palabra] += 1
print(f"Conteo con defaultdict: {dict(conteo_default)}")

# Agrupar elementos
estudiantes = [
    ("Ana", "A"),
    ("Luis", "B"),
    ("María", "A"),
    ("Carlos", "C"),
    ("Elena", "B"),
    ("Pedro", "A")
]

por_grado = defaultdict(list)
for nombre, grado in estudiantes:
    por_grado[grado].append(nombre)

print("\nEstudiantes por grado:")
for grado, nombres in sorted(por_grado.items()):
    print(f"  Grado {grado}: {', '.join(nombres)}")

# ============================================
# 9. COUNTER
# ============================================

print("\n" + "=" * 50)
print("9. COUNTER (collections)")
print("=" * 50)

# Contar elementos
votos = ["Ana", "Luis", "Ana", "María", "Luis", "Ana", "Carlos", "Ana"]
contador = Counter(votos)

print(f"Votos totales: {dict(contador)}")

# Más comunes
print(f"\nTOP 2 candidatos:")
for candidato, votos in contador.most_common(2):
    print(f"  {candidato}: {votos} votos")

# Operaciones con Counters
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"\nC1: {dict(c1)}")
print(f"C2: {dict(c2)}")
print(f"C1 + C2: {dict(c1 + c2)}")
print(f"C1 - C2: {dict(c1 - c2)}")

# ============================================
# 10. EJEMPLO PRÁCTICO: SISTEMA DE INVENTARIO
# ============================================

print("\n" + "=" * 50)
print("10. EJEMPLO PRÁCTICO: INVENTARIO")
print("=" * 50)

# Sistema de inventario de tienda
inventario = {
    "laptops": {"cantidad": 15, "precio": 999.99, "categoria": "electrónica"},
    "teclados": {"cantidad": 45, "precio": 49.99, "categoria": "accesorios"},
    "monitores": {"cantidad": 20, "precio": 299.99, "categoria": "electrónica"},
    "ratones": {"cantidad": 60, "precio": 24.99, "categoria": "accesorios"},
    "webcams": {"cantidad": 12, "precio": 79.99, "categoria": "accesorios"}
}

print("INVENTARIO DE LA TIENDA")
print("-" * 70)
print(f"{'Producto':<15} {'Cantidad':>10} {'Precio':>12} {'Categoría':<15}")
print("-" * 70)

valor_total = 0
for producto, info in inventario.items():
    cantidad = info["cantidad"]
    precio = info["precio"]
    categoria = info["categoria"]
    valor = cantidad * precio
    valor_total += valor
    
    print(f"{producto.capitalize():<15} {cantidad:>10} ${precio:>10.2f} {categoria:<15}")

print("-" * 70)
print(f"Valor total del inventario: ${valor_total:,.2f}")

# Productos por categoría
print("\nPRODUCTOS POR CATEGORÍA:")
categorias = defaultdict(list)
for producto, info in inventario.items():
    categorias[info["categoria"]].append(producto)

for categoria, productos in categorias.items():
    print(f"  {categoria.capitalize()}: {', '.join(productos)}")

# Productos con bajo stock (< 20)
print("\nALERTA - BAJO STOCK:")
bajo_stock = {prod: info for prod, info in inventario.items() if info["cantidad"] < 20}
for producto, info in bajo_stock.items():
    print(f"  {producto}: Solo {info['cantidad']} unidades")

print("\n" + "=" * 50)
print("FIN DE LOS EJEMPLOS")
print("=" * 50)
