import datetime
import csv
import os

class SistemaContabilidadTributaria:
    def __init__(self, empresa):
        """
        Inicializa el sistema tributario:
        - empresa: Diccionario con datos fiscales
        - transacciones: Lista de operaciones contables
        - impuestos: Configuración de alícuotas (actualizado a 2025)
        """
        self.empresa = empresa
        self.transacciones = []
        self.impuestos = {
            'IVA': 0.13,         # 13%
            'RC_IVA': 0.20,       # Régimen Complementario al IVA (20%)
            'IT': 0.03,           # Impuesto a las Transacciones (3%)
            'IUE': 0.25           # Impuesto a las Utilidades (25%)
        }
        self.libros = {
            'ventas': [],
            'compras': []
        }
    
    def registrar_transaccion(self, tipo, monto, nit_cliente=None, fecha=None):
        """
        Registra transacción con desglose tributario automático
        Tipos: 'venta', 'compra', 'gasto', 'inversion'
        """
        fecha = fecha or datetime.date.today()
        transaccion = {
            'id': len(self.transacciones) + 1,
            'tipo': tipo,
            'fecha': fecha,
            'monto_base': monto,
            'nit_cliente': nit_cliente,
            'impuestos': {}
        }

        # Cálculo de impuestos según tipo
        if tipo == 'venta':
            transaccion['impuestos']['IVA'] = monto * self.impuestos['IVA']
            transaccion['impuestos']['IT'] = monto * self.impuestos['IT']
            
        elif tipo == 'compra':
            transaccion['impuestos']['IVA'] = monto * self.impuestos['IVA']
            
            # Aplicar RC-IVA si supera umbral
            if monto > 50000:  # Supuesto: 50,000 BOB
                transaccion['impuestos']['RC_IVA'] = monto * self.impuestos['RC_IVA']
        
        elif tipo in ('gasto', 'inversion'):
            # Solo IUE aplica en liquidación anual
            pass

        self.transacciones.append(transaccion)
        
        # Actualizar libros contables
        if tipo == 'venta':
            self.libros['ventas'].append(transaccion)
        elif tipo == 'compra':
            self.libros['compras'].append(transaccion)
            
        return transaccion

    def generar_libro_ventas(self, mes, año):
        """Genera libro de ventas formato SIFAC (Bolivia)"""
        filename = f"Libro_Ventas_{self.empresa['nit']}_{mes}_{año}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([
                "NIT Emisor", "Razón Social", "Periodo",
                "Fecha", "NIT Comprador", "Monto Total",
                "IVA", "IT", "RC-IVA"
            ])
            
            for venta in self.libros['ventas']:
                if venta['fecha'].month == mes and venta['fecha'].year == año:
                    writer.writerow([
                        self.empresa['nit'],
                        self.empresa['razon_social'],
                        f"{mes}-{año}",
                        venta['fecha'].strftime("%d/%m/%Y"),
                        venta['nit_cliente'],
                        venta['monto_base'],
                        venta['impuestos'].get('IVA', 0),
                        venta['impuestos'].get('IT', 0),
                        venta['impuestos'].get('RC_IVA', 0)
                    ])
        return filename

    def calcular_obligaciones_mensuales(self, mes, año):
        """Calcula impuestos a pagar mensualmente"""
        ventas_mes = [t for t in self.transacciones 
                     if t['tipo'] == 'venta' 
                     and t['fecha'].month == mes 
                     and t['fecha'].year == año]
        
        compras_mes = [t for t in self.transacciones 
                      if t['tipo'] == 'compra' 
                      and t['fecha'].month == mes 
                      and t['fecha'].year == año]
        
        # Cálculos principales
        total_iva_ventas = sum(t['impuestos'].get('IVA', 0) for t in ventas_mes)
        total_iva_compras = sum(t['impuestos'].get('IVA', 0) for t in compras_mes)
        iva_por_pagar = max(0, total_iva_ventas - total_iva_compras)
        
        total_it = sum(t['impuestos'].get('IT', 0) for t in ventas_mes)
        total_rc_iva = sum(t['impuestos'].get('RC_IVA', 0) for t in compras_mes)
        
        return {
            'IVA': iva_por_pagar,
            'IT': total_it,
            'RC_IVA': total_rc_iva,
            'Total': iva_por_pagar + total_it + total_rc_iva
        }

    def liquidacion_iue(self, año):
        """Calcula Impuesto a las Utilidades (anual)"""
        utilidad_bruta = sum(
            t['monto_base'] for t in self.transacciones 
            if t['tipo'] == 'venta' and t['fecha'].year == año
        ) - sum(
            t['monto_base'] for t in self.transacciones 
            if t['tipo'] in ('compra', 'gasto') and t['fecha'].year == año
        )
        
        iue = max(0, utilidad_bruta * self.impuestos['IUE'])
        return iue

# Configuración inicial de empresa
empresa_boliviana = {
    'nit': '1020304050',
    'razon_social': 'TECNOLOGIA ANDINA S.A.',
    'actividad_economica': 'DESARROLLO DE SOFTWARE',
    'regimen': 'REGIMEN GENERAL'
}

# Crear sistema contable
sistema = SistemaContabilidadTributaria(empresa_boliviana)

# Registrar transacciones de ejemplo
sistema.registrar_transaccion('venta', 150000, '1456789012', datetime.date(2025, 6, 15))
sistema.registrar_transaccion('compra', 80000, '2345678901', datetime.date(2025, 6, 20))
sistema.registrar_transaccion('venta', 45000, '3456789012', datetime.date(2025, 7, 3))
sistema.registrar_transaccion('compra', 55000, '4567890123', datetime.date(2025, 7, 10))  # Supera umbral RC-IVA

# Generar reportes
print("\n=== Obligaciones Tributarias Julio 2025 ===")
obligaciones = sistema.calcular_obligaciones_mensuales(7, 2025)
for imp, monto in obligaciones.items():
    print(f"{imp}: {monto:.2f} BOB")

print("\nGenerando libro de ventas...")
libro_ventas = sistema.generar_libro_ventas(7, 2025)
print(f"Archivo generado: {libro_ventas}")

print("\n=== Liquidación Anual IUE 2025 ===")
iue = sistema.liquidacion_iue(2025)
print(f"Impuesto a las Utilidades: {iue:.2f} BOB")