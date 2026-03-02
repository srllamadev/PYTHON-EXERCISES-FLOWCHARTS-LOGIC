"""
PASS - Ejemplos
===============
Ejemplos de uso de la sentencia pass
"""

# Ejemplo 1: Placeholder en condicional
print("=== Ejemplo 1: Pass en Condicional ===")
for num in range(1, 6):
    if num == 3:
        pass  # TODO: Implementar lógica especial para el 3
    else:
        print(f"Número: {num}")

print("Nota: El número 3 no fue procesado (pass)\n")

# Ejemplo 2: Función vacía (por implementar)
print("=== Ejemplo 2: Funciones Placeholder ===")

def procesar_datos():
    """Esta función se implementará después"""
    pass

def validar_usuario():
    """Validación pendiente"""
    pass

def enviar_email():
    """Sistema de email en desarrollo"""
    pass

print("Funciones definidas pero vacías (con pass)")
print("- procesar_datos()")
print("- validar_usuario()")
print("- enviar_email()\n")

# Ejemplo 3: Clase vacía
print("=== Ejemplo 3: Clase Placeholder ===")

class Usuario:
    """Modelo de usuario - pendiente de implementar"""
    pass

class Producto:
    pass

class Pedido:
    pass

# Se pueden crear instancias aunque estén vacías
usuario1 = Usuario()
producto1 = Producto()

print("Clases vacías creadas con pass:")
print(f"- Usuario: {usuario1}")
print(f"- Producto: {producto1}\n")

# Ejemplo 4: Exception handler vacío
print("=== Ejemplo 4: Manejo de Excepciones Silencioso ===")
numeros = [1, 2, "tres", 4, "cinco", 6]

print("Procesando lista con elementos mezclados:")
for num in numeros:
    try:
        resultado = num * 2
        print(f"  {num} × 2 = {resultado}")
    except TypeError:
        pass  # Ignorar elementos que no se pueden multiplicar

print()

# Ejemplo 5: Loop con condiciones complejas
print("=== Ejemplo 5: Múltiples Condiciones ===")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} es par")
    elif i % 3 == 0:
        print(f"{i} es múltiplo de 3")
    elif i % 5 == 0:
        print(f"{i} es múltiplo de 5")
    else:
        pass  # Números que no cumplen ninguna condición

print()

# Ejemplo 6: Desarrollo incremental
print("=== Ejemplo 6: Desarrollo por Fases ===")

def sistema_completo():
    """Sistema en desarrollo por fases"""
    
    # Fase 1: Completada
    print("✅ Fase 1: Inicialización")
    inicializar_sistema()
    
    # Fase 2: En desarrollo
    print("🚧 Fase 2: Procesamiento (en desarrollo)")
    pass
    
    # Fase 3: Pendiente
    print("⏳ Fase 3: Finalización (pendiente)")
    pass

def inicializar_sistema():
    print("   Sistema inicializado correctamente")

sistema_completo()

print()

# Ejemplo 7: Estructuras de control temporales
print("=== Ejemplo 7: Debug Temporal ===")

modo_debug = True

for i in range(5):
    if modo_debug:
        pass  # En producción aquí iría: logging.debug(f"Iteración {i}")
    
    print(f"Procesando item {i}")

print()

# Ejemplo 8: Context manager vacío
print("=== Ejemplo 8: Context Manager Placeholder ===")

class ConexionDB:
    """Simulación de conexión a base de datos"""
    
    def __enter__(self):
        print("  [Conectando a DB...]")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  [Cerrando conexión DB...]")
        pass  # Aquí iría la lógica de cierre real

print("Usando context manager:")
with ConexionDB() as db:
    pass  # Por ahora no hacemos nada con la conexión

print()

# Ejemplo 9: Match/Case con pass (Python 3.10+)
print("=== Ejemplo 9: Pattern Matching con Pass ===")

def procesar_comando(comando):
    """Procesador de comandos - en desarrollo"""
    match comando:
        case "iniciar":
            print("  Sistema iniciado")
        case "detener":
            print("  Sistema detenido")
        case "pausar":
            pass  # TODO: Implementar pausa
        case "reiniciar":
            pass  # TODO: Implementar reinicio
        case _:
            print(f"  Comando '{comando}' no reconocido")

comandos = ["iniciar", "pausar", "detener", "reiniciar"]
print("Probando comandos:")
for cmd in comandos:
    print(f"Comando: {cmd}")
    procesar_comando(cmd)

print()

# Ejemplo 10: Combinación práctica
print("=== Ejemplo 10: Sistema de Categorización ===")

productos = [
    {"nombre": "Laptop", "categoria": "electronica", "precio": 1200},
    {"nombre": "Camisa", "categoria": "ropa", "precio": 30},
    {"nombre": "Libro", "categoria": "libros", "precio": 15},
    {"nombre": "Mouse", "categoria": "electronica", "precio": 25}
]

print("Procesando productos por categoría:\n")

for producto in productos:
    categoria = producto["categoria"]
    nombre = producto["nombre"]
    precio = producto["precio"]
    
    if categoria == "electronica":
        print(f"📱 {nombre}: ${precio} (Electrónica)")
    elif categoria == "ropa":
        print(f"👕 {nombre}: ${precio} (Ropa)")
    elif categoria == "libros":
        pass  # TODO: Implementar procesamiento especial para libros
    else:
        pass  # Categorías futuras

print("\nNota: Categoría 'libros' aún no implementada")
