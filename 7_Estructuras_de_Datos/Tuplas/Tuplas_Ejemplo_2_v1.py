# Base de datos de transacciones: (ticker, fecha, precio, cantidad, tipo)
transacciones = [
    ('AAPL', '2023-01-15', 150.25, 100, 'compra'),
    ('MSFT', '2023-01-16', 250.50, 50, 'compra'),
    ('AAPL', '2023-02-20', 170.80, 75, 'venta'),
    ('GOOGL', '2023-03-05', 1250.75, 30, 'compra'),
    ('MSFT', '2023-04-18', 275.30, 50, 'venta'),
    ('TSLA', '2023-05-22', 700.40, 25, 'compra')
]

# Calcula posición neta por acción (compras positivas, ventas negativas)
def valor_total_por_accion(transacciones, accion):
    total = 0
    for ticker, _, precio, cantidad, tipo in transacciones:
        if ticker == accion:
            total += precio * cantidad * (1 if tipo == 'compra' else -1)
    return round(total, 2)

# Filtra transacciones por rango de fechas (devuelve tupla inmutable)
def transacciones_por_fecha(transacciones, fecha_inicio, fecha_fin):
    return tuple(
        t for t in transacciones 
        if fecha_inicio <= t[1] <= fecha_fin
    )

# Calcula ganancias usando método FIFO (First-In First-Out)
def rendimiento_operaciones(transacciones):
    compras = {}
    ventas = {}
    
    # Clasificar operaciones por acción
    for t in transacciones:
        ticker, _, precio, cantidad, tipo = t
        if tipo == 'compra':
            compras.setdefault(ticker, []).append((precio, cantidad))
        else:
            ventas.setdefault(ticker, []).append((precio, cantidad))
    
    # Calcular ganancias emparejando ventas con compras (FIFO)
    resultados = []
    for ticker, ventas_ticker in ventas.items():
        for v_precio, v_cantidad in ventas_ticker:
            while v_cantidad > 0 and compras.get(ticker):
                c_precio, c_cantidad = compras[ticker][0]
                cantidad_vendida = min(v_cantidad, c_cantidad)
                
                ganancia = (v_precio - c_precio) * cantidad_vendida
                resultados.append((ticker, ganancia))
                
                # Actualizar inventario de compras
                if c_cantidad == cantidad_vendida:
                    compras[ticker].pop(0)
                    if not compras[ticker]: 
                        del compras[ticker]
                else:
                    compras[ticker][0] = (c_precio, c_cantidad - cantidad_vendida)
                
                v_cantidad -= cantidad_vendida
    
    return resultados

# Genera resumen de operaciones por acción
def resumen_actividad(transacciones):
    acciones = {t[0] for t in transacciones}
    return tuple(
        (accion, sum(1 for t in transacciones if t[0] == accion))
        for accion in acciones
    )

# Ejecución principal
if __name__ == "__main__":
    # 1. Valor total por acción
    print("Valor neto AAPL:", valor_total_por_accion(transacciones, 'AAPL'))
    
    # 2. Transacciones en Q1 2023
    print("\nTransacciones Q1-2023:")
    for t in transacciones_por_fecha(transacciones, '2023-01-01', '2023-03-31'):
        print(t)
    
    # 3. Cálculo de ganancias
    print("\nGanancias por operación:")
    for accion, ganancia in rendimiento_operaciones(transacciones):
        print(f"{accion}: ${ganancia:+.2f}")
    
    # 4. Resumen de actividad
    print("\nOperaciones por acción:")
    for accion, count in resumen_actividad(transacciones):
        print(f"{accion}: {count} operaciones")