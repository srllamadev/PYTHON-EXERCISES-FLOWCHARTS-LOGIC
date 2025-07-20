"""
SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO
Este programa simula un sistema de inventario multialmacén con:
- Gestión de productos en múltiples ubicaciones
- Cálculo de rotación de inventario (FIFO)
- Sistema de reabastecimiento automático
- Análisis de movimientos con series temporales
"""

from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt

# =============================================
# VARIABLES GLOBALES
# =============================================
CATEGORIAS = ["Electrónicos", "Ropa", "Alimentos", "Muebles", "Juguetes"]
ALMACENES = ["Norte", "Sur", "Centro", "Este", "Oeste"]
PROVEEDORES = ["ProveedorA", "ProveedorB", "ProveedorC", "ProveedorD"]

# =============================================
# CLASE PRINCIPAL: SISTEMA DE INVENTARIO
# =============================================
class SistemaInventario:
    def __init__(self):
        # Lista principal de productos (cada producto es un diccionario)
        self.productos = []
        
        # Lista de movimientos de inventario (entradas/salidas)
        self.movimientos = []
        
        # Umbrales para reabastecimiento automático
        self.umbral_reabastecimiento = {
            "Electrónicos": 10,
            "Ropa": 20,
            "Alimentos": 50,
            "Muebles": 5,
            "Juguetes": 15
        }
        
        # Tiempo de reposición por proveedor (días)
        self.tiempo_reposicion = {
            "ProveedorA": 3,
            "ProveedorB": 5,
            "ProveedorC": 7,
            "ProveedorD": 10
        }
        
        # Generar datos iniciales
        self._generar_productos_iniciales(50)
        self._simular_movimientos(200)

    def _generar_productos_iniciales(self, cantidad):
        """Genera productos iniciales con datos aleatorios"""
        for i in range(1, cantidad + 1):
            categoria = random.choice(CATEGORIAS)
            proveedor = random.choice(PROVEEDORES)
            precio = round(random.uniform(10, 500), 2)
            costo = round(precio * random.uniform(0.4, 0.8), 2)
            
            # Crear entradas de inventario por almacén
            inventario = []
            for almacen in ALMACENES:
                # Aumentamos el stock inicial mínimo a 50 unidades
                stock = random.randint(50, 150)
                if stock > 0:
                    inventario.append({
                        "almacen": almacen,
                        "stock": stock,
                        "lote": f"LOTE-{random.randint(1000,9999)}",
                        "fecha_ingreso": (datetime.now() - timedelta(days=random.randint(1, 60))).strftime("%Y-%m-%d")
                    })
            
            self.productos.append({
                "id": f"PROD-{i:04d}",
                "nombre": f"Producto {i}",
                "categoria": categoria,
                "proveedor": proveedor,
                "precio": precio,
                "costo": costo,
                "inventario": inventario
            })

    def _simular_movimientos(self, cantidad):
        """Simula movimientos de inventario históricos con manejo de errores"""
        for _ in range(cantidad):
            producto = random.choice(self.productos)
            almacen = random.choice(ALMACENES)
            
            # Aumentamos probabilidad de entradas (70%) vs salidas (30%)
            tipo = random.choices(["entrada", "salida"], weights=[7, 3], k=1)[0]
            
            # Reducimos la cantidad máxima para salidas
            if tipo == "salida":
                cantidad_mov = random.randint(1, 10)  # Máximo 10 unidades
            else:
                cantidad_mov = random.randint(5, 30)  # Entradas entre 5-30
                
            fecha = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
            
            # Intentamos registrar el movimiento
            try:
                self.registrar_movimiento(
                    producto["id"], almacen, tipo, cantidad_mov, fecha
                )
            except ValueError as e:
                # Si hay error de stock insuficiente, lo convertimos en entrada
                if "Stock insuficiente" in str(e):
                    tipo = "entrada"
                    # Volvemos a intentar como entrada
                    self.registrar_movimiento(
                        producto["id"], almacen, tipo, cantidad_mov, fecha
                    )
                else:
                    # Re-lanzamos otros tipos de errores
                    raise

    def registrar_movimiento(self, producto_id, almacen, tipo, cantidad, fecha=None):
        """Registra un movimiento de inventario aplicando FIFO"""
        # Buscar el producto
        producto = next((p for p in self.productos if p["id"] == producto_id), None)
        if not producto:
            raise ValueError(f"Producto {producto_id} no encontrado")
        
        # Obtener inventario específico del almacén
        inv_almacen = next((inv for inv in producto["inventario"] if inv["almacen"] == almacen), None)
        
        # Si no existe registro para este almacén, crearlo
        if not inv_almacen:
            inv_almacen = {
                "almacen": almacen,
                "stock": 0,
                "lote": f"LOTE-NUEVO",
                "fecha_ingreso": datetime.now().strftime("%Y-%m-%d")
            }
            producto["inventario"].append(inv_almacen)
        
        # Manejar entrada/salida
        if tipo == "entrada":
            inv_almacen["stock"] += cantidad
        elif tipo == "salida":
            if inv_almacen["stock"] < cantidad:
                raise ValueError(f"Stock insuficiente en {almacen} para {producto_id}")
            inv_almacen["stock"] -= cantidad
        
        # Registrar movimiento
        movimiento = {
            "producto_id": producto_id,
            "almacen": almacen,
            "tipo": tipo,
            "cantidad": cantidad,
            "fecha": fecha or datetime.now().strftime("%Y-%m-%d"),
            "stock_restante": inv_almacen["stock"]
        }
        self.movimientos.append(movimiento)
        
        # Verificar necesidad de reabastecimiento
        self.verificar_reabastecimiento(producto_id, almacen)
        
        return movimiento

    def verificar_reabastecimiento(self, producto_id, almacen):
        """Verifica si se necesita reabastecer y genera pedido automático"""
        producto = next((p for p in self.productos if p["id"] == producto_id), None)
        if not producto:
            return False
            
        inv_almacen = next((inv for inv in producto["inventario"] if inv["almacen"] == almacen), None)
        if not inv_almacen:
            return False
            
        umbral = self.umbral_reabastecimiento.get(producto["categoria"], 10)
        
        if inv_almacen["stock"] <= umbral:
            # Calcular cantidad a pedir (doble del umbral)
            cantidad_pedido = umbral * 2
            tiempo_reposicion = self.tiempo_reposicion.get(producto["proveedor"], 5)
            fecha_estimada = (datetime.now() + timedelta(days=tiempo_reposicion)).strftime("%Y-%m-%d")
            
            print(f"⚠️ Generando pedido de {cantidad_pedido} unidades de {producto_id} para {almacen}")
            print(f"   Proveedor: {producto['proveedor']}, Entrega estimada: {fecha_estimada}")
            
            # Simular entrada futura
            self.registrar_movimiento(
                producto_id, almacen, "entrada", cantidad_pedido, fecha_estimada
            )
            
            return True
        return False

    def calcular_valor_inventario(self):
        """Calcula el valor total del inventario por categoría y almacén"""
        # Estructura para resultados: {categoria: {almacen: valor}}
        valor_inventario = {cat: {alm: 0.0 for alm in ALMACENES} for cat in CATEGORIAS}
        
        for producto in self.productos:
            for inv in producto["inventario"]:
                valor = inv["stock"] * producto["costo"]
                valor_inventario[producto["categoria"]][inv["almacen"]] += valor
        
        return valor_inventario

    def analisis_rotacion(self, dias=30):
        """Analiza rotación de inventario en los últimos N días"""
        fecha_limite = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d")
        movimientos_recientes = [m for m in self.movimientos if m["fecha"] >= fecha_limite]
        
        # Calcular rotación por categoría
        rotacion = {cat: {"entradas": 0, "salidas": 0} for cat in CATEGORIAS}
        
        for mov in movimientos_recientes:
            producto = next((p for p in self.productos if p["id"] == mov["producto_id"]), None)
            if not producto:
                continue
                
            cat = producto["categoria"]
            
            if mov["tipo"] == "entrada":
                rotacion[cat]["entradas"] += mov["cantidad"]
            else:
                rotacion[cat]["salidas"] += mov["cantidad"]
        
        # Calcular ratio de rotación
        for cat, datos in rotacion.items():
            total_movimientos = datos["entradas"] + datos["salidas"]
            datos["ratio"] = total_movimientos / dias if dias > 0 else 0
        
        return rotacion

    def generar_reporte_estado(self):
        """Genera reporte de estado de inventario"""
        print("\n" + "="*50)
        print("REPORTE DE ESTADO DE INVENTARIO")
        print("="*50)
        
        valor_inventario = self.calcular_valor_inventario()
        rotacion = self.analisis_rotacion()
        
        # Imprimir por categoría
        for categoria in CATEGORIAS:
            print(f"\n🔹 {categoria.upper()}")
            print(f"  Rotación (últimos 30 días): {rotacion[categoria]['ratio']:.2f} movimientos/día")
            print(f"  Valor total en inventario: ${sum(valor_inventario[categoria].values()):,.2f}")
            
            # Detalle por almacén
            for almacen, valor in valor_inventario[categoria].items():
                print(f"  - {almacen}: ${valor:,.2f}")

    def visualizar_tendencias(self):
        """Visualiza tendencias de inventario usando matplotlib"""
        # Preparar datos para gráfico de series temporales
        fechas = sorted(set(mov["fecha"] for mov in self.movimientos))
        datos_por_fecha = {fecha: {"entradas": 0, "salidas": 0} for fecha in fechas}
        
        for mov in self.movimientos:
            if mov["tipo"] == "entrada":
                datos_por_fecha[mov["fecha"]]["entradas"] += mov["cantidad"]
            else:
                datos_por_fecha[mov["fecha"]]["salidas"] += mov["cantidad"]
        
        # Convertir a listas ordenadas
        fechas_ordenadas = sorted(fechas)
        entradas = [datos_por_fecha[f]["entradas"] for f in fechas_ordenadas]
        salidas = [datos_por_fecha[f]["salidas"] for f in fechas_ordenadas]
        
        # Crear gráfico
        plt.figure(figsize=(12, 6))
        plt.plot(fechas_ordenadas, entradas, 'g-', label='Entradas')
        plt.plot(fechas_ordenadas, salidas, 'r-', label='Salidas')
        plt.title('Tendencias de Movimientos de Inventario')
        plt.xlabel('Fecha')
        plt.ylabel('Cantidad')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

# =============================================
# EJECUCIÓN DEL SISTEMA
# =============================================
if __name__ == "__main__":
    sistema = SistemaInventario()
    
    # Generar reporte de estado
    sistema.generar_reporte_estado()
    
    # Visualizar tendencias (con manejo de errores)
    try:
        sistema.visualizar_tendencias()
    except Exception as e:
        print(f"\n⚠️ Error al generar gráfico: {str(e)}")
        print("Asegúrate de tener matplotlib instalado: pip install matplotlib")
    
    # Simular nueva venta
    print("\nSimulando nueva venta...")
    producto_venta = random.choice(sistema.productos)
    almacen_venta = random.choice(ALMACENES)
    sistema.registrar_movimiento(
        producto_venta["id"], almacen_venta, "salida", 15
    )
    print(f"Venta registrada: 15 unidades de {producto_venta['id']} en {almacen_venta}")
    
    # Generar reporte actualizado
    sistema.generar_reporte_estado()