#Análisis del Código
##1. Estructura de Datos
-Cada transacción es una tupla con:

´´´python
(ticker, fecha, precio_por_accion, cantidad, tipo_operacion)
Inmutabilidad: Garantiza que los registros históricos no sean alterados
´´´
#Eficiencia: Menor sobrecarga que diccionarios u objetos para datos simples

## 2. Funciones Clave
### valor_total_por_accion:

- Calcula posición neta por acción

- Considera compras como positivas y ventas como negativas

- Ejemplo: AAPL = (100*150.25) - (75*170.80)

### transacciones_por_fecha:

- Filtra usando comparación directa de strings (formato ISO 8601)

- Devuelve una tupla para evitar modificaciones

### rendimiento_operaciones:

- Implementa método FIFO para cálculo de ganancias

- Empareja ventas con las compras más antiguas

- Retorna lista de tuplas con resultados por operación

### resumen_actividad:

- Usa set comprehension para identificar acciones únicas

- Cuenta operaciones por acción

## 3. ¿Por qué Tuplas?
- Seguridad: Previene modificación accidental de transacciones

- Rendimiento: Procesamiento más rápido que listas para acceso

- Integridad: Ideal para representar registros históricos

- Consistencia: Garantiza estructura homogénea en todos los registros