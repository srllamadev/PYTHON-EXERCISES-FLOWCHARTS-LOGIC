"""
BREAK, CONTINUE, PASS - Ejemplo Combinado
==========================================
Uso conjunto de las tres sentencias de control
"""

# Ejemplo 1: Sistema de procesamiento de pedidos
print("=== Ejemplo 1: Sistema de Pedidos ===")

pedidos = [
    {"id": 101, "total": 150, "estado": "pendiente"},
    {"id": 102, "total": 0, "estado": "pendiente"},      # Total inválido
    {"id": 103, "total": 300, "estado": "cancelado"},    # Cancelado
    {"id": 104, "total": 200, "estado": "pendiente"},
    {"id": 105, "total": -50, "estado": "pendiente"},    # Total inválido
    {"id": 106, "total": 500, "estado": "pendiente"},
]

limite_procesamiento = 1000
total_procesado = 0

print("Procesando pedidos:\n")

for pedido in pedidos:
    id_pedido = pedido["id"]
    total = pedido["total"]
    estado = pedido["estado"]
    
    # CONTINUE: Saltar pedidos cancelados
    if estado == "cancelado":
        print(f"⏭️  Pedido {id_pedido}: CANCELADO (saltado)")
        continue
    
    # CONTINUE: Saltar pedidos con total inválido
    if total <= 0:
        print(f"❌ Pedido {id_pedido}: Total inválido ${total} (saltado)")
        continue
    
    # BREAK: Detener si se alcanza el límite
    if total_procesado + total > limite_procesamiento:
        print(f"\n🛑 Límite alcanzado con pedido {id_pedido}")
        print(f"   No se puede procesar ${total} (excede límite)")
        break
    
    # PASS: Placeholder para lógica futura
    if total > 400:
        pass  # TODO: Aplicar descuento especial
    
    # Procesar pedido válido
    total_procesado += total
    print(f"✅ Pedido {id_pedido}: ${total} procesado (Total: ${total_procesado})")

print(f"\n📊 Total procesado: ${total_procesado}")

print("\n" + "="*60 + "\n")

# Ejemplo 2: Validador de datos de estudiantes
print("=== Ejemplo 2: Validador de Estudiantes ===")

estudiantes = [
    {"nombre": "Ana López", "edad": 20, "notas": [8, 9, 7]},
    {"nombre": "", "edad": 22, "notas": [6, 7, 8]},                    # Nombre vacío
    {"nombre": "Carlos Ruiz", "edad": -5, "notas": [9, 9, 10]},        # Edad inválida
    {"nombre": "Diana Torres", "edad": 21, "notas": []},               # Sin notas
    {"nombre": "Eduardo Gómez", "edad": 23, "notas": [7, 8, 9]},
    {"nombre": "STOP", "edad": 0, "notas": []},                        # Marca de fin
    {"nombre": "Lucía Fernández", "edad": 19, "notas": [10, 9, 10]},
]

print("Validando y procesando estudiantes:\n")

for i, estudiante in enumerate(estudiantes, 1):
    nombre = estudiante["nombre"]
    edad = estudiante["edad"]
    notas = estudiante["notas"]
    
    # BREAK: Detener si encontramos marca de fin
    if nombre == "STOP":
        print(f"🛑 Marca STOP encontrada. Deteniendo procesamiento.")
        break
    
    # CONTINUE: Saltar si el nombre está vacío
    if not nombre.strip():
        print(f"#{i} ⚠️  Nombre vacío (registro saltado)")
        continue
    
    # CONTINUE: Saltar si la edad es inválida
    if edad < 0 or edad > 100:
        print(f"#{i} ❌ {nombre}: Edad inválida ({edad}) - saltado")
        continue
    
    # CONTINUE: Saltar si no tiene notas
    if not notas:
        print(f"#{i} ⚠️  {nombre}: Sin notas - saltado")
        continue
    
    # PASS: Reservado para validaciones futuras
    if edad < 18:
        pass  # TODO: Marcar como menor de edad
    
    # Procesar estudiante válido
    promedio = sum(notas) / len(notas)
    print(f"#{i} ✅ {nombre} ({edad} años)")
    print(f"     Notas: {notas} → Promedio: {promedio:.2f}")

print("\n" + "="*60 + "\n")

# Ejemplo 3: Procesador de transacciones bancarias
print("=== Ejemplo 3: Procesador de Transacciones ===")

transacciones = [
    {"tipo": "deposito", "monto": 500, "cuenta": "activa"},
    {"tipo": "retiro", "monto": 100, "cuenta": "activa"},
    {"tipo": "deposito", "monto": -50, "cuenta": "activa"},        # Monto negativo
    {"tipo": "retiro", "monto": 200, "cuenta": "bloqueada"},       # Cuenta bloqueada
    {"tipo": "transferencia", "monto": 300, "cuenta": "activa"},   # No implementado
    {"tipo": "retiro", "monto": 1500, "cuenta": "activa"},         # Excede saldo
    {"tipo": "deposito", "monto": 1000, "cuenta": "activa"},
]

saldo = 1000
limite_transaccion = 5
transacciones_procesadas = 0

print(f"💰 Saldo inicial: ${saldo}")
print(f"📊 Límite: {limite_transaccion} transacciones\n")

for i, trans in enumerate(transacciones, 1):
    tipo = trans["tipo"]
    monto = trans["monto"]
    cuenta = trans["cuenta"]
    
    # BREAK: Límite de transacciones alcanzado
    if transacciones_procesadas >= limite_transaccion:
        print(f"\n🛑 Límite de {limite_transaccion} transacciones alcanzado")
        print(f"   Transacciones restantes no procesadas: {len(transacciones) - i + 1}")
        break
    
    # CONTINUE: Cuenta bloqueada
    if cuenta == "bloqueada":
        print(f"#{i} 🔒 {tipo.capitalize()}: Cuenta bloqueada - saltado")
        continue
    
    # CONTINUE: Monto inválido
    if monto <= 0:
        print(f"#{i} ❌ {tipo.capitalize()}: Monto inválido (${monto}) - saltado")
        continue
    
    # PASS: Tipo de transacción no implementado
    if tipo == "transferencia":
        print(f"#{i} 🚧 Transferencia: No implementada - saltado")
        pass  # TODO: Implementar transferencias
        continue
    
    # Procesar según tipo
    if tipo == "deposito":
        saldo += monto
        transacciones_procesadas += 1
        print(f"#{i} ✅ Depósito: +${monto} → Saldo: ${saldo}")
    
    elif tipo == "retiro":
        if monto > saldo:
            print(f"#{i} ⚠️  Retiro: ${monto} excede saldo (${saldo}) - saltado")
            continue
        
        saldo -= monto
        transacciones_procesadas += 1
        print(f"#{i} ✅ Retiro: -${monto} → Saldo: ${saldo}")

print(f"\n💵 Saldo final: ${saldo}")
print(f"📈 Transacciones procesadas: {transacciones_procesadas}")

print("\n" + "="*60 + "\n")

# Ejemplo 4: Analizador de código fuente (simplificado)
print("=== Ejemplo 4: Analizador de Código ===")

codigo = [
    "def calcular_suma(a, b):",
    "    # Esta es una función",
    "    resultado = a + b",
    "    ",  # Línea vacía
    "    return resultado",
    "",
    "# TODO: Implementar resta",
    "def calcular_resta(a, b):",
    "    pass",
    "ERROR_LINE",  # Marca de error crítico
    "print('Hola')",
]

print("Analizando código fuente:\n")

lineas_codigo = 0
lineas_comentario = 0
lineas_vacias = 0

for num_linea, linea in enumerate(codigo, 1):
    linea_limpia = linea.strip()
    
    # BREAK: Error crítico encontrado
    if "ERROR_LINE" in linea:
        print(f"❌ Línea {num_linea}: ERROR CRÍTICO - Análisis detenido")
        break
    
    # CONTINUE: Líneas vacías
    if not linea_limpia:
        lineas_vacias += 1
        continue
    
    # Comentarios
    if linea_limpia.startswith('#'):
        lineas_comentario += 1
        print(f"💬 Línea {num_linea}: Comentario")
        continue
    
    # PASS: Placeholder
    if "pass" in linea_limpia:
        print(f"🚧 Línea {num_linea}: Placeholder (pass)")
        pass  # Aquí podríamos marcar para revisión
    
    # Código ejecutable
    lineas_codigo += 1
    print(f"✅ Línea {num_linea}: {linea_limpia[:40]}...")

print(f"\n📊 Estadísticas:")
print(f"   Líneas de código: {lineas_codigo}")
print(f"   Comentarios: {lineas_comentario}")
print(f"   Líneas vacías: {lineas_vacias}")
print(f"   Total analizado: {lineas_codigo + lineas_comentario + lineas_vacias}")
