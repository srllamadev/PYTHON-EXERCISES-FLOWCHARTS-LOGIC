
# Características Tributarias Implementadas

## Impuestos Clave

- **IVA (13%)**: Calculado en ventas y compras.
- **RC-IVA (20%)**: Aplicado a compras > 50,000 BOB (valor referencial).
- **IT (3%)**: Sobre todas las ventas.
- **IUE (25%)**: Sobre utilidades anuales.

## Libros Oficiales

- Generación de Libro de Ventas en formato CSV compatible con SIFAC.
- Estructura con campos requeridos por normativa boliviana.

## Cálculos Automatizados

- Obligaciones mensuales (IVA, IT, RC-IVA).
- Liquidación anual de IUE.
- Desglose de impuestos por transacción.

## Flujo de Trabajo

1. Registrar transacciones con tipo y monto.
2. Generar libro de ventas para presentación ante Impuestos Nacionales.
3. Calcular obligaciones mensuales.
4. Realizar liquidación anual de IUE.

## Ejemplo de Salida

=== Obligaciones Tributarias Julio 2025 ===
IVA: 5850.00 BOB
IT: 1350.00 BOB
RC-IVA: 11000.00 BOB
Total: 18200.00 BOB

Generando libro de ventas...
Archivo generado: Libro_Ventas_1020304050_7_2025.csv

=== Liquidación Anual IUE 2025 ===
Impuesto a las Utilidades: 15000.00 BOB

markdown

Copiar

## Consideraciones Legales (Simplificadas)

- **RC-IVA**: Aplicable cuando compras superan cierto umbral (verificar valores actualizados).
- **IUE**: Se calcula sobre utilidades netas (ingresos - gastos deducibles).
- **IT**: Obligatorio para todas las ventas.

## Plazos

- **Libros de venta**: Hasta el 15 del mes siguiente.
- **Pago de impuestos**: Depende del NIT (cronograma de obligaciones).

## Mejoras Recomendadas

- Integración con facturación electrónica.
- Cálculo de depreciaciones para IUE.
- Manejo de créditos fiscales.
- Conexión con sistemas gubernamentales (SIN, SIFAC).
- Validación de NITs con algoritmo de módulo 11.

---

> **¡Importante!** Este es un modelo educativo 