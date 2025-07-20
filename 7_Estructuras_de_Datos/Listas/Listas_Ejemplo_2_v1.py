"""
SISTEMA DE CONTABILIDAD BÁSICO
Este programa demuestra el uso de listas para gestionar transacciones contables,
calcular balances, generar reportes y analizar datos financieros.
"""

class SistemaContabilidad:
    def __init__(self):
        # Lista principal para almacenar transacciones
        # Cada transacción es un diccionario con: fecha, descripción, tipo, monto, categoría
        self.transacciones = []
        
        # Lista de categorías válidas
        self.categorias_validas = ["Ventas", "Compras", "Nómina", "Impuestos", "Servicios", "Otros"]

    def agregar_transaccion(self, fecha, descripcion, tipo, monto, categoria):
        """Agrega una nueva transacción a la lista con validación de datos"""
        if tipo not in ["ingreso", "gasto"]:
            raise ValueError("Tipo inválido. Debe ser 'ingreso' o 'gasto'")
        
        if categoria not in self.categorias_validas:
            raise ValueError(f"Categoría inválida. Opciones: {', '.join(self.categorias_validas)}")
        
        nueva_transaccion = {
            "fecha": fecha,
            "descripcion": descripcion,
            "tipo": tipo,
            "monto": monto,
            "categoria": categoria
        }
        self.transacciones.append(nueva_transaccion)
        print(f"Transacción agregada: {descripcion} (${monto:.2f})")

    def calcular_balance(self):
        """Calcula el balance total sumando ingresos y restando gastos"""
        total_ingresos = sum(t['monto'] for t in self.transacciones if t['tipo'] == 'ingreso')
        total_gastos = sum(t['monto'] for t in self.transacciones if t['tipo'] == 'gasto')
        return total_ingresos - total_gastos

    def generar_reporte_categorias(self):
        """Genera un reporte de ingresos/gastos por categoría usando listas y diccionarios"""
        reporte = {categoria: {"ingresos": 0, "gastos": 0} for categoria in self.categorias_validas}
        
        for t in self.transacciones:
            if t['tipo'] == 'ingreso':
                reporte[t['categoria']]["ingresos"] += t['monto']
            else:
                reporte[t['categoria']]["gastos"] += t['monto']
        
        return reporte

    def filtrar_transacciones(self, tipo=None, categoria=None, mes=None):
        """Filtra transacciones usando comprensión de listas con múltiples criterios"""
        resultado = self.transacciones.copy()
        
        if tipo:
            resultado = [t for t in resultado if t['tipo'] == tipo]
        
        if categoria:
            resultado = [t for t in resultado if t['categoria'] == categoria]
        
        if mes:
            resultado = [t for t in resultado if t['fecha'].split('-')[1] == mes.zfill(2)]
        
        return resultado

    def obtener_mayores_transacciones(self, n=5, tipo="gasto"):
        """Obtiene las n mayores transacciones de un tipo específico"""
        filtradas = [t for t in self.transacciones if t['tipo'] == tipo]
        # Ordenar por monto descendente
        filtradas.sort(key=lambda x: x['monto'], reverse=True)
        return filtradas[:n]

# =============================================
# EJEMPLO DE USO DEL SISTEMA CONTABLE
# =============================================

# Crear instancia del sistema
contabilidad = SistemaContabilidad()

# Agregar transacciones (fecha, descripción, tipo, monto, categoría)
contabilidad.agregar_transaccion("2023-01-05", "Venta producto A", "ingreso", 15000, "Ventas")
contabilidad.agregar_transaccion("2023-01-12", "Compra materiales", "gasto", 4500, "Compras")
contabilidad.agregar_transaccion("2023-01-18", "Pago nómina", "gasto", 8000, "Nómina")
contabilidad.agregar_transaccion("2023-02-03", "Venta servicio B", "ingreso", 9200, "Ventas")
contabilidad.agregar_transaccion("2023-02-10", "Pago impuestos", "gasto", 3500, "Impuestos")
contabilidad.agregar_transaccion("2023-02-15", "Mantenimiento equipos", "gasto", 2100, "Servicios")
contabilidad.agregar_transaccion("2023-02-22", "Venta producto C", "ingreso", 12600, "Ventas")

# Calcular y mostrar balance
balance = contabilidad.calcular_balance()
print(f"\nBalance total: ${balance:.2f}")

# Generar reporte por categorías
reporte = contabilidad.generar_reporte_categorias()
print("\nReporte por categorías:")
for categoria, datos in reporte.items():
    print(f"{categoria}: Ingresos ${datos['ingresos']:.2f} | Gastos ${datos['gastos']:.2f}")

# Filtrar transacciones de febrero
print("\nTransacciones de febrero:")
feb_trans = contabilidad.filtrar_transacciones(mes="02")
for t in feb_trans:
    print(f"{t['fecha']} - {t['descripcion']}: ${t['monto']:.2f} ({t['tipo']})")

# Obtener mayores gastos
print("\nMayores gastos:")
mayores_gastos = contabilidad.obtener_mayores_transacciones(tipo="gasto")
for i, gasto in enumerate(mayores_gastos, 1):
    print(f"{i}. {gasto['descripcion']}: ${gasto['monto']:.2f} ({gasto['categoria']})")