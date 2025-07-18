import random

class SistemaInventario:
    def __init__(self, productos):
        """
        Inicializa el sistema con:
        - productos: Diccionario {nombre: [stock_actual, stock_mínimo, precio]}
        - historial: Registro de movimientos
        - eventos_aleatorios: Factores de riesgo
        """
        self.productos = productos
        self.historial = []
        self.eventos_aleatorios = {
            "demanda_pico": 0.3,   # Probabilidad de aumento repentino de demanda
            "fallo_suministro": 0.2 # Probabilidad de fallo en reabastecimiento
        }
    
    def simular_dia(self, dias=30):
        """
        Simula la operación diaria del inventario durante 'dias':
        - Ventas aleatorias con fluctuaciones
        - Reabastecimiento automático
        - Manejo de eventos imprevistos
        """
        print(f"\n{'='*50}\nSimulando {dias} días de operación\n{'='*50}")
        
        # Bucle principal por días
        for dia in range(1, dias + 1):
            eventos_dia = []
            print(f"\nDía {dia}: {'-'*40}")
            
            # Paso 1: Simular ventas diarias
            for producto, datos in self.productos.items():
                stock_actual, stock_min, precio = datos
                
                # Calcular venta base + fluctuación aleatoria
                venta_base = random.randint(1, 5)
                venta_real = venta_base + (random.randint(0, 3) if random.random() < self.eventos_aleatorios["demanda_pico"] else 0)
                
                # Aplicar venta y actualizar stock
                venta_real = min(venta_real, stock_actual)
                self.productos[producto][0] -= venta_real
                
                if venta_real > 0:
                    eventos_dia.append(f"Venta: {venta_real} {producto} (${venta_real * precio:.2f})")
            
            # Paso 2: Verificar y reabastecer inventario
            for producto in self.productos.keys():
                stock_actual, stock_min, _ = self.productos[producto]
                
                # Lógica de reorden usando while para reintentos
                if stock_actual <= stock_min:
                    cantidad_orden = stock_min * 3  # Cantidad fija de reabastecimiento
                    reintentos = 3
                    
                    while reintentos > 0:
                        # Verificar fallo de suministro
                        if random.random() < self.eventos_aleatorios["fallo_suministro"]:
                            eventos_dia.append(f"Fallo suministro {producto} (Reintentos: {reintentos-1})")
                            reintentos -= 1
                        else:
                            self.productos[producto][0] += cantidad_orden
                            eventos_dia.append(f"Reabastecido: +{cantidad_orden} {producto}")
                            break
            
            # Paso 3: Reporte diario
            print("\nEventos del día:")
            for evento in eventos_dia:
                print(f" - {evento}")
            
            self._generar_reporte_estado()
    
    def _generar_reporte_estado(self):
        """Muestra el estado actual del inventario con formato tabular"""
        print("\nEstado de inventario:")
        print(f"{'Producto':<15} | {'Stock':<6} | {'Mínimo':<6} | {'Estado':<10}")
        print("-"*45)
        
        for producto, (stock, minimo, _) in self.productos.items():
            estado = "CRÍTICO" if stock <= minimo else "OK" if stock <= minimo * 2 else "SANO"
            print(f"{producto:<15} | {stock:<6} | {minimo:<6} | {estado:<10}")

# Configuración inicial del inventario
productos_iniciales = {
    "Laptops": [15, 5, 1200],
    "Smartphones": [30, 10, 800],
    "Tablets": [20, 8, 600],
    "Smartwatches": [25, 7, 300]
}

# Ejecutar simulación
sistema = SistemaInventario(productos_iniciales)
sistema.simular_dia(10)